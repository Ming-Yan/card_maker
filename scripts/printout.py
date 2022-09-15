import uproot
if __name__ == "__main__":
    #higgsCombineall_syst_2017_all_mu0_UES.FitDiagnostics.mH125.root
    syst= ["old","higgs","BrHWW","scalevar","UEPS","aSPDF","puwei","L1wei","lepSF","JES","JER","UES","None"]
    #flav = ["all","ee","mumu","emu"]
    flav = ["emu"]
    for f in flav : 
        file_old = uproot.open("higgsCombinecorrPU_2017_%s_old.AsymptoticLimits.mH125.root" %(f))
        for s in syst:
            #files = uproot.open("output/corrsyst_2017/higgsCombinecorrsyst_2017_%s_%s.AsymptoticLimits.mH125.root" %(f,s))
            files = uproot.open("higgsCombinecorrPU_2017_%s_%s.AsymptoticLimits.mH125.root" %(f,s))
            
            #files = uproot.open("higgsCombinecorrsyst_2017_%s_%s.AsymptoticLimits.mH125.root" %(f,s))
            #print(f,s,files["limit"]["limit"].array()[2])
            print(f'{files["limit"]["limit"].array()[2]}')
        
