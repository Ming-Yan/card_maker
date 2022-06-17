import ROOT 
chn='emu'

fsr = ROOT.TFile.Open('shape/templates_SR_%s_ll_mass_2017.root' %(chn))
fsr2 = ROOT.TFile.Open('shape/templates_SR2_%s_ll_mass_2017.root' %(chn))
histlist= ['hc','data_obs','st','vv','ttbar','vjets']
hist={}
hist2={}
hist_lm={}
hist2_lm={}
histcr={}



for h in histlist:  
    hist[h] = fsr.Get(h)
    hist2[h] = fsr2.Get(h)
    hist_lm[h] = ROOT.TH1F(h,h,13,0,78)
    hist2_lm[h] = ROOT.TH1F(h,h,13,0,78)
    histcr[h] = ROOT.TH1F(h,h,37,78,300)
    for b in range(50):
        if b < 13:
            hist_lm[h].SetBinContent(b+1,hist[h].GetBinContent(b+1))
            hist2_lm[h].SetBinContent(b+1,hist2[h].GetBinContent(b+1))
        else:histcr[h].SetBinContent(b+1-13,hist2[h].GetBinContent(b+1)+hist[h].GetBinContent(b+1))
    # hist_lm[h].Rebin(2)

fsr_lm = ROOT.TFile.Open('shape/templates_SR_LM_%s_ll_mass_2017.root' %(chn), "recreate")
fsr_lm.cd() 
for  h in histlist: hist_lm[h].Write()
fsr_lm.Close()
fsr2_lm = ROOT.TFile.Open('shape/templates_SR2_LM_%s_ll_mass_2017.root' %(chn), "recreate")
fsr2_lm.cd()    
for  h in histlist: hist2_lm[h].Write()
fsr2_lm.Close()
fscr_lm = ROOT.TFile.Open('shape/templates_HM_CR_%s_ll_mass_2017.root' %(chn), "recreate")
fscr_lm.cd()    
for  h in histlist:histcr[h].Write()
fscr_lm.Close()
    
