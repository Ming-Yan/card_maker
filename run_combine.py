import os

def t2w(card,twoPOI):
    
    if twoPOI:os.system("text2workspace.py %s.txt  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel  --PO verbose --PO  'map=.*/higgs:r_higgs[1,0,10]' --PO 'map=.*/hc:r_hc[1,0,10]' -m 125 -o %s_twoPOI.root --channel-masks" %(card,card))
    else:os.system("text2workspace.py %s.txt -m 125 %s.root --channel-masks" %(card,card))
# def generatoronly(prefix,card,cbs,mu=1,blind="blind"):
def asymptotic(prefix,card,cbs,blind="blind",twoPOI=False,rmin=-5000,rmax=5000):
    if twoPOI:
        if "freezeParameters" in cbs: 
            cbs= ","+cbs[cbs.find("freezeParameters")+17:]
        else:cbs=" "+cbs

        os.system("combineTool.py -M AsymptoticLimits -d %s_twoPOI.root -m 125 --there --run blind  --cminDefaultMinimizerStrategy 0 --setParameters r_hc=1,r_higgs=1 --redefineSignalPOIs=r_hc --setParameterRanges r_hc=%.2f,%.2f  -n  %s%s --freezeParameters CMS_higgs%s" %(card, rmin,rmax,card[card.rfind("/")+1:],prefix,cbs))
        os.system("combineTool.py -M AsymptoticLimits -d %s_twoPOI.root -m 125 --there --run blind  --cminDefaultMinimizerStrategy 0 --setParameters r_hc=1,r_higgs=1 --redefineSignalPOIs=r_higgs --setParameterRanges r_higgs=%.2f,%.2f  -n %s%s.r_higgs  --freezeParameters CMS_higgs%s" %(card, rmin,rmax,card[card.rfind("/")+1:],prefix,cbs))
        os.system("combineTool.py -M AsymptoticLimits -d %s_twoPOI.root -m 125 --there --run blind  --cminDefaultMinimizerStrategy 0 --setParameters r_hc=1,r_higgs=1 --redefineSignalPOIs=r_hc --setParameterRanges r_hc=%.2f,%.2f  -n  %s%s --freezeParameters r_higgs%s" %(card, rmin,rmax,card[card.rfind("/")+1:],prefix+"1D",cbs))
        os.system("combineTool.py -M AsymptoticLimits -d %s_twoPOI.root -m 125 --there --run blind  --cminDefaultMinimizerStrategy 0 --setParameters r_hc=1,r_higgs=1 --redefineSignalPOIs=r_higgs --setParameterRanges r_higgs=%.2f,%.2f -n  %s%s.r_higgs --freezeParameters=%s" %(card, rmin,rmax,card[card.rfind("/")+1:],prefix+"1D",cbs[1:]))
    else: os.system("combineTool.py -M AsymptoticLimits -d %s.root -m 125 --there --run blind  --cminDefaultMinimizerStrategy 0 --setParameterRanges r=%.2f,%.2f -n  %s%s %s" %(card, rmin,rmax,card[card.rfind("/")+1:],prefix,cbs))
    
def fitdiagonotistic(prefix,card,cbs,mu=1,blind="blind",twoPOI=False,rmin=-5000,rmax=5000):
    if twoPOI:
        card=card+"_twoPOI"
        cbs = cbs +" --redefineSignalPOIs=r_hc"
    if blind == "blind":
        os.system("combineTool.py  -M FitDiagnostics -d %s.root --there -m 125  -t -1 --expectSignal %d --cminDefaultMinimizerStrategy 0 -n %s_mu%d_%s.preFit --setParameterRanges r=%.2f,%.2f --saveShapes --saveWithUncertainties %s" %(card,mu, card[card.rfind("/")+1:], mu, prefix,rmin,rmax,cbs))
        os.system("combineTool.py  -M FitDiagnostics -d %s.root --there -m 125  -t -1 --expectSignal %d --cminDefaultMinimizerStrategy 0 -n %s_mu%d_%s.ToyFreq --rMin -5000 --rMax 5000 --toysFrequentist --saveShapes --saveWithUncertainties %s" %(card,mu, card[card.rfind("/")+1:], mu, prefix,cbs))
    # if blind =="unblind_CR": os.system("combineTool.py --there -M FitDiagnostics %s.root -m 125  -t -1 --expectSignal %d --cminDefaultMinimizerStrategy 0 -n %s_mu%d_%s --rMin -5000 --rMax 5000 --toysFrequentist --saveShapes --saveWithUncertainties %s" %(card,mu, card[card.rfind("/")+1:], mu, prefix,cbs))
