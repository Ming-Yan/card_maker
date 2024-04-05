import ROOT,argparse,uproot
import numpy as np
var={"top_CR":"template_mTh","HM_CR":"template_BDT_SR_HM",
    'top_CR_1j':"template_mTh","top_CR_nj":"template_mTh",'HM_CR_1j':"template_BDT_SR_HM",'HM_CR_nj':"template_BDT_SR_HM",'SR_LM':"template_BDT_SR_LM",'SR2_LM':"template_BDT_SR2_LM",'SR_LM_1D':"template_BDT_SR_LM_1D",'SR2_LM_1D':"template_BDT_SR2_LM_1D"}
parser = argparse.ArgumentParser(
    description="Run analysis on baconbits files using processor coffea files"
)
parser.add_argument(
    "-v",
    "--version",
    default=None,
    type=str,
    required=True,
    help="version",
)
parser.add_argument(
    "-y",
    "--year",
    choices=["2016_preVFP","2016_postVFP","2017","2018"],
    default="2017",
    help="year",
)
parser.add_argument(
    "-f","--func",
    choices=["remove_neg","reorder_BDT","merge_bin","merge_top"],
    default="merge_bin",
     help="func",
)
parser.add_argument("-b","--rebin",default=5,type=int,help="rebin")
parser.add_argument("-r","--region",default="top_CR_lowmT",type=str,help="rebin",choices=var.keys())

args = parser.parse_args()
# version="0627_newBDT"

# var={'SR_LM_all':"2017_SR_LM_all_template_BDT2D_SR_LM_all_0608_off.root",'SR2_LM':"2017_SR2_LM_template_BDT2D_SR2_LM_0608_off.root","SR_LM":"2017_SR_LM_template_BDT2D_SR_LM_0608_off.root"}
# var={"SR_LM":"2017_SR_LM_template_nbin16_septrain_SR_LM.root"}#"SR_LM":"2017_SR_LM_template_nbin30_septrain_SR_LM.root","SR2_LM":"2017_SR2_LM_template_nbin50_septrain_SR2_LM.root"}
def getall(d, basepath="/"):
    "Generator function to recurse into a ROOT file/dir and yield (path, obj) pairs"
    for key in d.GetListOfKeys():
        kname = key.GetName()
        if key.IsFolder():
            # TODO: -> "yield from" in Py3
            for i in getall(d.Get(kname), basepath+kname+"/"):
                yield i
        else:
            yield basepath+kname, d.Get(kname)
def remove_neg(year,version,regions="top_CR_lowmT"):
    print("=======> remove negative bins")

    for region in [regions]:
        f = ROOT.TFile.Open("shape/%s_%s_%s_%s.root"%(year,region,var[region],version),"update")
        # f= ROOT.TFile.Open("shape/%s" %(var[region]),"update")
        # fup = uproot.open("shape/%s" %(var[region]))
        fup=uproot.open("shape/%s_%s_%s_%s.root"%(year,region,var[region],version))
        
        for h in fup.keys():
            hist = f.Get(h)
            negbins=False
            for bins in range(1,hist.GetNbinsX()):
                # for yb in range(1,hist.GetNbinsY()):
                if hist.GetBinContent(bins)>=0:continue
                print(h,hist.GetBinContent(bins))
                hist.SetBinContent(bins,0.)
                hist.SetBinError(bins,0.)
                negbins=True
            if negbins:
                f.Delete(h)
                hist.Write()
