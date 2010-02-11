import FWCore.ParameterSet.Config as cms

process = cms.Process("EXOMuOct09Skim")

# initialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

#number of Events to be skimmed.
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50000)
)

#replace fileNames  with the file you want to skim
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/F67BCF17-48E2-DE11-98B1-000423D94534.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/E432BCD7-55E2-DE11-B670-001617C3B6CC.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/D0586F90-5FE2-DE11-8976-001D09F24691.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/B60CC58F-5CE2-DE11-9FC7-001D09F24DDF.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/A4D9D21B-58E2-DE11-8F7A-000423D986A8.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/A0FC9BDF-65E2-DE11-A6A1-000423D174FE.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/903D2066-61E2-DE11-9F6E-0019B9F704D6.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/7EFA67BE-66E2-DE11-AE17-001617C3B79A.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/7E34865F-45E2-DE11-896A-000423D98F98.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/76CCDA0D-8AE2-DE11-AF65-0030487A3C9A.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/68ED95B5-50E2-DE11-B4C8-001D09F27003.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/5C4B3A8E-63E2-DE11-A02A-000423D99E46.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/54A3A373-4CE2-DE11-8658-000423D99AAA.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/4693BF9A-40E2-DE11-BDBD-000423D944F8.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/2EC732CC-5CE2-DE11-A781-001D09F290BF.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/2A6903C0-68E2-DE11-B6BA-001D09F28D54.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/26EC6965-4CE2-DE11-ABCF-003048D373AE.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/263E80C6-41E2-DE11-A194-001617C3B66C.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/14D22A92-62E2-DE11-9B14-000423D990CC.root',
        '/store/data/BeamCommissioning09/MinimumBias/RECO/v2/000/123/596/0A71AE7F-4DE2-DE11-8B2F-001D09F251CC.root'

	    )
)

#load the EventContent and Skim cff/i files for EXOMu sub-skim.
process.load('SUSYBSMAnalysis.Skimming.EXOMuOct09_EventContent_cfi')
process.load('SUSYBSMAnalysis.Skimming.EXOMuOct09_cff')

#possible trigger modification by user, defualt HLT_Mu9 in EXOMuOct09_cff.py
#process.exoticaMuHLT.HLTPaths = ['HLT_Mu3']

#define output file name. 
process.exoticaMuOutputModule.fileName = cms.untracked.string('EXOMuOct09.root')#possible EventContent  modification by user
#AODSIMEventContent/AODEventContent/RECOSIMEventContent/RECOEventContent
#by uncommenting next lines.
#from Configuration.EventContent.EventContent_cff import *
#from SUSYBSMAnalysis.Skimming.EXOMuOct09_EventContent_cfi import *
#SpecifiedEvenetContent=cms.PSet(
#    outputCommands = cms.untracked.vstring(
#      "keep *_exoticaHLTMuonFilter_*_*",
#	  "keep *_exoticaRecoMuonFilter_*_*",
#      )
#    )
#process.exoticaMuOutputModule.outputCommands.extend(RECOSIMEventContent.outputCommands)
#process.exoticaMuOutputModule.outputCommands.extend(SpecifiedEvenetContent.outputCommands)

#possible cut modification by user
#process.exoticaHLTMuonFilter.cut=  cms.string('pt > 5.0')
#process.exoticaHLTMuonFilter.minN=   cms.int32(2) 
#process.exoticaRecoMuonFilter.cut=  cms.string('pt > 15.0')

#Possible exoticaMuHLTQualitySeq or exoticaMuRecoQualitySeq selection by user

#process.exoticaMuSkimPath=cms.Path(process.exoticaMuHLTQualitySeq)
process.exoticaMuSkimPath=cms.Path(process.exoticaMuRecoQualitySeq)

process.endPath = cms.EndPath(process.exoticaMuOutputModule)
