import ROOT

for r in range(1, 3):
    for ch in ["ee", "mumu", "emu"]:
        c = ROOT.TCanvas("c", "c", 800, 800)

        f = ROOT.TFile.Open("cards/moredy_2017/inputhc_%s_%d_13TeV.root " % (ch, r))
        histlist = ["hc", "data_obs", "st", "vv", "ttbar", "vjets", "higgs"]
        hist = {}
        for h in histlist:
            hist[h] = f.Get("hc_%s_%d_13TeV/%s" % (ch, r, h))
        hs = ROOT.THStack("hs", "")
        # print(type(hist['higgs']))
        hist["vjets"].SetLineColor(ROOT.TColor.GetColor("#854e99"))
        hist["ttbar"].SetLineColor(ROOT.TColor.GetColor("#73AF48"))
        hist["st"].SetLineColor(ROOT.TColor.GetColor("#38A6A5"))
        hist["vv"].SetLineColor(ROOT.TColor.GetColor("#CC503E"))
        hist["vjets"].SetFillColor(ROOT.TColor.GetColor("#854e99"))
        hist["ttbar"].SetFillColor(ROOT.TColor.GetColor("#73AF48"))
        hist["st"].SetFillColor(ROOT.TColor.GetColor("#38A6A5"))
        hist["vv"].SetFillColor(ROOT.TColor.GetColor("#CC503E"))
        hist["hc"].SetLineColor(ROOT.TColor.GetColor("#a6a1a1"))
        hist["higgs"].SetLineColor(ROOT.TColor.GetColor("#c2a482"))
        hist["higgs"].SetFillColor(ROOT.TColor.GetColor("#c2a482"))
        hist["higgs"].SetFillStyle(3)
        hist["hc"].SetLineWidth(2)
        hist["data_obs"].SetLineColor(1)
        hist["data_obs"].SetMarkerColor(1)
        hist["data_obs"].SetMarkerStyle(20)
        for nbin in range(
            hist["data_obs"].GetNbinsX() - 9, hist["data_obs"].GetNbinsX() + 1
        ):
            hist["data_obs"].SetBinContent(nbin, 0)
        hs.Add(hist["vjets"])
        hs.Add(hist["ttbar"])
        hs.Add(hist["st"])
        hs.Add(hist["vv"])
        hs.Add(hist["higgs"])

        hs.SetMaximum(25000)
        hs.SetMinimum(0.1)
        hs.Draw("hist")
        hist["data_obs"].Draw("epsame")
        l = ROOT.TLegend(0.5, 0.6, 0.9, 0.9)
        l.SetNColumns(2)
        l.AddEntry(hist["st"], "ST", "f")
        l.AddEntry(hist["vv"], "VV", "f")
        l.AddEntry(hist["vjets"], "V+jets", "f")
        l.AddEntry(hist["ttbar"], "t#bar{t}", "f")
        l.AddEntry(hist["higgs"], "higgs#times500", "f")
        l.AddEntry(hist["hc"], "signal#times50000", "l")
        l.AddEntry(hist["data_obs"], "data", "ep")
        l.SetTextSize(0.05)
        hr = ROOT.TRatioPlot(hs, hist["data_obs"])
        hr.Draw("ep")
        hr.GetLowerRefYaxis().SetRangeUser(0.5, 1.5)
        hr.GetLowerRefYaxis().SetNdivisions(505)
        pu = hr.GetUpperPad()
        pu.cd()
        pu.SetLogy()
        hist["hc"].Scale(50000)
        hist["higgs"].Scale(500)
        hist["hc"].Draw("histsame")
        hist["higgs"].Draw("histsame")

        l.Draw()
        c.Print("plot/%d_%s_dymore.pdf" % (r, ch))
