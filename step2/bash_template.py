from cmsdriver_commands import command_dict
from jinja2 import Template

cmssw_mc_template = """#!/bin/bash

{{ LC_template }}

############
### Computing environments
############
echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node
source /cvmfs/cms.cern.ch/cmsset_default.sh
export BASEDIR=`pwd`

{{ proxy_template }}

############
### LHE step
############
echo "********** LHE start **********"
export SCRAM_ARCH={{ lhe_scram_arch }}
scram p {{ lhe_cmssw }}
cd {{ lhe_cmssw }}/src
eval `scram runtime -sh`

mkdir -p Configuration/GenProduction/python/
mv ${BASEDIR}/monoWprime_hadronizer.py Configuration/GenProduction/python/
xrdcp root://eosuser.cern.ch/{{ path }} ./ ## Copy input file

scram b

{{ lhe_command }}
cmsRun lhe_cfg.py
echo "********** LHE End **********"

############
### GEN step
############
echo "********** GEN start **********"
{{ gen_command }}
cmsRun gen_cfg.py
echo "********** GEN End **********"

############
### SIM step
############
echo "********** SIM start **********"
cd ${BASEDIR}

scram p {{ sim_cmssw }}
cd {{ sim_cmssw }}/src
eval `scram runtime -sh`
scram b

### Move file
mv ${BASEDIR}/{{ lhe_cmssw }}/src/gen.root ./

{{ sim_command }}
cmsRun sim_cfg.py
echo "********** SIM End **********"

############
### DIGI-Premix step
############
echo "********** DIGI Premix start **********"
{{ digi_command }}
cmsRun digi_premix_cfg.py
echo "********** DIGI Premix End **********"

############
### HLT step
############
echo "********** HLT start **********"
cd ${BASEDIR}
export SCRAM_ARCH={{ hlt_scram_arch }}
scram p {{ hlt_cmssw }}
cd {{ hlt_cmssw }}/src
eval `scram runtime -sh`
scram b

### Move file
mv ${BASEDIR}/{{ sim_cmssw }}/src/digiPremix.root ./

{{ hlt_command }}
cmsRun hlt_cfg.py
echo "********** HLT End **********"

############
### RECO step
############
echo "********** RECO start **********"
cd ${BASEDIR}

export SCRAM_ARCH={{ reco_scram_arch }}
cd {{ reco_cmssw }}/src
eval `scram runtime -sh`
scram b

### Move file
mv ${BASEDIR}/{{ hlt_cmssw }}/src/hlt.root ./

{{ reco_command }}
cmsRun reco_cfg.py
echo "********** RECO End **********"

############
### MINIAOD step
############
echo "********** MINIAOD start **********"
cd ${BASEDIR}

scram p {{ miniaod_cmssw }}
cd {{ miniaod_cmssw }}/src
eval `scram runtime -sh`
scram b

### Move file
mv ${BASEDIR}/{{ reco_cmssw }}/src/reco.root ./

{{ miniaod_command }}
cmsRun miniaod_cfg.py
echo "********** MINIAOD End **********"

############
### NANOAOD step
############
echo "********** NANOAOD start **********"
cd ${BASEDIR}

scram p {{ nanoaod_cmssw }}
cd {{ nanoaod_cmssw }}/src
eval `scram runtime -sh`

mv ${BASEDIR}/CustomNanoAOD_AK15.tgz ./
tar -zxf CustomNanoAOD_AK15.tgz

scram b -j 4

### Move file
mv ${BASEDIR}/{{ miniaod_cmssw }}/src/miniaod.root ./

{{ nanoaod_command }}
cmsRun nanoaod_cfg.py
echo "********** NANOAOD End **********"

### Change file name
mv nanoaod.root nanoaod_${3}_${4}.root
xrdfs {{ xrootd_protocol }} mkdir -p {{ eos_localpath }}
xrdcp -f nanoaod_${3}_${4}.root {{ full_eospath }}/nanoaod_${3}_${4}.root

### Backup path to save NanoAOD
{{ cernbox_outpath }}
"""

proxy_template="""
############
### Add x509 proxy
############
export X509_USER_PROXY=${5}
voms-proxy-info -all
voms-proxy-info -all -file ${5}
"""

LC_template = """
############
### Set LANG environments
############
export LC_CTYPE=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
"""


def make_template(eospath: str, year: str, nevt: int = 10, backup: str = "", submit_lpc: bool = False):
    cmd_list = command_dict[year]
    path_list = eospath.split('//')

    cernbox_outpath = f"xrdcp -f nanoaod_${{3}}_${{4}}.root root://eosuser.cern.ch/{backup}/nanoaod_${{3}}_${{4}}.root"
    if backup == "":
        cernbox_outpath = ""

    misc_options = {
        'input': '${2}',
        'nevt': nevt
    }

    cmd_options = {
        'path': '${1}',
        'xrootd_protocol': f'{path_list[0]}//{path_list[1]}/',
        'eos_localpath': f'/{path_list[2]}/',
        'full_eospath': eospath,
        'cernbox_outpath': cernbox_outpath,
        'lhe_scram_arch': cmd_list['LHE']['scram_arch'],
        'lhe_cmssw': cmd_list['LHE']['cmssw'],
        'lhe_command': Template(cmd_list['LHE']['command']).render(misc_options),
        'gen_command': Template(cmd_list['GEN']['command']).render(misc_options),
        'sim_cmssw': cmd_list['SIM']['cmssw'],
        'sim_command': Template(cmd_list['SIM']['command']).render(misc_options),
        'digi_command': Template(cmd_list['DIGI']['command']).render(misc_options),
        'hlt_scram_arch': cmd_list['HLT']['scram_arch'],
        'hlt_cmssw': cmd_list['HLT']['cmssw'],
        'hlt_command': Template(cmd_list['HLT']['command']).render(misc_options),
        'reco_scram_arch': cmd_list['RECO']['scram_arch'],
        'reco_cmssw': cmd_list['RECO']['cmssw'],
        'reco_command': Template(cmd_list['RECO']['command']).render(misc_options),
        'miniaod_cmssw': cmd_list['MINI']['cmssw'],
        'miniaod_command': Template(cmd_list['MINI']['command']).render(misc_options),
        'nanoaod_cmssw': cmd_list['NANO']['cmssw'],
        'nanoaod_command': Template(cmd_list['NANO']['command']).render(misc_options),
        'proxy_template': proxy_template if not submit_lpc else "",
        'LC_template': LC_template if submit_lpc else "",
    }

    bash_script = Template(cmssw_mc_template).render(cmd_options)
    return bash_script
