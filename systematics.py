import CombineHarvester.CombineTools.ch as ch

### Uncertainties common to all Run-2 years
def AddCommonSystematics(cb,doshape=True,splitJEC=True):
  # Theory uncertainties:
    ##https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNHLHE2019
    cb.cp().process(['hc']).AddSyst(cb,'QCDscale_hc', 'lnN', ch.SystMap()(1.15))
    cb.cp().process(['hc']).AddSyst(cb,'pdf_Higgs_hc', 'lnN', ch.SystMap()(1.06))
    cb.cp().process(['hc']).AddSyst(cb,'FS_hc', 'lnN', ch.SystMap()(1.30))
    #cb.cp().process(['hb']).AddSyst(cb,'QCDscale_hb', 'lnN', ch.SystMap()(1.15))
    #cb.cp().process(['hb']).AddSyst(cb,'pdf_Higgs_hb', 'lnN', ch.SystMap()(1.06))
    #cb.cp().process(['hb']).AddSyst(cb,'FS_hb', 'lnN', ch.SystMap()(1.30))
    cb.cp().process(['higgs']).AddSyst(cb,'theo_higgs','lnN',ch.SystMap()(1.0992))
    cb.cp().process(['higgs','hc']).AddSyst(cb,'BR_HWW_theo','lnN',ch.SystMap()(1.0099)) 
    cb.cp().process(['higgs','hc']).AddSyst(cb,'BR_HWW_mq','lnN',ch.SystMap()(1.0098))
    cb.cp().process(['higgs','hc']).AddSyst(cb,'BR_HWW_alphas','lnN',ch.SystMap()((0.9938,1.0064)))
    cb.cp().process(['ggH_hww','ggH_htautau']).AddSyst(cb,'scale_ggH','lnN',ch.SystMap()((1.046,0.9351)))
    cb.cp().process(['ggH_hww','ggH_htautau']).AddSyst(cb,'PDFalphaS_ggH','lnN',ch.SystMap()(1.031))
    cb.cp().process(['qqH_hww','ggH_htautau']).AddSyst(cb,'scale_qqH','lnN',ch.SystMap()((1.004,0.997)))
    cb.cp().process(['qqH_hww','ggH_htautau']).AddSyst(cb,'PDFalphaS_qqH','lnN',ch.SystMap()(1.021))
    cb.cp().process(['VH_hww','VH_htautau']).AddSyst(cb,'scale_VH','lnN',ch.SystMap()(1.0051))
    cb.cp().process(['VH_hww','VH_htautau']).AddSyst(cb,'PDFalphaS_VH','lnN',ch.SystMap()(1.0135))
    cb.cp().process(['ttH_hww','ttH_htautau']).AddSyst(cb,'scale_ttH','lnN',ch.SystMap()((1.058,0.908)))
    cb.cp().process(['ttH_hww','ttH_htautau']).AddSyst(cb,'PDFalphaS_ttH','lnN',ch.SystMap()(1.036))
    cb.cp().process(['ggH_hww','ggH_htautau']).AddSyst(cb,'flavor_composition_ggH','lnN',ch.SystMap()(1.10))
   
    # cb.cp().process(['ggH_hww','qqH_hww','VH_hww','ggH_htautau','qqH_htautau']).AddSyst(cb,'theo_higgs','lnN',ch.SystMap()(1.25))
    cb.cp().process(['ggH_hww','qqH_hww','VH_hww','ttH_hww','hc','hb']).AddSyst(cb,'BR_HWW_theo','lnN',ch.SystMap()(1.0099))
    cb.cp().process(['ggH_hww','qqH_hww','VH_hww','ttH_hww','hc','hb']).AddSyst(cb,'BR_HWW_mq','lnN',ch.SystMap()(1.0098))
    cb.cp().process(['ggH_hww','qqH_hww','VH_hww','ttH_hww','hc','hb']).AddSyst(cb,'BR_HWW_alphas','lnN',ch.SystMap()((1.0064,0.9947)))
    cb.cp().process(['ggH_htautau','qqH_htautau','VH_htautau','ttH_htautau']).AddSyst(cb,'BR_Htautau_theo','lnN',ch.SystMap()((1.0117,0.9884)))
    cb.cp().process(['ggH_htautau','qqH_htautau','VH_htautau','ttH_htautau']).AddSyst(cb,'BR_Htautau_mq','lnN',ch.SystMap()(1.0098))
    cb.cp().process(['ggH_htautau','qqH_htautau','VH_htautau','ttH_htautau']).AddSyst(cb,'BR_Htautau_alphas','lnN',ch.SystMap()((1.0062,0.9940)))
    # cb.cp().process(['ggH_hzz','qqH_hzz']).AddSyst(cb,'CMS_Br_HZZ_theo','lnN',ch.SystMap()((1.0173,0.9828)))
    # cb.cp().process(['ggH_hzz','qqH_hzz']).AddSyst(cb,'CMS_Br_HZZ_mq','lnN',ch.SystMap()((1.0093,0.9901)))
    # cb.cp().process(['ggH_hzz','qqH_hzz']).AddSyst(cb,'CMS_Br_HZZ_aS','lnN',ch.SystMap()((1.0061,0.9938)))
    
  # background
    # ttbar : https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO#Top_quark_pair_cross_sections_at
    #cb.cp().process(['ttbar']).AddSyst(cb,'CMS_scale_ttbar', 'lnN', ch.SystMap()((0.9754,1.0360)))
    #cb.cp().process(['ttbar']).AddSyst(cb,'CMS_pdf_alphaS_ttbar', 'lnN', ch.SystMap()(1.0251))
    #cb.cp().process(['ttbar']).AddSyst(cb,'CMS_massunc_ttbar', 'lnN', ch.SystMap()((0.9873,1.0167)))
    #cb.cp().process(['ttbar']).AddSyst(cb,'pdf_ttbar', 'lnN', ch.SystMap()(1.0265))
    # cb.cp().process(['ttbar']).AddSyst(cb,'scale_ttbar', 'lnN', ch.SystMap()(1.12))
    # single top https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef#Predictions_for_top_quark_produc
    cb.cp().process(['st']).AddSyst(cb,'pdf_st', 'lnN', ch.SystMap()(1.0288))
    #cb.cp().process(['st']).AddSyst(cb,'scale_st', 'lnN', ch.SystMap()(1.0288))
    cb.cp().process(['zjets']).AddSyst(cb,'pdf_zjets', 'lnN', ch.SystMap()(1.027))
    cb.cp().process(['vv']).AddSyst(cb,'pdf_vv', 'lnN', ch.SystMap()(1.0135))
    
    cb.cp().process(['vv']).AddSyst(cb, 'theo_vv', 'lnN', ch.SystMap()(1.037))
    cb.cp().process(['st']).AddSyst(cb, 'theo_st', 'lnN', ch.SystMap()(1.017))
    #cb.cp().process(['ttbar']).AddSyst(cb, 'theo_ttbar', 'lnN', ch.SystMap()(1.02))
    cb.cp().process(["zjets"]).AddSyst(cb, "theo_zjets", "lnN", ch.SystMap()(1.05))

    #cb.cp().process([p]).AddSyst(cb,'CMS_scale_%s_13TeV'%(p),'shape',ch.SystMap()(1.0))
  # Shape uncertainties
    if doshape:
      # cb.cp().process(['hc']).AddSyst(cb,'CMS_FS_13TeV','shape',ch.SystMap()(1.0))

      for p in ['ggH_hww','qqH_hww','VH_hww','ttH_hww','ggH_htautau','qqH_htautau','VH_htautau','ttH_htautau','zjets','st','vv','ttbar']:

        cb.cp().process([p]).AddSyst(cb,'UEPS_FSR_%s_13TeV'%(p),'shape',ch.SystMap()(1.0))
        cb.cp().process([p]).AddSyst(cb,'UEPS_ISR_%s_13TeV'%(p),'shape',ch.SystMap()(1.0))
        cb.cp().process([p]).AddSyst(cb,'scale_muRmuF_%s_13TeV'%(p),'shape',ch.SystMap()(1.0))
      # cb.cp().AddSyst(cb,'CMS_PDFaS_weight','shape',ch.SystMap()(1.0))
      # cb.cp().AddSyst(cb,'CMS_aS_weight_13TeV','shape',ch.SystMap()(1.0))
      # cb.cp().AddSyst(cb,'CMS_PDF_weight_13TeV','shape',ch.SystMap()(1.0))

      ## ttbar weight
      cb.cp().process(['ttbar']).AddSyst(cb,'pt_weight','shape',ch.SystMap()(1.0))

      ## charm tagger SFs
      #cb.cp().AddSyst(cb,'CMS_eff_c_DeepJetC_PUWeight_13TeV','shape',ch.SystMap()(1.0))
      #cb.cp().AddSyst(cb,'CMS_eff_c_DeepJetC_PSWeightISR_13TeV','shape',ch.SystMap()(1.0))
      #cb.cp().AddSyst(cb,'CMS_eff_c_DeepJetC_PSWeightFSR_13TeV','shape',ch.SystMap()(1.0))
      #cb.cp().AddSyst(cb,'CMS_eff_c_DeepJetC_jesTotal_13TeV','shape',ch.SystMap()(1.0))
      #cb.cp().AddSyst(cb,'CMS_eff_c_DeepJetC_jer_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_eff_c_DeepJetC_Interp_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_eff_c_DeepJetC_Extrap_13TeV','shape',ch.SystMap()(1.0))
      #cb.cp().AddSyst(cb,'CMS_eff_c_DeepJetC_LHEScaleWeight_muR_13TeV','shape',ch.SystMap()(1.0))
      #cb.cp().AddSyst(cb,'CMS_eff_c_DeepJetC_LHEScaleWeight_muF_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_eff_c_DeepJetC_XSec_BRUnc_WJets_c_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_eff_c_DeepJetC_XSec_BRUnc_DYJets_b_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_eff_c_DeepJetC_XSec_BRUnc_DYJets_c_13TeV','shape',ch.SystMap()(1.0))
      if splitJEC:
        cb.cp().AddSyst(cb,'CMS_scale_j_FlavorQCD_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_RelativeBal_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_BBEC1_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_EC2_13TeV','shape',ch.SystMap()(1.0))
        # cb.cp().AddSyst(cb,'CMS_scale_j_scale_j_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_Absolute_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_HF_13TeV','shape',ch.SystMap()(1.0))

