import CombineHarvester.CombineTools.ch as ch

def AddCommonSystematics(cb):
  
########################################################################################################################################
### Uncertainties common to all Run-2 years
########################################################################################################################################
  
  # Theory uncertainties: 
    cb.cp().process(['hc']).AddSyst(cb,'CMS_hc','lnN',ch.SystMap()(1.25))
    cb.cp().process(['higgs']).AddSyst(cb,'CMS_higgs','lnN',ch.SystMap()(1.25))
    cb.cp().process(['higgs','hc']).AddSyst(cb,'CMS_Br_HWW_theo','lnN',ch.SystMap()(1.0099))
    cb.cp().process(['higgs','hc']).AddSyst(cb,'CMS_Br_HWW_mq','lnN',ch.SystMap()(1.0098))
    cb.cp().process(['higgs','hc']).AddSyst(cb,'CMS_Br_HWW_alphas','lnN',ch.SystMap()((0.9938,1.0064)))

    ### background
    cb.cp().process(["st", "vv"]).AddSyst(cb, "CMS_vvst", "lnN", ch.SystMap()(1.15))
    cb.cp().process(["ttbar"]).AddSyst(cb, "CMS_ttbar", "lnN", ch.SystMap()(1.005))
    cb.cp().process(["vjets"]).AddSyst(cb, "CMS_vjet", "lnN", ch.SystMap()(1.05))

    # Measured cross section uncertainties because we don't have SF
    # cb.cp().process(['VVother','VZcc']).AddSyst(cb,'CMS_vhcc_VV', 'lnN', ch.SystMap()(1.05)) 
    # cb.cp().process(['s_Top']).AddSyst(cb,'CMS_vhcc_ST', 'lnN', ch.SystMap()(1.15)) 

    # Shape uncertainties
    cb.cp().AddSyst(cb,'CMS_scalevar_3pt','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_UEPS_FSR','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_UEPS_ISR','shape',ch.SystMap()(1.0))
    # cb.cp().AddSyst(cb,'CMS_PDFaS_weight','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_aS_weight','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_PDF_weight','shape',ch.SystMap()(1.0))
   
    

########################################################################################################################################
### Uncertainties for 2016
########################################################################################################################################
# def AddSystematics2016(cb, chn,splitJEC=False):
########################################################################################################################################
### Uncertainties for 2017
########################################################################################################################################
def AddSystematics2017(cb, chn,splitJEC=False):

####################### SCALE FACTORS RATEPARAM
    if chn!='emu' : chns = 'll'
    else : chns = chn
    cb.cp().channel([chn]).process(["ttbar"]).AddSyst(
            cb, "CMS_SF_tt_%s_13TeV_2017" % (chns), "rateParam", ch.SystMap()(1.0)
        )
    cb.GetParameter("CMS_SF_tt_%s_13TeV_2017" % (chns)).set_range(0.0, 5.0)
    if chn != "emu":
        cb.cp().channel([chn]).process(["vjets"]).AddSyst(
            cb, "CMS_SF_vjets_%s_13TeV_2017" % (chns), "rateParam", ch.SystMap()(1.0)
        )
        cb.GetParameter("CMS_SF_vjets_%s_13TeV_2017" % (chns)).set_range(0.0, 5.0)


  
  ####################### EXPERIMENTAL UNCERTAINTIES
    cb.cp().AddSyst(cb,'lumi_13TeV_2017','lnN', ch.SystMap()(1.020))
    cb.cp().AddSyst(cb,'lumi_13TeV_1718','lnN', ch.SystMap()(1.006))
    cb.cp().AddSyst(cb,'lumi_13TeV_correlated','lnN', ch.SystMap()(1.009))  
    cb.cp().AddSyst(cb,'CMS_puweight_13TeV_2017','shape',ch.SystMap()(1.0))

  ####################### Prefire efficiencies
    cb.cp().AddSyst(cb,'CMS_L1prefireweight','shape',ch.SystMap()(1.0))

  #######################lepton efficiencies

    cb.cp().channel(['ee','emu']).AddSyst(cb,'CMS_eleSFs_13TeV_2017','shape',ch.SystMap()(1.0))
    cb.cp().channel(['mumu','emu']).AddSyst(cb,'CMS_muSFs_13TeV_2017','shape',ch.SystMap()(1.0))

  # ####################### Jet energy scale and resolution
    cb.cp().AddSyst(cb,'CMS_JES_13TeV_2017','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_JER_13TeV_2017','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_UES_13TeV_2017','shape',ch.SystMap()(1.0)) 


  ####################### Tagger uncertainties

  #  cb.cp().AddSyst(cb,'CMS_cTagWeight_JEC','shape',ch.SystMap()(1.0))
  #   cb.cp().AddSyst(cb,'CMS_cTagWeight_JER','shape',ch.SystMap()(1.0))
  #   cb.cp().AddSyst(cb,'CMS_cTagWeight_JES','shape',ch.SystMap()(1.0))
  #   cb.cp().AddSyst(cb,'CMS_cTagWeight_PU','shape',ch.SystMap()(1.0))
  #   cb.cp().AddSyst(cb,'CMS_cTagWeight_EleId','shape',ch.SystMap()(1.0))
  #   cb.cp().AddSyst(cb,'CMS_cTagWeight_MuId','shape',ch.SystMap()(1.0))
  #   cb.cp().AddSyst(cb,'CMS_cTagWeight_muR','shape',ch.SystMap()(1.0))
  #   cb.cp().AddSyst(cb,'CMS_cTagWeight_mu','shape',ch.SystMap()(1.0))
  #   cb.cp().AddSyst(cb,'CMS_cTagWeight_XSecDYJets','shape',ch.SystMap()(1.0))
  #   cb.cp().AddSyst(cb,'CMS_cTagWeight_XSecST','shape',ch.SystMap()(1.0))
  #   cb.cp().AddSyst(cb,'CMS_cTagWeight_XSecWJets','shape',ch.SystMap()(1.0))
  #   cb.cp().AddSyst(cb,'CMS_cTagWeight_XSecTTbar','shape',ch.SystMap()(1.0))
  #   cb.cp().AddSyst(cb,'CMS_cTagWeight_Stat_2017','shape',ch.SystMap()(1.0))

  #============= post-cTagWeight uncertainties

    cb.cp().AddSyst(cb,'CMS_cjetSFs_13TeV_2017','shape',ch.SystMap()(1.0))


########################################################################################################################################
### Uncertainties for 2018
########################################################################################################################################
