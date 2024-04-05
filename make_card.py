import CombineHarvester.CombineTools.ch as ch
import numpy as np
import os
import argparse
import json
from systematics import AddCommonSystematics,AddSystematics2017,AddSystematics2018,AddSystematics2016_postVFP,AddSystematics2016_preVFP,group_nuisances
cb = ch.CombineHarvester()
parser = argparse.ArgumentParser()
parser.add_argument(
    "--year",
    "-y",
    default="2017",
    required=True,
    choices=["2016_preVFP", "2016_postVFP", "2017", "2018"],
    help="""Year to produce datacards for (2018, 2017 or 2016)""",
)

parser.add_argument(
    "-ch",
    "--chn",
    default="emu",
    choices=["ee", "mumu", "emu", "all"],
    type=str,
    help="channel",
)
parser.add_argument("-v", "--version", type=str, required=True, help="version")
parser.add_argument("--doshape",action="store_true", default = False,help="run shape uncertainties")
parser.add_argument("--groupunc", choices = ["split","versions","sys_combine","nosyst"],help="run shape uncertainties")
parser.add_argument("--noMCstat",action="store_true", default = False,help="No MC statistical uncertainty")
parser.add_argument("--splitJEC",action="store_true", default = False,help="split JEC into 11 sources")
parser.add_argument("--combine_cards",action="store_true", default = False,help="combine datacards")
args = parser.parse_args()
shapes = os.getcwd()

year = args.year
# bkg_proc = ["st", "vv", "zjets", "ttbar","higgs"]
bkg_proc = ["st", "vv", "zjets", "ttbar",'ggH_hww','qqH_hww','VH_hww','ttH_hww','ggH_htautau','qqH_htautau','VH_htautau','ttH_htautau','hb']

sig_proc = ["hc"]
cats,regions={},{}
with open("shapemap.json") as json_file:
    input_map = json.load(json_file)
    input_map = input_map[args.version]

cats[args.chn]=[]
for i,r in enumerate(input_map.keys(),1):
    regions[r] = i
    cats[args.chn].append(tuple([i,str(r)]))

cb.AddObservations(["*"], ["hc"], ["13TeV"], [args.chn], cats[args.chn])
cb.AddProcesses(["*"], ["hc"], ["13TeV"], [args.chn], bkg_proc, cats[args.chn], False)
cb.AddProcesses(["*"], ["hc"], ["13TeV"], [args.chn], sig_proc, cats[args.chn], True)

## read shapes

for region in regions.keys():
    print(region)
    file = "shape/%s.root" % (input_map[region])
    file = str(file)
    AddCommonSystematics(cb,doshape=args.doshape,splitJEC=args.splitJEC)
    if year=="2016_preVFP": AddSystematics2016_preVFP(cb,args.chn,doshape=args.doshape,splitJEC=args.splitJEC)
    if year=="2016_postVFP": AddSystematics2016_postVFP(cb,args.chn,doshape=args.doshape,splitJEC=args.splitJEC)
    if year=="2017": AddSystematics2017(cb,args.chn,doshape=args.doshape,splitJEC=args.splitJEC)
    if year=="2018": AddSystematics2018(cb,args.chn,doshape=args.doshape,splitJEC=args.splitJEC)
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




if not args.noMCstat:cb.AddDatacardLineAtEnd("* autoMCStats 0")
if args.groupunc!="nosyst":
    group_nuisances(cb,year,scheme=args.groupunc,splitJEC=args.splitJEC)
writer = ch.CardWriter(
    "cards/" + args.version + "_" + args.year + "/$BIN" + ".txt",
    "cards/" + args.version + "_" + args.year + "/input$BIN" + ".root",
)
writer.SetWildcardMasses([])
writer.WriteCards(args.chn, cb.cp().channel([args.chn]))

if args.combine_cards:
    
    dict_cat = {v: k for k, v in dict(cats[args.chn]).items()}
    combine_format={
        "SR_LM_comb":["SR2_LM","SR_LM"],
        "all":["SR2_LM","SR_LM","HM_CR","top_CR"],
        "SR":["SR2_LM","SR_LM","HM_CR"],
        "all1D":["SR2_LM_1D","SR_LM_1D","HM_CR",'top_CR'],
        "SR_1D":["SR2_LM_1D","SR_LM_1D","HM_CR"],
        "SR_1D_LM_comb":["SR2_LM_1D","SR_LM_1D"],
        
    }
    if len(dict_cat)==1:
        combine_format={}
        combine_format["all"]=[list(dict_cat.keys())[0]]
    for comb in combine_format:
        commands="combineCards.py "
        for card in combine_format[comb]:
            commands=commands+(card+"=cards/"+args.version+"_"+str(args.year)+"/hc_"+args.chn+"_"+str(dict_cat[card])+"_13TeV.txt ")
        commands=commands+" >cards/"+args.version+"_"+str(args.year)+"/hc_"+args.chn+"_"+comb+"_13TeV.txt"
        os.system(commands)



