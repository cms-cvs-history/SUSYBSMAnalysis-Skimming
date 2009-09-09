import FWCore.ParameterSet.Config as cms

process = cms.Process("EXOMuOct09Skim")
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)
#number of Events to be skimmed.
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

#replace fileNames  with the file you want to skim
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    "/store/relval/CMSSW_3_2_6/RelValTTbar_Tauola_2M_PROD/GEN-SIM-RECO/MC_31X_V8-v1/0013/F46F8CA0-D09A-DE11-9DE6-001D09F251E0.root"
	    )
)

#load the EventContent and Skim cff/i files for EXOMu sub-skim.
process.load('SUSYBSMAnalysis.Skimming.EXOMuOct09_EventContent_cfi')
process.load('SUSYBSMAnalysis.Skimming.EXOMuOct09_cff')
process.eventInfo = cms.OutputModule (
    "AsciiOutputModule"
)

#define output file name.
process.exoticaMuOutputModule.fileName = cms.untracked.string('EXOMuOct09.root')

process.exoticaMuSkimPath=cms.Path(process.exoticaMuSeq)
process.endPath = cms.EndPath(process.eventInfo+process.exoticaMuOutputModule)
