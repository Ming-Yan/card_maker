import CombineHarvester.CombineTools.ch as ch
import numpy as np
import os
import argparse
import json
from systematics import AddCommonSystematics,AddSystematics2017
cb = ch.CombineHarvester()
parser = argparse.ArgumentParser()
parser.add_argument(
    "-o",
    "--output_folder",
    default="H+c_cards",
    help="""Subdirectory of ./output/ where the cards are written out to""",
)
parser.add_argument(
    "--year",
    default="2017",
    help="""Year to produce datacards for (2018, 2017 or 2016)""",
)
parser.add_argument(
    "-i", "--input", type=str, required=True, help="observable to the fit"
)
parser.add_argument(
    "-ch",
    "--chn",
    default="ee",
    choices=["ee", "mumu", "emu", "all"],
    type=str,
    help="channel",
)
parser.add_argument("-v", "--version", type=str, required=True, help="version")

args = parser.parse_args()
shapes = os.getcwd()
mass = ["125"]

regions = {"SR": 1, "SR2": 2, "DY_CR": 4, "top_CR": 3}
year = args.year
bkg_proc = ["st", "vv", "vjets", "ttbar", "higgs"]
sig_proc = ["hc"]
cats = {
    "ee": [(1, "SR"), (2, "SR2"), (3, "top_CR"), (4, "DY_CR")],  # ,(5,'HM_CR')],
    "mumu": [(1, "SR"), (2, "SR2"), (3, "top_CR"), (4, "DY_CR")],  # ,(5,'HM_CR')],
    "emu": [(1, "SR"), (2, "SR2"), (3, "top_CR")],  # ,(5,'HM_CR')],
}
with open(args.input) as json_file:
    input_map = json.load(json_file)
    input_map = input_map[args.version]


cb.AddObservations(["*"], ["hc"], ["13TeV"], [args.chn], cats[args.chn])
cb.AddProcesses(["*"], ["hc"], ["13TeV"], [args.chn], bkg_proc, cats[args.chn], False)
cb.AddProcesses(["*"], ["hc"], ["13TeV"], [args.chn], sig_proc, cats[args.chn], True)

## read shapes

for region in regions.keys():

    file = "shape/templates_%s_%s_%s.root" % (region, args.chn, input_map[region])
    file = str(file)
    AddCommonSystematics(cb)
    AddSystematics2017(cb,args.chn)
    cb.cp().channel([args.chn]).signals().bin_id([regions[region]]).ExtractShapes(
        file, "$PROCESS", "$PROCESS_$SYSTEMATIC"
    )
    cb.cp().channel([args.chn]).backgrounds().bin_id([regions[region]]).ExtractShapes(
        file, "$PROCESS", "$PROCESS_$SYSTEMATIC"
    )
    
    rebin = (
        ch.AutoRebin()
        .SetBinThreshold(1.0)
        .SetRebinMode(1)
        .SetPerformRebin(True)
        .SetVerbosity(1)
    )
    
    rebin.Rebin(cb, cb)

ch.SetStandardBinNames(cb)




cb.AddDatacardLineAtEnd("* autoMCStats 0")
cb.AddDatacardLineAtEnd("theory_sig group = CMS_hc CMS_higgs CMS_Br_HWW_theo CMS_Br_HWW_mq CMS_Br_HWW_alphas")
cb.AddDatacardLineAtEnd("theory_bkg group = CMS_vvst CMS_ttbar CMS_vjet")
cb.AddDatacardLineAtEnd("theory_shape group = CMS_scalevar_3pt CMS_UEPS_FSR CMS_UEPS_ISR  CMS_aS_weight CMS_PDF_weight")
cb.AddDatacardLineAtEnd("log group = lumi_13TeV_2017 lumi_13TeV_1718 lumi_13TeV_correlated")

if args.chn=='emu' : 
    cb.AddDatacardLineAtEnd("rateparam group = CMS_SF_tt_emu_13TeV_2017")
    cb.AddDatacardLineAtEnd("shape_exp group = CMS_eleSFs_13TeV_2017 CMS_muSFs_13TeV_2017 CMS_L1prefireweight CMS_puweight_13TeV_2017 CMS_cjetSFs_13TeV_2017")
else : 
    cb.AddDatacardLineAtEnd("rateparam group = CMS_SF_tt_ll_13TeV_2017 CMS_SF_vjets_ll_13TeV_2017" )#%(args.chn,args.chn))
    if args.chn == 'ee':cb.AddDatacardLineAtEnd("shape_exp group = CMS_eleSFs_13TeV_2017 CMS_L1prefireweight CMS_puweight_13TeV_2017 CMS_cjetSFs_13TeV_2017")
    else :cb.AddDatacardLineAtEnd("shape_exp group = CMS_muSFs_13TeV_2017 CMS_L1prefireweight CMS_puweight_13TeV_2017 CMS_cjetSFs_13TeV_2017")

cb.AddDatacardLineAtEnd("shape_JER group = CMS_UES_13TeV_2017 CMS_JES_13TeV_2017 CMS_JER_13TeV_2017")
writer = ch.CardWriter(
    "cards/" + args.version + "_" + args.year + "/$BIN" + ".txt",
    "cards/" + args.version + "_" + args.year + "/input$BIN" + ".root",
)
writer.SetWildcardMasses([])
writer.WriteCards(args.chn, cb.cp().channel([args.chn]))

cb.cp().mass("*").WriteDatacard(
    "cards/" + args.version + "_" + args.year + "/combine" + args.chn + ".txt",
    "cards/" + args.version + "_" + args.year + "/combineinput" + args.chn + ".root",
)




