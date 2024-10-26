command_dict = {

    ## 2016 PreVFP
    '2016APV': {
        'LHE': {
            'cmssw': 'CMSSW_10_6_30_patch1',
            'command': 'cmsDriver.py Configuration/GenProduction/python/monoWprime_hadronizer.py --python_filename lhe_cfg.py --filein {{ input }} --fileout file:lhe_{{ seed }}.root --eventcontent LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier LHE --conditions 106X_mcRun2_asymptotic_preVFP_v8 --beamspot Realistic25ns13TeV2016Collision --step NONE --era Run2_2016_HIPM --no_exec --mc -n $EVENTS',
        },
        'GEN': {
            'cmssw': 'CMSSW_10_6_30_patch1',
            'command': 'cmsDriver.py Configuration/GenProduction/python/monoWprime_hadronizer.py --python_filename gen_cfg.py --filein file:lhe_{{ seed }}.root --fileout file:gen_{{ seed }}.root --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN --conditions 106X_mcRun2_asymptotic_preVFP_v8 --beamspot Realistic25ns13TeV2016Collision --step GEN --geometry DB:Extended --era Run2_2016_HIPM --no_exec --mc -n $EVENTS',
        },
        'SIM': {
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename sim_cfg.py --filein file:gen_{{ seed }}.root --fileout file:sim_{{ seed }}.root --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions 106X_mcRun2_asymptotic_preVFP_v8 --beamspot Realistic25ns13TeV2016Collision --step SIM --geometry DB:Extended --era Run2_2016_HIPM --runUnscheduled --no_exec --mc -n $EVENTS',
        },
        'DIGI': {
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename digi_premix_cfg.py --filein file:sim_{{ seed }}.root --fileout file:digiPremix_{{ seed }}.root --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL16_106X_mcRun2_asymptotic_v13-v1/PREMIX" --conditions 106X_mcRun2_asymptotic_preVFP_v8 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --geometry DB:Extended --datamix PreMix --era Run2_2016_HIPM --runUnscheduled --no_exec --mc -n $EVENTS',
        },
        'HLT': {
            'cmssw': 'CMSSW_8_0_36_UL_patch2',
            'command': "cmsDriver.py --python_filename hlt_cfg.py --filein file:digiPremix_{{ seed }}.root --fileout file:hlt_{{ seed }}.root --eventcontent RAWSIM --outputCommand 'keep *_mix_*_*,keep *_genPUProtons_*_*' --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --inputCommands 'keep *','drop *_*_BMTF_*','drop *PixelFEDChannel*_*_*_*' --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --customise_commands 'process.source.bypassVersionCheck = cms.untracked.bool(True)' --step HLT:25ns15e33_v4 --geometry DB:Extended --era Run2_2016 --no_exec --mc -n $EVENTS",
        },
        'RECO': {
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename reco_cfg.py --filein file:hlt_{{ seed }}.root --fileout file:reco_{{ seed }}.root --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions 106X_mcRun2_asymptotic_preVFP_v8 --step RAW2DIGI,L1Reco,RECO,RECOSIM --geometry DB:Extended --era Run2_2016_HIPM --runUnscheduled --no_exec --mc -n $EVENTS',
        },
        'MINI': {
            'cmssw': 'CMSSW_10_6_25',
            'command': 'cmsDriver.py --python_filename miniaod_cfg.py --filein file:reco_{{ seed }}.root --fileout file:miniaod_{{ seed }}.root --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions 106X_mcRun2_asymptotic_preVFP_v11 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --era Run2_2016_HIPM --runUnscheduled --no_exec --mc -n $EVENTS',
        },
        'NANO': {
            'cmssw': 'CMSSW_10_6_32_patch1',
            'command': 'cmsDriver.py --python_filename nanoaod_cfg.py --filein file:miniaod_{{ seed }}.root --fileout file:nanoaod_{{ seed }}.root --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --step NANO --era Run2_2016_HIPM,run2_nanoAOD_106Xv2 --no_exec --mc -n $EVENTS',
        },
    },

    ## 2016 PostVFP
    '2016': {
        'LHE': {
            'cmssw': 'CMSSW_10_6_30_patch1',
            'command': 'cmsDriver.py Configuration/GenProduction/python/monoWprime_hadronizer.py --python_filename lhe_cfg.py --filein {{ input }} --fileout file:lhe_{{ seed }}.root --eventcontent LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier LHE --conditions 106X_mcRun2_asymptotic_v13 --beamspot Realistic25ns13TeV2016Collision --step NONE --era Run2_2016 --no_exec --mc -n $EVENTS',
        },
        'GEN': {
            'cmssw': 'CMSSW_10_6_30_patch1',
            'command': 'cmsDriver.py Configuration/GenProduction/python/monoWprime_hadronizer.py --python_filename gen_cfg.py --filein file:lhe_{{ seed }}.root --fileout file:gen_{{ seed }}.root --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN --conditions 106X_mcRun2_asymptotic_v13 --beamspot Realistic25ns13TeV2016Collision --step GEN --geometry DB:Extended --era Run2_2016 --no_exec --mc -n $EVENTS',
        },
        'SIM': {
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename sim_cfg.py --filein file:gen_{{ seed }}.root --fileout file:sim_{{ seed }}.root --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions 106X_mcRun2_asymptotic_v13 --beamspot Realistic25ns13TeV2016Collision --step SIM --geometry DB:Extended --era Run2_2016 --runUnscheduled --no_exec --mc -n $EVENTS',
        },
        'DIGI': {
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename digi_premix_cfg.py --filein file:sim_{{ seed }}.root --fileout file:digiPremix_{{ seed }}.root --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL16_106X_mcRun2_asymptotic_v13-v1/PREMIX" --conditions 106X_mcRun2_asymptotic_v13 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --geometry DB:Extended --datamix PreMix --era Run2_2016 --runUnscheduled --no_exec --mc -n $EVENTS',
        },
        'HLT': {
            'cmssw': 'CMSSW_8_0_36_UL_patch2',
            'command': "cmsDriver.py --python_filename hlt_cfg.py --filein file:digiPremix_{{ seed }}.root --fileout file:hlt_{{ seed }}.root --eventcontent RAWSIM --outputCommand 'keep *_mix_*_*,keep *_genPUProtons_*_*' --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --inputCommands 'keep *','drop *_*_BMTF_*','drop *PixelFEDChannel*_*_*_*' --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --customise_commands 'process.source.bypassVersionCheck = cms.untracked.bool(True)' --step HLT:25ns15e33_v4 --geometry DB:Extended --era Run2_2016 --no_exec --mc -n $EVENTS",
        },
        'RECO': {
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename reco_cfg.py--filein file:hlt_{{ seed }}.root --fileout file:reco_{{ seed }}.root --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions 106X_mcRun2_asymptotic_v13 --step RAW2DIGI,L1Reco,RECO,RECOSIM --geometry DB:Extended --era Run2_2016 --runUnscheduled --no_exec --mc -n $EVENTS',
        },
        'MINI': {
            'cmssw': 'CMSSW_10_6_25',
            'command': 'cmsDriver.py --python_filename miniaod_cfg.py --filein file:reco_{{ seed }}.root --fileout file:miniaod_{{ seed }}.root --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions 106X_mcRun2_asymptotic_v17 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --era Run2_2016 --runUnscheduled --no_exec --mc -n $EVENTS',
        },
        'NANO': {
            'cmssw': 'CMSSW_10_6_32_patch1',
            'command': 'cmsDriver.py --python_filename nanoaod_cfg.py --filein file:miniaod_{{ seed }}.root --fileout file:nanoaod_{{ seed }}.root --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --conditions 106X_mcRun2_asymptotic_v17 --step NANO --era Run2_2016,run2_nanoAOD_106Xv2 --no_exec --mc -n $EVENTS',
        },
    },

    '2017': {
        'LHE': {
            'cmssw': 'CMSSW_10_6_30_patch1',
            'command': 'cmsDriver.py Configuration/GenProduction/python/monoWprime_hadronizer.py --python_filename lhe_cfg.py --filein {{ input }} --fileout file:lhe_{{ seed }}.root --eventcontent LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier LHE --conditions 106X_mc2017_realistic_v6 --step NONE --era Run2_2017 --no_exec --mc -n $EVENTS',
        },
        'GEN': {
            'cmssw': 'CMSSW_10_6_30_patch1',
            'command': 'cmsDriver.py Configuration/GenProduction/python/monoWprime_hadronizer.py --python_filename gen_cfg.py --filein file:lhe_{{ seed }}.root --fileout file:gen_{{ seed }}.root --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --step GEN --geometry DB:Extended --era Run2_2017 --no_exec --mc -n $EVENTS',
        },
        'SIM': {
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename sim_cfg.py --filein file:gen_{{ seed }}.root --fileout file:sim_{{ seed }}.root --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --step SIM --geometry DB:Extended --era Run2_2017 --runUnscheduled --no_exec --mc -n $EVENTS',
        },
        'DIGI': {
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename digi_premix_cfg.py --filein file:sim_{{ seed }}.root --fileout file:digiPremix_{{ seed }}.root --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL17_106X_mc2017_realistic_v6-v3/PREMIX" --conditions 106X_mc2017_realistic_v6 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --geometry DB:Extended --datamix PreMix --era Run2_2017 --runUnscheduled --no_exec --mc -n $EVENTS',
        },
        'HLT': {
            'cmssw': 'CMSSW_9_4_14_UL_patch1',
            'command': "cmsDriver.py --python_filename hlt_cfg.py --filein file:digiPremix_{{ seed }}.root --fileout file:hlt_{{ seed }}.root --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v15 --customise_commands 'process.source.bypassVersionCheck = cms.untracked.bool(True)' --step HLT:2e34v40 --geometry DB:Extended --era Run2_2017 --no_exec --mc -n $EVENTS",
        },
        'RECO': {
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename reco_cfg.py --filein file:hlt_{{ seed }}.root --fileout file:reco_{{ seed }}.root --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions 106X_mc2017_realistic_v6 --step RAW2DIGI,L1Reco,RECO,RECOSIM --geometry DB:Extended --era Run2_2017 --runUnscheduled --no_exec --mc -n $EVENTS',
        },
        'MINI': {
            'cmssw': 'CMSSW_10_6_20',
            'command': 'cmsDriver.py --python_filename miniaod_cfg.py --filein file:reco_{{ seed }}.root --fileout file:miniaod_{{ seed }}.root --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions 106X_mc2017_realistic_v9 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --era Run2_2017 --runUnscheduled --no_exec --mc -n $EVENTS',
        },
        'NANO': {
            'cmssw': 'CMSSW_10_6_32_patch1',
            'command': 'cmsDriver.py --python_filename nanoaod_cfg.py --filein file:miniaod_{{ seed }}.root --fileout file:nanoaod_{{ seed }}.root --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --conditions 106X_mc2017_realistic_v9 --step NANO --era Run2_2017,run2_nanoAOD_106Xv2 --no_exec --mc -n $EVENTS',
        },
    },

    '2018': {
        'LHE': {
            'cmssw': 'CMSSW_10_6_30_patch1',
            'command': 'cmsDriver.py Configuration/GenProduction/python/monoWprime_hadronizer.py --python_filename lhe_cfg.py --filein {{ input }} --fileout file:lhe_{{ seed }}.root --eventcontent LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier LHE --conditions 106X_upgrade2018_realistic_v4 --step NONE --era Run2_2018 --no_exec --mc -n {{ nevt }}',
        },
        'GEN': {
            'cmssw': 'CMSSW_10_6_30_patch1',
            'command': 'cmsDriver.py Configuration/GenProduction/python/monoWprime_hadronizer.py --python_filename gen_cfg.py --filein file:lhe_{{ seed }}.root --fileout file:gen_{{ seed }}.root --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN --conditions 106X_upgrade2018_realistic_v4 --beamspot Realistic25ns13TeVEarly2018Collision --step GEN --geometry DB:Extended --era Run2_2018 --no_exec --mc -n {{ nevt }}',
        },
        'SIM': {
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename sim_cfg.py --filein file:gen_{{ seed }}.root --fileout file:sim_{{ seed }}.root --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions 106X_upgrade2018_realistic_v11_L1v1 --beamspot Realistic25ns13TeVEarly2018Collision --step SIM --geometry DB:Extended --era Run2_2018 --runUnscheduled --no_exec --mc -n $EVENTS',
        },
        'DIGI': {
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename digi_premix_cfg.py --filein file:sim_{{ seed }}.root --fileout file:digiPremix_{{ seed }}.root --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL18_106X_upgrade2018_realistic_v11_L1v1-v2/PREMIX" --conditions 106X_upgrade2018_realistic_v11_L1v1 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --geometry DB:Extended --datamix PreMix --era Run2_2018 --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'HLT': {
            'cmssw': 'CMSSW_10_2_16_UL',
            'command': "cmsDriver.py --python_filename hlt_cfg.py --filein file:digiPremix_{{ seed }}.root --fileout file:hlt_{{ seed }}.root --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions 102X_upgrade2018_realistic_v15 --customise_commands 'process.source.bypassVersionCheck = cms.untracked.bool(True)' --step HLT:2018v32 --geometry DB:Extended --era Run2_2018 --no_exec --mc -n {{ nevt }}",
        },
        'RECO': {
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename reco_cfg.py --filein file:hlt_{{ seed }}.root --fileout file:reco_{{ seed }}.root --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions 106X_upgrade2018_realistic_v11_L1v1 --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI --geometry DB:Extended --era Run2_2018 --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'MINI': {
            'cmssw': 'CMSSW_10_6_20',
            'command': 'cmsDriver.py --python_filename miniaod_cfg.py --filein file:reco_{{ seed }}.root --fileout file:miniaod_{{ seed }}.root --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions 106X_upgrade2018_realistic_v16_L1v1 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --era Run2_2018 --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'NANO': {
            'cmssw': 'CMSSW_10_6_32_patch1',
            'command': 'cmsDriver.py --python_filename nanoaod_cfg.py --filein file:miniaod_{{ seed }}.root --fileout file:nanoaod_{{ seed }}.root --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --conditions 106X_upgrade2018_realistic_v16_L1v1 --step NANO --era Run2_2018,run2_nanoAOD_106Xv2 --no_exec --mc -n {{ nevt }}',
        },
    }
}