def reorder_BDT(year,version):  
    for region in ["SR_LM","SR2_LM"]:
        f = ROOT.TFile.Open("shape/%s_%s_template_BDT_%s_%s.root"%(year,region,region,version))
        f2 = ROOT.TFile.Open("shape/%s_%s_template_BDT_%s_%s_update.root"%(year,region,region,version),"recreate")
        fup=uproot.open("shape/%s_%s_template_BDT_%s_%s.root"%(year,region,region,version))
        if year!="preVFP":sig,bkg = np.zeros(len(fup["hc;1"].values)+1),np.zeros(len(fup["hc;1"].values)+1)
        else:sig,bkg = np.zeros(len(fup["hc;1"].values)),np.zeros(len(fup["hc;1"].values))
        for s in ['ttbar', 'st', 'zjets', 'vv', 'ggH_hww', 'qqH_hww', 'VH_hww', 'ttH_hww', 'ggH_htautau', 'qqH_htautau', 'VH_htautau', 'ttH_htautau', 'hc', 'hb']:#["ttbar;1","st;1","zjets;1","vv;1","higgs;1","hc;1"]:
            h = f.Get("%s;1" %(s))
            for b in range(len(sig)):
                if "hc" in s :sig[b] = h.GetBinContent(b+1)
                else :
                    bkg[b] = h.GetBinContent(b+1)+bkg[b]
        

        index_map=list(np.argsort(sig/np.sqrt(bkg)))
        # index_map[]
        # print(sig[index_map])
        hist = f.Get("hc;1")
        bb=[]
        for b in range(0,len(sig)):
            bb.append(hist.GetBinContent(index_map[b]+1))
        print(bb)
        for h in fup.keys():
            hist = f.Get(h)
            #f.Delete(h)
            hist_new = ROOT.TH1F(h.replace(";1",""),h.replace(";1",""),len(sig),0,len(sig))
            
            for bins in range(0,len(sig)):
                content=hist.GetBinContent(index_map[bins]+1)
                error=hist.GetBinError(index_map[bins]+1)
                hist_new.SetBinContent(bins+1,content)
                hist_new.SetBinError(bins+1,error)
                if "hc" in h : print(hist_new.GetBinContent(bins+1))
        
        #     
            f2.WriteObject(hist_new,hist.GetName())
            #hist_new.Write()
        # hist = f.Get("hc;1")
        # for b in range(1,len(sig)):
        #     print(hist.GetBinContent(b),b)
            # print(hist.GetBinContent(b))
def merge_bin(year,version,rebin=5,region="top_CR_lowmT"):
    for r in [region]:
        # f = ROOT.TFile.Open("shape/%s_%s_%s_%s.root"%(year,region,var[region],version))
        f = ROOT.TFile.Open("shape/%s_%s_%s_%s_rebin%d.root"%(year,region,var[region],version,rebin),"recreate")
        fs =ROOT.TFile.Open("shape/%s_%s_%s_%s.root"%(year,region,var[region],version))

        # f.cd()
        for k, o in getall(fs):
            hist=o

            bins=hist.GetNbinsX()
            # print(bins)
            
            if type(rebin) is int and bins%rebin==0:hist.Rebin(int(bins/rebin))
            else:hist =hist.Rebin(len(rebin)-1,hist.GetName(),rebin)
            # else: raise Exception("rebin not possible")
            f.WriteObject(hist,hist.GetName())

def merge_top(year,version,region,rebin):
    r = {"top_CR":"template_mTh","HM_CR":"template_BDT_SR_HM"}

    fm = ROOT.TFile.Open("shape/%s_%s_%s_%s.root"%(year,region,r[region],version),"recreate")
    f1 =ROOT.TFile.Open("shape/%s_%s_1j_%s_%s_rebin%d.root"%(year,region,r[region],version,rebin))
    fu=uproot.open("shape/%s_%s_1j_%s_%s_rebin%d.root"%(year,region,r[region],version,rebin))
    f2 =ROOT.TFile.Open("shape/%s_%s_nj_%s_%s_rebin%d.root"%(year,region,r[region],version,rebin))
    for h in fu.keys():
        hist1 = f1.Get(h)
        hist2 = f2.Get(h)
        bins=hist1.GetNbinsX()
        histall=hist1
        for i in range(1,bins+1):
            histall.SetBinContent(i,hist1.GetBinContent(i)+hist2.GetBinContent(i))
            histall.SetBinError(i,np.sqrt(hist1.GetBinError(i)**2+hist2.GetBinError(i)**2))
        # print(bins)
        
        # if type(rebin) is int and bins%rebin==0:hist.Rebin(int(bins/rebin))
        # else:hist =hist.Rebin(len(rebin)-1,hist.GetName(),rebin)
        # else: raise Exception("rebin not possible")
        fm.WriteObject(histall,histall.GetName())
if __name__ == "__main__":
    # print("This is the __main__ part")
    if args.func=="remove_neg":remove_neg(args.year,args.version,args.region)
    if args.func=="reorder_BDT":reorder_BDT(args.year,args.version)
    
    if args.func=="merge_bin":merge_bin(args.year,args.version,args.rebin,args.region)#np.array( [0.0,  0.2, 0.4,  0.6,  0.8, 1.0]))
    if args.func=="merge_top":merge_top(args.year,args.version,args.region,args.rebin)
