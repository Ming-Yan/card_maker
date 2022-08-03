import CombineHarvester.CombineTools.ch as ch
import numpy as np
import os
import argparse
import json

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
chns = ["ee", "mumu", "emu"]
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
for chn in chns:
    if args.chn != "all" and args.chn != chn:
        continue

    cb.AddObservations(["*"], ["hc"], ["13TeV"], [chn], cats[chn])
    cb.AddProcesses(["*"], ["hc"], ["13TeV"], [chn], bkg_proc, cats[chn], False)
    cb.AddProcesses(["*"], ["hc"], ["13TeV"], [chn], sig_proc, cats[chn], True)

    ## read shapes
    i = 1
    for region in regions.keys():

        file = "shape/templates_%s_%s_%s.root" % (region, chn, input_map[region])
        if region == "top_CR" and chn == "emu":file = "shape/templates_top_CR_emu_jetflav_btagDeepFlavCvB_2017.root"
        file = str(file)
        
        # cb.cp().channel([chn]).signals().bin_id([regions[region]]).ExtractShapes(
            # file, "$PROCESS", "$PROCESS_$SYSTEMATIC"
        # )
        # cb.cp().channel([chn]).backgrounds().bin_id([regions[region]]).ExtractShapes(
        #     file, "$PROCESS", "$PROCESS_$SYSTEMATIC"
        # )
        cb.cp().channel([chn]).signals().bin_id([regions[region]]).ExtractShapes(
            file, "$PROCESS", "$PROCESS"
        )
        cb.cp().channel([chn]).backgrounds().bin_id([regions[region]]).ExtractShapes(
            file, "$PROCESS", "$PROCESS"
        )
        cb.cp().AddSyst(cb,'lumi_13TeV','lnN', ch.SystMap()(1.023))
        
        cb.cp().process(['st','vv']).AddSyst(cb,'CMS_vvst','lnN',ch.SystMap()(1.15))
        cb.cp().process(['ttbar']).AddSyst(cb,'CMS_ttbar','lnN',ch.SystMap()(1.005))
        cb.cp().process(['vjets']).AddSyst(cb,'CMS_vjet','lnN',ch.SystMap()(1.05))
        cb.cp().channel([chn]).process(['ttbar']).AddSyst(cb, 'SF_tt_%s' %(chn),'rateParam',ch.SystMap()(1.0))
        cb.GetParameter('SF_tt_%s' %(chn)).set_range(0.0,5.0)
        if ch != 'emu' :
            cb.cp().channel([chn]).process(['vjets']).AddSyst(cb, 'SF_vjets_%s' %(chn),'rateParam',ch.SystMap()(1.0))
        cb.GetParameter('SF_vjets_%s' %(chn)).set_range(0.0,5.0)
        rebin = (
            ch.AutoRebin()
            .SetBinThreshold(1.0)
            .SetRebinMode(1)
            .SetPerformRebin(True)
            .SetVerbosity(1)
        )
        rebin.Rebin(cb, cb)
        # i=i+1

ch.SetStandardBinNames(cb)
cb.AddDatacardLineAtEnd("* autoMCStats 0")
writer = ch.CardWriter(
    "cards/" + args.version + "_" + args.year + "/$BIN" + ".txt",
    "cards/" + args.version + "_" + args.year + "/input$BIN" + ".root",
)
writer.SetWildcardMasses([])

for chn in chns:

    cb.AddDatacardLineAtEnd("* autoMCStats 0")
    writer.WriteCards(chn, cb.cp().channel([chn]))

cb.cp().mass("*").WriteDatacard(
    "cards/" + args.version + "_" + args.year + "/combine" + args.chn + ".txt",
    "cards/" + args.version + "_" + args.year + "/combineinput" + args.chn + ".root",
)
# cb.AddDatacardLineAtEnd("* autoMCStats 0")