# 2016 preVFP
def AddSystematics2016_preVFP(cb, chn, doshape=True,splitJEC=True):
    if chn!='emu' : chns = 'll'
    else : chns = chn
    cb.cp().channel([chn]).process(["ttbar"]).AddSyst(
            cb, "CMS_SF_ttbar_%s_2016_13TeV" % (chns), "rateParam", ch.SystMap()(1.0)
        )
    cb.GetParameter("CMS_SF_ttbar_%s_2016_13TeV" % (chns)).set_range(0.0, 5.0)
    if chn != "emu":
        cb.cp().channel([chn]).process(["vjets"]).AddSyst(
            cb, "CMS_SF_vjets_%s_2016_13TeV" % (chns), "rateParam", ch.SystMap()(1.0)
        )
        cb.GetParameter("CMS_SF_vjets_%s_2016_13TeV" % (chns)).set_range(0.0, 5.0)



  # EXPERIMENTAL UNCERTAINTIES
    cb.cp().AddSyst(cb,'lumi_2016_13TeV','lnN', ch.SystMap()(1.010))
    cb.cp().AddSyst(cb,'lumi_13TeV_correlated','lnN', ch.SystMap()(1.006))
    if doshape:
      cb.cp().AddSyst(cb,'CMS_pileup_2016_preVFP_13TeV','shape',ch.SystMap()(1.0))

  # Prefire efficiencies
    if doshape:cb.cp().AddSyst(cb,'CMS_L1prefireweight_13TeV','shape',ch.SystMap()(1.0))

  #lepton efficiencies

    if doshape:cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_eff_e_ID_2016_preVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_eff_e_Reco_2016_preVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_eff_m_ID_2016_preVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_eff_m_Iso_2016_preVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_eff_m_Reco_2016_preVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_eff_HLT_2016_preVFP_13TeV','shape',ch.SystMap()(1.0))

  # # Jet energy scale and resolution
    if doshape:
      if splitJEC:
        cb.cp().AddSyst(cb,'CMS_scale_j_Absolute_2016_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_HF_2016_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_BBEC1_2016_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_EC2_2016_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_RelativeSample_2016_13TeV','shape',ch.SystMap()(1.0))
      else:cb.cp().AddSyst(cb,'CMS_scale_j_2016_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().AddSyst(cb,'CMS_res_j_2016_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().AddSyst(cb,'CMS_scale_met_2016_13TeV','shape',ch.SystMap()(1.0))


  # Tagger uncertainties / uncorrelate
    if doshape:cb.cp().AddSyst(cb,'CMS_eff_c_DeepJetC_Stat_2016_preVFP_13TeV','shape',ch.SystMap()(1.0))


def AddSystematics2016_postVFP(cb, chn, doshape=True,splitJEC=True):
    if chn!='emu' : chns = 'll'
    else : chns = chn
    cb.cp().channel([chn]).process(["ttbar"]).AddSyst(
            cb, "CMS_SF_ttbar_%s_2016_13TeV" % (chns), "rateParam", ch.SystMap()(1.0)
        )
    cb.GetParameter("CMS_SF_ttbar_%s_2016_13TeV" % (chns)).set_range(0.0, 5.0)
    if chn != "emu":
        cb.cp().channel([chn]).process(["vjets"]).AddSyst(
            cb, "CMS_SF_vjets_%s_2016_13TeV" % (chns), "rateParam", ch.SystMap()(1.0)
        )
        cb.GetParameter("CMS_SF_vjets_%s_2016_13TeV" % (chns)).set_range(0.0, 5.0)



  # EXPERIMENTAL UNCERTAINTIES
    cb.cp().AddSyst(cb,'lumi_2016_13TeV','lnN', ch.SystMap()(1.010))
    cb.cp().AddSyst(cb,'lumi_13TeV_correlated','lnN', ch.SystMap()(1.006))
    if doshape:cb.cp().AddSyst(cb,'CMS_pileup_2016_postVFP_13TeV','shape',ch.SystMap()(1.0))

  # Prefire efficiencies
    if doshape:cb.cp().AddSyst(cb,'CMS_L1prefireweight_13TeV','shape',ch.SystMap()(1.0))

  #lepton efficiencies

    if doshape:cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_eff_e_ID_2016_postVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_eff_e_Reco_2016_postVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_eff_m_ID_2016_postVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_eff_m_Iso_2016_postVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_eff_m_Reco_2016_postVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_eff_HLT_2016_postVFP_13TeV','shape',ch.SystMap()(1.0))
    # cb.cp().AddSyst(cb,'CMS_eff_HLT_syst_2016_postVFP_13TeV','lnN', ch.SystMap()(1.03))

  # # Jet energy scale and resolution
    if doshape:
      if splitJEC:
        cb.cp().AddSyst(cb,'CMS_scale_j_Absolute_2016_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_HF_2016_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_BBEC1_2016_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_EC2_2016_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_RelativeSample_2016_13TeV','shape',ch.SystMap()(1.0))
      else:cb.cp().AddSyst(cb,'CMS_scale_j_2016_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().AddSyst(cb,'CMS_res_j_2016_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().AddSyst(cb,'CMS_scale_met_2016_13TeV','shape',ch.SystMap()(1.0))
    


  # Tagger uncertainties / uncorrelate
    if doshape:cb.cp().AddSyst(cb,'CMS_eff_c_DeepJetC_Stat_2016_postVFP_13TeV','shape',ch.SystMap()(1.0))

## 2017
def AddSystematics2017(cb, chn, doshape=True,splitJEC=True):
    if chn!='emu' : chns = 'll'
    else : chns = chn
    cb.cp().channel([chn]).process(["ttbar"]).AddSyst(
            cb, "CMS_SF_ttbar_%s_2017_13TeV" % (chns), "rateParam", ch.SystMap()(1.0)
        )
    cb.GetParameter("CMS_SF_ttbar_%s_2017_13TeV" % (chns)).set_range(0.0, 5.0)
    if chn != "emu":
        cb.cp().channel([chn]).process(["vjets"]).AddSyst(
            cb, "CMS_SF_vjets_%s_2017_13TeV" % (chns), "rateParam", ch.SystMap()(1.0)
        )
        cb.GetParameter("CMS_SF_vjets_%s_2017_13TeV" % (chns)).set_range(0.0, 5.0)



  # EXPERIMENTAL UNCERTAINTIES
    cb.cp().AddSyst(cb,'lumi_2017_13TeV','lnN', ch.SystMap()(1.020))
    cb.cp().AddSyst(cb,'lumi_13TeV_1718','lnN', ch.SystMap()(1.006))
    cb.cp().AddSyst(cb,'lumi_13TeV_correlated','lnN', ch.SystMap()(1.009))
    if doshape:cb.cp().AddSyst(cb,'CMS_pileup_2017_13TeV','shape',ch.SystMap()(1.0))

  # Prefire efficiencies
    if doshape:cb.cp().AddSyst(cb,'CMS_L1prefireweight_13TeV','shape',ch.SystMap()(1.0))

  #lepton efficiencies

    if doshape:cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_eff_e_ID_2017_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_eff_e_Reco_2017_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_eff_m_ID_2017_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_eff_m_Iso_2017_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_eff_m_Reco_2017_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_eff_HLT_2017_13TeV','shape',ch.SystMap()(1.0))
    # cb.cp().AddSyst(cb,'CMS_eff_HLT_syst_2017_13TeV','lnN', ch.SystMap()(1.03))

  # Jet energy scale and resolution
    if doshape:
      if splitJEC:
        cb.cp().AddSyst(cb,'CMS_scale_j_Absolute_2017_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_HF_2017_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_BBEC1_2017_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_EC2_2017_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_RelativeSample_2017_13TeV','shape',ch.SystMap()(1.0))
      else:cb.cp().AddSyst(cb,'CMS_scale_j_2017_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().AddSyst(cb,'CMS_res_j_2017_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().AddSyst(cb,'CMS_scale_met_2017_13TeV','shape',ch.SystMap()(1.0))


  # Tagger uncertainties / uncorrelate
    if doshape:cb.cp().AddSyst(cb,'CMS_eff_c_DeepJetC_Stat_2017_13TeV','shape',ch.SystMap()(1.0))

def AddSystematics2018(cb, chn, doshape=True,splitJEC=True):
    if chn!='emu' : chns = 'll'
    else : chns = chn
    cb.cp().channel([chn]).process(["ttbar"]).AddSyst(
            cb, "CMS_SF_ttbar_%s_2018_13TeV" % (chns), "rateParam", ch.SystMap()(1.0)
        )
    cb.GetParameter("CMS_SF_ttbar_%s_2018_13TeV" % (chns)).set_range(0.0, 5.0)
    if chn != "emu":
        cb.cp().channel([chn]).process(["vjets"]).AddSyst(
            cb, "CMS_SF_vjets_%s_2018_13TeV" % (chns), "rateParam", ch.SystMap()(1.0)
        )
        cb.GetParameter("CMS_SF_vjets_%s_2018_13TeV" % (chns)).set_range(0.0, 5.0)



  ## EXPERIMENTAL UNCERTAINTIES
    cb.cp().AddSyst(cb,'lumi_2018_13TeV','lnN', ch.SystMap()(1.015))
    cb.cp().AddSyst(cb,'lumi_13TeV_1718','lnN', ch.SystMap()(1.002))
    cb.cp().AddSyst(cb,'lumi_13TeV_correlated','lnN', ch.SystMap()(1.020))
    if doshape:cb.cp().AddSyst(cb,'CMS_pileup_2018_13TeV','shape',ch.SystMap()(1.0))



  # Lepton efficiencies

    if doshape:cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_eff_e_ID_2018_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_eff_e_Reco_2018_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_eff_m_ID_2018_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_eff_m_Iso_2018_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_eff_m_Reco_2018_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_eff_HLT_2018_13TeV','shape',ch.SystMap()(1.0))
    # cb.cp().AddSyst(cb,'CMS_eff_HLT_syst_2018_13TeV','lnN', ch.SystMap()(1.03))

  # Jet energy scale and resolution
    if doshape:
      if splitJEC:
        cb.cp().AddSyst(cb,'CMS_scale_j_Absolute_2018_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_HF_2018_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_BBEC1_2018_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_EC2_2018_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_RelativeSample_2018_13TeV','shape',ch.SystMap()(1.0))
      else:cb.cp().AddSyst(cb,'CMS_scale_j_2018_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().AddSyst(cb,'CMS_res_j_2018_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().AddSyst(cb,'CMS_scale_met_2018_13TeV','shape',ch.SystMap()(1.0))


  # Tagger uncertainties / uncorrelate
    if doshape:cb.cp().AddSyst(cb,'CMS_eff_c_DeepJetC_Stat_2018_13TeV','shape',ch.SystMap()(1.0))



syst_groups ={
  "theory_sig":" pdf_Higgs_hc QCDscale_hc FS_hc",
    "theory_bkg":" theo_vv theo_st theo_zjets pdf_Higgs_hc pdf_st pdf_zjets pdf_vv",
  "exp_lumi": " lumi_2017_13TeV lumi_13TeV_1718 lumi_13TeV_correlated",
  # "theory_shape":" UEPS_FSR_higgs_13TeV UEPS_FSR_st_13TeV UEPS_FSR_ttbar_13TeV UEPS_FSR_vv_13TeV UEPS_ISR_higgs_13TeV UEPS_ISR_st_13TeV UEPS_ISR_ttbar_13TeV UEPS_ISR_vv_13TeV UEPS_FSR_zjets_13TeV UEPS_FSR_zjets_13TeV",
    #"exp_ctag":" CMS_eff_c_DeepJetC_Extrap_13TeV CMS_eff_c_DeepJetC_Interp_13TeV CMS_eff_c_DeepJetC_LHEScaleWeight_muF_13TeV CMS_eff_c_DeepJetC_LHEScaleWeight_muR_13TeV CMS_eff_c_DeepJetC_PSWeightFSR_13TeV CMS_eff_c_DeepJetC_PSWeightISR_13TeV CMS_eff_c_DeepJetC_PUWeight_13TeV CMS_eff_c_DeepJetC_Stat_2017_13TeV CMS_eff_c_DeepJetC_XSec_BRUnc_DYJets_b_13TeV CMS_eff_c_DeepJetC_XSec_BRUnc_DYJets_c_13TeV CMS_eff_c_DeepJetC_XSec_BRUnc_WJets_c_13TeV CMS_eff_c_DeepJetC_jer_13TeV CMS_eff_c_DeepJetC_jesTotal_13TeV",
   "exp_ctag":" CMS_eff_c_DeepJetC_Extrap_13TeV CMS_eff_c_DeepJetC_Interp_13TeV CMS_eff_c_DeepJetC_Stat_2017_13TeV CMS_eff_c_DeepJetC_XSec_BRUnc_DYJets_b_13TeV CMS_eff_c_DeepJetC_XSec_BRUnc_DYJets_c_13TeV CMS_eff_c_DeepJetC_XSec_BRUnc_WJets_c_13TeV",
  "exp_JERC":" CMS_res_j_2017_13TeV CMS_scale_j_2017_13TeV CMS_scale_met_2017_13TeV",
  "exp_split_JERC": " CMS_scale_j_HF_2017_13TeV CMS_scale_j_Absolute_2017_13TeV CMS_scale_j_BBEC1_2017_13TeV CMS_scale_j_EC2_2017_13TeV CMS_scale_j_RelativeSample_2017_13TeV CMS_scale_j_FlavorQCD_13TeV CMS_scale_j_RelativeBal_13TeV CMS_scale_j_BBEC1_13TeV CMS_scale_j_EC2_13TeV  CMS_scale_j_Absolute_13TeV CMS_scale_j_HF_13TeV",
  "exp_other_weights":" CMS_L1prefireweight_13TeV CMS_pileup_2017_13TeV pt_weight",
  "exp_lepID":" CMS_eff_e_ID_2017_13TeV CMS_eff_e_Reco_2017_13TeV CMS_eff_m_ID_2017_13TeV CMS_eff_m_Iso_2017_13TeV CMS_eff_m_Reco_2017_13TeV",
  # "old_unc":"CMS_hc theo_higgs theo_vvst theo_ttbar theo_zjets lumi_2017_13TeV lumi_13TeV_1718 lumi_13TeV_correlated CMS_SF_ttbar_emu_2017_13TeV"
}

def group_nuisances(cb,year="2017",scheme="version",splitJEC=True):
  theo_group,exp_group=[],[]
  for group in syst_groups.keys():
    
    if splitJEC and group=="exp_JERC":continue
    elif not splitJEC and group=="exp_split_JERC":continue
    if scheme=="sys_combine":
        if "theory" in group:theo_group=theo_group+syst_groups[group]
        if "exp" in group:
          if "2016" in year and ("JERC" in group or "lumi" == group or "old_unc" == group):exp_group=exp_group+syst_groups[group].replace("2017","2016").replace(" lumi_13TeV_1718","")
          elif "2018" == year:exp_group=exp_group+syst_groups[group].replace("CMS_L1prefireweight_13TeV ","")
          else:exp_group=exp_group+syst_groups[group].replace("2017",year)
    else:
      if scheme!="version" and "old_unc"==group:continue
      if "2016" in year and ("JERC" in group or "lumi" in group or "old_unc" == group):cb.AddDatacardLineAtEnd("%s group = %s" %(group, syst_groups[group].replace("2017","2016").replace(" lumi_13TeV_1718","")))
      elif "2018" == year:cb.AddDatacardLineAtEnd("%s group = %s" %(group, syst_groups[group].replace("2017",year).replace("CMS_L1prefireweight_13TeV ","")))
      else:cb.AddDatacardLineAtEnd("%s group = %s" %(group, syst_groups[group].replace("2017",year)))

  if scheme=="sys_combine":
    cb.AddDatacardLineAtEnd("theo group = %s" %(theo_group))
    cb.AddDatacardLineAtEnd("exp group = %s" %(exp_group))

