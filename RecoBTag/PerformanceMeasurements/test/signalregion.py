import os
#import numpy
import glob
import math    

import ROOT 
#ROOT.gROOT.Macro("rootlogon.C")
from ROOT import *

import FWCore.ParameterSet.Config as cms

import sys
from DataFormats.FWLite import Events, Handle

import JetInfoBranches
from JetInfoBranches import *

from array import *

from optparse import OptionParser
parser = OptionParser()

parser.add_option("-o", "--outName", dest="outName",
                  help="output file name")
#parser.add_option("-t", "--saveTrig", dest="saveTrig",
#                  help="trigger info saved")
#parser.add_option("-b", "--ttbar", dest="ttbar",
#                  help="isttbar")
#parser.add_option("-d", "--data", dest="data",
#                  help="isdata")
(options, args) = parser.parse_args()
outputfilename = options.outName

#numberLimit = float(sys.argv[1])

f = ROOT.TFile.Open(sys.argv[1],"READ")

f2 =  ROOT.TFile(outputfilename, 'recreate')
#print outputfilename
f2.cd()

JetInfoBranches FatJetInfo
treeMine  = f.Get('btaganaFatJets/ttree')
FatJetInfo.ReadTree(treeMine,"FatJetInfo");
myTree = ROOT.TTree('myTree', 'myTree')

doubleb1 = ROOT.TH1F("doubleb1", "Double B Tagger", 400, -20, 20)

nevent = treeMine.GetEntries();
counter = 0
for i in range(0, nevent) :
    counter = counter + 1
    treeMine.GetEntry(i)
    for j in range(FatJetInfo.nJet):
        doubleb1.Fill(FatJetInfo.Jet_LSF_LSF[j])

    myTree.Fill()

f2.cd()
f2.Write()
f2.Close()

f.Close()


