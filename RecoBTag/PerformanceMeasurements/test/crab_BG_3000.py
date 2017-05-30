from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'BG_3000_puppi'
 
config.section_('JobType')
config.JobType.psetName = 'runBTagAnalyzer_cfg.py'
config.JobType.pluginName = 'Analysis'
config.JobType.pyCfgParams = ['miniAOD=True','runFatJets=True','runSubJets=True', 'processStdAK4Jets=False', 'usePuppi=True']

config.section_('Data')
config.Data.inputDataset = '/BulkGravTohhTohVVhbb_narrow_M-3000_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
config.Data.unitsPerJob = 10
config.Data.splitting = 'FileBased'
config.Data.inputDBS = 'global'
config.Data.outputDatasetTag = "BG_3000_puppi"
config.section_('User')

config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC'
