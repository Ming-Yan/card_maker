import CombineHarvester.CombineTools.ch as ch

### Uncertainties common to all Run-2 years
def AddCommonSystematics(cb,doshape=True,splitJEC=True):
  # Theory uncertainties:
    cb.cp().process(['hc']).AddSyst(cb,'CMS_hc','lnN',ch.SystMap()(1.25))
    cb.cp().process(['higgs']).AddSyst(cb,'CMS_higgs','lnN',ch.SystMap()(1.25))
    cb.cp().process(['higgs','hc']).AddSyst(cb,'CMS_Br_HWW_theo','lnN',ch.SystMap()(1.0099))
    cb.cp().process(['higgs','hc']).AddSyst(cb,'CMS_Br_HWW_mq','lnN',ch.SystMap()(1.0098))
    cb.cp().process(['higgs','hc']).AddSyst(cb,'CMS_Br_HWW_alphas','lnN',ch.SystMap()((0.9938,1.0064)))

  # background
    cb.cp().process(['higgs']).AddSyst(cb,'CMS_LHE_pdf_higgs', 'lnN', ch.SystMap()(1.018))
    cb.cp().process(['ttbar']).AddSyst(cb,'CMS_LHE_pdf_tt', 'lnN', ch.SystMap()(1.0265))
    cb.cp().process(['st']).AddSyst(cb,'CMS_LHE_pdf_st', 'lnN', ch.SystMap()(1.0288))
    cb.cp().process(['zjets']).AddSyst(cb,'CMS_LHE_pdf_zjets', 'lnN', ch.SystMap()(1.027))
    cb.cp().process(['vv']).AddSyst(cb,'CMS_LHE_pdf_vv', 'lnN', ch.SystMap()(1.0135))
    cb.cp().process(['st','vv']).AddSyst(cb, 'CMS_vvst', 'lnN', ch.SystMap()(1.15))
    cb.cp().process(["ttbar"]).AddSyst(cb, "CMS_ttbar","lnN", ch.SystMap()(1.005))
    cb.cp().process(["zjets"]).AddSyst(cb, "CMS_zjets", "lnN", ch.SystMap()(1.05))


  # Shape uncertainties
    if doshape:
      cb.cp().process(['hc']).AddSyst(cb,'CMS_FS_13TeV','shape',ch.SystMap()(1.0))

      for p in ['higgs','zjets','ttbar','st','vv']:
        cb.cp().process([p]).AddSyst(cb,'CMS_scalevar_3pt_%s_13TeV'%(p),'shape',ch.SystMap()(1.0))
        cb.cp().process([p]).AddSyst(cb,'CMS_UEPS_FSR_%s_13TeV'%(p),'shape',ch.SystMap()(1.0))
        cb.cp().process([p]).AddSyst(cb,'CMS_UEPS_ISR_%s_13TeV'%(p),'shape',ch.SystMap()(1.0))
      # cb.cp().AddSyst(cb,'CMS_PDFaS_weight','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_aS_weight_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_PDF_weight_13TeV','shape',ch.SystMap()(1.0))

      ## ttbar weight
      cb.cp().process(['ttbar']).AddSyst(cb,'CMS_ttbar_weight_13TeV','shape',ch.SystMap()(1.0))

      ## charm tagger SFs
      cb.cp().AddSyst(cb,'CMS_DeepJetC_PUWeight_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_DeepJetC_PSWeightISR_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_DeepJetC_PSWeightFSR_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_DeepJetC_jesTotal_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_DeepJetC_jer_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_DeepJetC_Interp_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_DeepJetC_Extrap_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_DeepJetC_LHEScaleWeight_muR_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_DeepJetC_LHEScaleWeight_muF_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_DeepJetC_XSec_BRUnc_WJets_c_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_DeepJetC_XSec_BRUnc_DYJets_b_13TeV','shape',ch.SystMap()(1.0))
      cb.cp().AddSyst(cb,'CMS_DeepJetC_XSec_BRUnc_DYJets_c_13TeV','shape',ch.SystMap()(1.0))
      if splitJEC:
        cb.cp().AddSyst(cb,'CMS_JES_FlavorQCD_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_RelativeBal_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_BBEC1_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_EC2_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_jes_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_Absolute_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_HF_13TeV','shape',ch.SystMap()(1.0))

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
    if doshape:cb.cp().AddSyst(cb,'CMS_puweight_2016_preVFP_13TeV','shape',ch.SystMap()(1.0))

  # Prefire efficiencies
    if doshape:cb.cp().AddSyst(cb,'CMS_L1prefireweight_13TeV','shape',ch.SystMap()(1.0))

  #lepton efficiencies

    if doshape:cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_ele_ID_2016_preVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_ele_Reco_2016_preVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_mu_ID_2016_preVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_mu_Iso_2016_preVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_mu_Reco_2016_preVFP_13TeV','shape',ch.SystMap()(1.0))

  # # Jet energy scale and resolution
    if doshape:
      if splitJEC:
        cb.cp().AddSyst(cb,'CMS_JES_Absolute_2016_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_HF_2016_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_BBEC1_2016_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_EC2_2016_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_RelativeSample_2016_13TeV','shape',ch.SystMap()(1.0))
      else:cb.cp().AddSyst(cb,'CMS_JES_2016_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().AddSyst(cb,'CMS_JER_2016_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().AddSyst(cb,'CMS_UES_2016_13TeV','shape',ch.SystMap()(1.0))


  # Tagger uncertainties / uncorrelate
    if doshape:cb.cp().AddSyst(cb,'CMS_DeepJetC_Stat_2016_preVFP_13TeV','shape',ch.SystMap()(1.0))


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
    if doshape:cb.cp().AddSyst(cb,'CMS_puweight_2016_postVFP_13TeV','shape',ch.SystMap()(1.0))

  # Prefire efficiencies
    if doshape:cb.cp().AddSyst(cb,'CMS_L1prefireweight_13TeV','shape',ch.SystMap()(1.0))

  #lepton efficiencies

    if doshape:cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_ele_ID_2016_postVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_ele_Reco_2016_postVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_mu_ID_2016_postVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_mu_Iso_2016_postVFP_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_mu_Reco_2016_postVFP_13TeV','shape',ch.SystMap()(1.0))

  # # Jet energy scale and resolution
    if doshape:
      if splitJEC:
        cb.cp().AddSyst(cb,'CMS_JES_Absolute_2016_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_HF_2016_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_BBEC1_2016_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_EC2_2016_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_RelativeSample_2016_13TeV','shape',ch.SystMap()(1.0))
      else:cb.cp().AddSyst(cb,'CMS_JES_2016_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().AddSyst(cb,'CMS_JER_2016_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().AddSyst(cb,'CMS_UES_2016_13TeV','shape',ch.SystMap()(1.0))


  # Tagger uncertainties / uncorrelate
    if doshape:cb.cp().AddSyst(cb,'CMS_DeepJetC_Stat_2016_postVFP_13TeV','shape',ch.SystMap()(1.0))

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
    if doshape:cb.cp().AddSyst(cb,'CMS_puweight_2017_13TeV','shape',ch.SystMap()(1.0))

  # Prefire efficiencies
    if doshape:cb.cp().AddSyst(cb,'CMS_L1prefireweight_13TeV','shape',ch.SystMap()(1.0))

  #lepton efficiencies

    if doshape:cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_ele_ID_2017_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_ele_Reco_2017_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_mu_ID_2017_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_mu_Iso_2017_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_mu_Reco_2017_13TeV','shape',ch.SystMap()(1.0))

  # Jet energy scale and resolution
    if doshape:
      if splitJEC:
        cb.cp().AddSyst(cb,'CMS_JES_Absolute_2017_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_HF_2017_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_BBEC1_2017_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_EC2_2017_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_RelativeSample_2017_13TeV','shape',ch.SystMap()(1.0))
      else:cb.cp().AddSyst(cb,'CMS_JES_2017_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().AddSyst(cb,'CMS_JER_2017_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().AddSyst(cb,'CMS_UES_2017_13TeV','shape',ch.SystMap()(1.0))


  # Tagger uncertainties / uncorrelate
    if doshape:cb.cp().AddSyst(cb,'CMS_DeepJetC_Stat_2017_13TeV','shape',ch.SystMap()(1.0))

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
    if doshape:cb.cp().AddSyst(cb,'CMS_puweight_2018_13TeV','shape',ch.SystMap()(1.0))



  # Lepton efficiencies

    if doshape:cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_ele_ID_2018_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_ele_Reco_2018_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_mu_ID_2018_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_mu_Iso_2018_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_mu_Reco_2018_13TeV','shape',ch.SystMap()(1.0))

  # Jet energy scale and resolution
    if doshape:
      if splitJEC:
        cb.cp().AddSyst(cb,'CMS_JES_Absolute_2018_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_HF_2018_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_BBEC1_2018_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_EC2_2018_13TeV','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_JES_RelativeSample_2018_13TeV','shape',ch.SystMap()(1.0))
      else:cb.cp().AddSyst(cb,'CMS_JES_2018_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().AddSyst(cb,'CMS_JER_2018_13TeV','shape',ch.SystMap()(1.0))
    if doshape:cb.cp().AddSyst(cb,'CMS_UES_2018_13TeV','shape',ch.SystMap()(1.0))


  # Tagger uncertainties / uncorrelate
    if doshape:cb.cp().AddSyst(cb,'CMS_DeepJetC_Stat_2018_13TeV','shape',ch.SystMap()(1.0))



syst_groups ={
  "theory_sig": "CMS_hc CMS_higgs CMS_Br_HWW_theo CMS_Br_HWW_mq CMS_Br_HWW_alphas",
  "theory_bkg":" CMS_vvst CMS_ttbar CMS_zjets CMS_LHE_pdf_higgs CMS_LHE_pdf_tt CMS_LHE_pdf_st CMS_LHE_pdf_zjets CMS_LHE_pdf_vv",
  "exp_lumi": " lumi_2017_13TeV lumi_13TeV_1718 lumi_13TeV_correlated",
  "theory_shape":" CMS_UEPS_FSR_higgs_13TeV CMS_UEPS_FSR_st_13TeV CMS_UEPS_FSR_ttbar_13TeV CMS_UEPS_FSR_vv_13TeV CMS_UEPS_ISR_higgs_13TeV CMS_UEPS_ISR_st_13TeV CMS_UEPS_ISR_ttbar_13TeV CMS_UEPS_ISR_vv_13TeV CMS_aS_weight_13TeV CMS_scalevar_3pt_higgs_13TeV CMS_scalevar_3pt_st_13TeV CMS_scalevar_3pt_ttbar_13TeV CMS_scalevar_3pt_vv_13TeV CMS_PDF_weight_13TeV CMS_UEPS_FSR_zjets_13TeV CMS_UEPS_ISR_zjets_13TeV CMS_scalevar_3pt_zjets_13TeV",
  "exp_ctag":" CMS_DeepJetC_Extrap_13TeV CMS_DeepJetC_Interp_13TeV CMS_DeepJetC_LHEScaleWeight_muF_13TeV CMS_DeepJetC_LHEScaleWeight_muR_13TeV CMS_DeepJetC_PSWeightFSR_13TeV CMS_DeepJetC_PSWeightISR_13TeV CMS_DeepJetC_PUWeight_13TeV CMS_DeepJetC_Stat_2017_13TeV CMS_DeepJetC_XSec_BRUnc_DYJets_b_13TeV CMS_DeepJetC_XSec_BRUnc_DYJets_c_13TeV CMS_DeepJetC_XSec_BRUnc_WJets_c_13TeV CMS_DeepJetC_jer_13TeV CMS_DeepJetC_jesTotal_13TeV",
  "exp_JERC":" CMS_JER_2017_13TeV CMS_JES_2017_13TeV CMS_UES_2017_13TeV",
  "exp_split_JERC": " CMS_JES_HF_2017_13TeV CMS_JES_Absolute_2017_13TeV CMS_JES_BBEC1_2017_13TeV CMS_JES_EC2_2017_13TeV CMS_JES_RelativeSample_2017_13TeV CMS_JES_FlavorQCD_13TeV CMS_JES_RelativeBal_13TeV CMS_JES_BBEC1_13TeV CMS_JES_EC2_13TeV CMS_JES_jes_13TeV CMS_JES_Absolute_13TeV CMS_JES_HF_13TeV",
  "exp_other_weights":" CMS_L1prefireweight_13TeV CMS_puweight_2017_13TeV CMS_ttbar_weight_13TeV",
  "exp_lepID":" CMS_ele_ID_2017_13TeV CMS_ele_Reco_2017_13TeV CMS_mu_ID_2017_13TeV CMS_mu_Iso_2017_13TeV CMS_mu_Reco_2017_13TeV",
  "old_unc":"CMS_hc CMS_higgs CMS_Br_HWW_theo CMS_Br_HWW_mq CMS_Br_HWW_alphas CMS_vvst CMS_ttbar CMS_zjets lumi_2017_13TeV lumi_13TeV_1718 lumi_13TeV_correlated CMS_SF_ttbar_emu_2017_13TeV"
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

