from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'Zp_puppi'
 
config.section_('JobType')
config.JobType.psetName = 'runBTagAnalyzer_cfg.py'
config.JobType.pluginName = 'Analysis'
config.JobType.pyCfgParams = ['miniAOD=True','runFatJets=True','runSubJets=True', 'processStdAK4Jets=False','usePuppi=True']

config.section_('Data')
config.Data.inputDataset = '/ZprimeToTT_M-1500_W-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
config.Data.unitsPerJob = 10
config.Data.splitting = 'FileBased'
config.Data.inputDBS = 'global'
config.Data.outputDatasetTag = "Zp_puppi"
config.section_('User')

config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC'
