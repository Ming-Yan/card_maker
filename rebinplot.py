import ROOT as rt
import matplotlib.pyplot as plt
import numpy as np
import argparse
if __name__ == "__main__":

    proc = ['st','vv','vjets','ttbar','hc','data_obs']
    chs=['ee','mumu','emu']
    region=['SR2']
    sig_proc = 'hc'
    version=['v7t','v7_focal','v7_focal_dy']
    for ch in chs:
        for v in version:
            for r in region:
                f = rt.TFile('shape/templates_%s_%s_srbdt_2017_%s.root'%(r,ch,v))
                fo = rt.TFile('shape/templates_%s_%s_srbdt_2017_%s_rebin.root'%(r,ch,v),'recreate')
                hs =rt.THStack ("hs","hs")
                h=dict.fromkeys(proc)
                h2=dict.fromkeys(proc)
                for p in proc:
                    h[p] =f.Get(p)
                    # if p=='data_obs':print("h0",h['data_obs'].Integral(),r,v,ch)
                    if r == 'SR':
                        if 'focal' in  v :
                            if ch == 'emu': binning = [0.,0.014,0.028,0.042,0.07,0.098,0.126,0.154,0.182,0.21,0.28,0.35,0.42,0.7]
                            else:binning = [0.,0.012,0.024,0.048,0.072,0.096,0.12,0.18,0.204,0.24,0.3,0.36,0.48,0.6]
                        elif  'v7t' in  v:
                            if ch == 'emu' : binning = [0.,0.016,0.032,0.064,0.096,0.128,0.144,0.176,0.24,0.32,0.4,0.48,0.56,0.64,0.8]
                            else:binning = [0.,0.018,0.036,0.072,0.108,0.144,0.18,0.216,0.252,0.288,0.324,0.36,0.45,0.63,0.9]
                    elif r == 'SR2':
                        if 'focal' in  v : binning = [0.,0.014,0.028,0.042,0.056,0.07,0.084,0.098,0.112,0.126,0.14,0.154,0.168,0.182,0.196,0.21,0.245,0.28,0.35,0.42,0.56,0.7]
                        elif 'v7t' in  v:  binning = [0.,0.018,0.036,0.054,0.072,0.09,0.108,0.126,0.144,0.162,0.18,0.198,0.216,0.252,0.288,0.324,0.36,0.396,0.45,0.54,0.63,0.72,0.9]
                    # print(binning)
                    h2[p]=h[p].Rebin(len(binning)-1,"h2[%s]"%(p),np.array(binning))
                    # if p=='data_obs':
                    #     h2[p].SetBinContent(len(binning),0.)
                    #     h2[p].SetBinContent(len(binning)-1,0.)
                    #     h2[p].SetBinContent(len(binning)-2,0.)
                    #     h2[p].SetBinContent(len(binning)-3,0.)
                    #     h2[p].SetBinContent(len(binning)-4,0.)
                # print(h2['data_obs'].Integral(),r,v,ch)  
                c=rt.TCanvas("c","c")
                c.cd()
                l =rt.TLegend(.75,.5,.9,.9)
                # c.SetLogy
                c.SetTitle(r)
                h2['st'].SetLineWidth(0)
                h2['vv'].SetLineWidth(0)
                h2['ttbar'].SetLineWidth(0)
                h2['vjets'].SetLineWidth(0)
                
                h2['st'].SetFillColor(rt.TColor.GetColor("#d62728"))
                h2['vv'].SetFillColor(rt.TColor.GetColor("#1f77b4"))
                h2['vjets'].SetFillColor(rt.TColor.GetColor("#ff7f0e"))
                h2['ttbar'].SetFillColor(rt.TColor.GetColor("#2ca02c"))
                hs.Add(h2['st'])
                hs.Add(h2['vv'])
                hs.Add(h2['vjets'])
                hs.Add(h2['ttbar'])
                l.AddEntry(h2['st'],"ST","f")
                l.AddEntry(h2['vv'],"VV","f")
                l.AddEntry(h2['vjets'],"V+jets","f")
                l.AddEntry(h2['ttbar'],"t#bar{t}","f")
                l.AddEntry(h2['hc'],"signal#times10e4","l")
                l.AddEntry(h2['data_obs'],"data","ep")
                l.SetTextSize(0.05)
                hs.Draw("hist")
                h2['hc'].SetLineColor(rt.TColor.GetColor("#9467bd"))
                h2['hc'].SetLineWidth(2)
                # h2['hc'].Scale(10000)
                h2['data_obs'].SetLineColor(rt.kBlack)
                h2['data_obs'].SetMarkerColor(rt.kBlack)
                h2['data_obs'].SetMarkerStyle(20)
                h2['hc'].Draw("histsame")
                h2['data_obs'].Draw("epsame")
                hs.SetMinimum(0.1)
                c.SetLogy()
                hr = rt.TRatioPlot(hs,h2['data_obs'])
                
                # l.Draw()
                # hr.SetLineColor(rt.kBlack)
                # hr.SetMarkerColor(rt.kBlack)
                # hr.SetMarkerStyle(20)
                # hr.SetGraphDrawOpt
                hr.Draw("ep")
                hr.GetLowerRefYaxis().SetRangeUser(0.5,1.5)
                # hr.GetLowerRefYaxis().SetMaximum(1.5)
                pu=hr.GetUpperPad()
                pu.cd()
                
                h2['hc'].Draw("histsame")
                fo.cd()
                h2['hc'].Write()
                h2['data_obs'].Write()
                h2['st'].Write()
                h2['vv'].Write()
                h2['vjets'].Write()
                h2['ttbar'].Write()
                fo.Close()
                # pu.SetLogy()
                # pd=hr.GetLowerPad()
                # hr.GetLowerRefYaxis().SetNdivisions(505)
                
                
                # c.Print("rebinnedBDT_%s_%s_%s.png"%(r,ch,v))


                
                
    