def impact(prefix,card,cbs,mu=1,blind="blind",twoPOI=False,rmin=-500,rmax=500,parallel=5):
    if twoPOI:
        card=card+"_twoPOI"
        os.system("combineTool.py -M Impacts  -d %s.root -m 125 --doInitialFit --robustFit 1 --setParameterRanges r_hc=%.2f,%.2f,r_higgs=-5,5 -P r_higgs -P r_hc -t -1 --setParameters r_hc=%d,r_higgs=%d   -n %s_mu%d_%s --cminDefaultMinimizerStrategy 0 --X-rtd FITTER_DYN_STEP %s"%(card,rmin,rmax,mu,mu,card[card.rfind("/")+1:],mu,prefix,cbs))
        os.system("combineTool.py -M Impacts   -d %s.root -m 125 --doFits --robustFit 1 --setParameterRanges r_hc=%.2f,%.2f,r_higgs=-5,5 -P r_higgs -P r_hc  --allPars -t -1 --setParameters r_hc=%d,r_higgs=%d  -n %s_mu%d_%s --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_analytic %s --parallel %d" %(card,rmin,rmax,mu,mu,card[card.rfind("/")+1:],mu,prefix,cbs,parallel))
    else:
        os.system("combineTool.py -M Impacts  -d %s.root -m 125 --doInitialFit --robustFit 1 --setParameterRanges r=%.2f,%.2f -t -1 --expectSignal %d  -n %s_mu%d_%s --cminDefaultMinimizerStrategy 0 --X-rtd FITTER_DYN_STEP %s"%(card,rmin,rmax,mu,card[card.rfind("/")+1:],mu,prefix,cbs))
        os.system("combineTool.py -M Impacts   -d %s.root -m 125 --doFits --robustFit 1 --setParameterRanges r=%.2f,%.2f --allPars -t -1 --expectSignal %d -n %s_mu%d_%s --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_analytic %s --parallel %d" %(card,rmin,rmax,mu,card[card.rfind("/")+1:],mu,prefix,cbs,parallel))
   
    os.system("combineTool.py  -M Impacts -d %s.root   -m 125 --allPars -o %s_impact_mu%d_%s.json -n %s_mu%d_%s"%(card,card,mu,prefix,card[card.rfind("/")+1:],mu,prefix))
    if twoPOI:
        os.system("plotImpacts.py -i %s_impact_mu%d_%s.json -o %s_impacts_mu%d_%s_r_higgs  --POI r_higgs --transparent"%(card,mu,prefix,card,mu,prefix))
        os.system("plotImpacts.py -i %s_impact_mu%d_%s.json -o %s_impacts_mu%d_%s_r_hc --POI r_hc  --transparent"%(card,mu,prefix,card,mu,prefix))
    else :os.system("plotImpacts.py -i %s_impact_mu%d_%s.json -o %s_impacts_mu%d_%s --transparent"%(card,mu,prefix,card,mu,prefix))

    # --job-mode condor --sub-opts='+JobFlavour = "workday"' --task-name VHccPreFit



# def goodnessoffit(prefix,card,cbs,mu=1,blind="blind",rmin=-5000,rmax=5000,ntoys=500,algo='saturated'):

#     os.system("combineTool.py -M GoodnessOfFit -d %s.root --there  --setParameterRanges r=%.2f,%.2f --algo=%s -n %s_mu%d_%s.%s %s -m 125 --cminDefaultMinimizerStrategy 0" %(card,rmin,rmax,algo,card[card.rfind("/")+1:],mu,prefix,algo,cbs))
#     os.system("combineTool.py -M GoodnessOfFit -d %s.root --there  --setParameterRanges r=%.2f,%.2f --algo=%s -t %d -n %s_mu%d_%s.toy.%s %s   -m 125 --cminDefaultMinimizerStrategy 0" %(card,rmin,rmax,algo,ntoys,card[card.rfind("/")+1:],mu,prefix,algo,cbs))
#     os.system("combineTool.py -M CollectGoodnessOfFit --input %s/higgsCombine%s_mu%d_%s.%s.root --there  --setParameterRanges r=%.2f,%.2f --algo=saturated -t %d -n %s_mu%d_%s.toy %s   -m 125 --cminDefaultMinimizerStrategy 0" %(:card[card.rfind("/")+1],card[card.rfind("/")+1:],mu,prefix,algo,))
#     combineTool.py -M CollectGoodnessOfFit --input output/[outDir]/cmb/higgsCombine.$ALGO.GoodnessOfFit.mH125.root output/[outDir]/cmb/higgsCombine.$ALGO.toys.GoodnessOfFit.mH125.*.root -o cmb_$ALGO.json   

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--prefix", default="",help="prefix name")
    parser.add_argument("-d","--card", help="datacard",required=True)
    parser.add_argument("--cbs", default="",help="combine commands")
    # parser.add_argument("--impact",action="store_true",help="Run impact plots")
    parser.add_argument("-M","--methods",choices=['impact','limit','gof','sigma','fit_diag'])
    parser.add_argument("--blind",default="blind",choices=['blind',"unblind_CR",'unblind'],help="blind option")
    parser.add_argument("--mu",default=1,type=float,help="signal strength")
    parser.add_argument("--twoPOI",action="store_true",help="2POI(float r_higgs,r_cH) fit")
    parser.add_argument("--t2w",action="store_true",help="Run text2workspace")
    parser.add_argument("--rmin",default=-500,help="Run text2workspace")
    parser.add_argument("--rmax",default=800,help="Run text2workspace")
    args = parser.parse_args()
    
    if args.t2w:t2w(args.card,args.twoPOI)

    if args.methods=="limit":asymptotic(args.prefix,args.card,args.cbs,args.blind,args.twoPOI)
    if args.methods=="impact":impact(args.prefix,args.card,args.cbs,args.mu,args.blind,args.twoPOI,args.rmin,args.rmax)
    if args.methods=="fit_diag":fitdiagonotistic(args.prefix,args.card,args.cbs,args.mu,args.blind,args.twoPOI)
    # if args.methods=="gof":
