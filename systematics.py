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
    cb.cp().process(['VVother','VZcc']).AddSyst(cb,'CMS_vhcc_VV', 'lnN', ch.SystMap()(1.05)) 
    cb.cp().process(['s_Top']).AddSyst(cb,'CMS_vhcc_ST', 'lnN', ch.SystMap()(1.15)) 

    # 
    

########################################################################################################################################
### Uncertainties for 2016
########################################################################################################################################
def AddSystematics2016(cb, chn):
 ####################### SCALE FACTORS RATEPARAM
    cb.cp().channel([chn]).process(["ttbar"]).AddSyst(
            cb, "CMS_SF_tt_%s_2016" % (chn), "rateParam", ch.SystMap()(1.0)
        )
    cb.GetParameter("CMS_SF_tt_%s_2016" % (chn)).set_range(0.0, 5.0)
    if chn != "emu":
        cb.cp().channel([chn]).process(["vjets"]).AddSyst(
            cb, "CMS_SF_vjets_%s_2016" % (chn), "rateParam", ch.SystMap()(1.0)
        )
        cb.GetParameter("CMS_SF_vjets_%s_2016" % (chn)).set_range(0.0, 5.0)

    
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #%%%%%%%%%%%%%%%%% EXPERIMENTAL UNCERTAINTIES

    cb.cp().AddSyst(cb,'lumi_13TeV_2016','lnN', ch.SystMap()(1.010))
    cb.cp().AddSyst(cb,'lumi_13TeV_correlated','lnN', ch.SystMap()(1.006))
    cb.cp().AddSyst(cb,'CMS_vhcc_puWeight_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_PUIDWeight_13TeV_2016','shape',ch.SystMap()(1.0))
    
    #============= Prefire efficiencies
    cb.cp().AddSyst(cb,'CMS_PrefireWeight','shape',ch.SystMap()(1.0))

    #============= lepton efficiencies

    cb.cp().channel(['Wmn']).AddSyst(cb,'CMS_vhcc_eff_m_Wln_13TeV_2016','lnN',ch.SystMap()(1.02))
    cb.cp().channel(['Wen']).AddSyst(cb,'CMS_vhcc_eff_e_Wln_13TeV_2016','lnN',ch.SystMap()(1.02))
    cb.cp().channel(['Zmm']).AddSyst(cb,'CMS_vhcc_eff_m_Zll_13TeV_2016','lnN',ch.SystMap()(1.04))
    cb.cp().channel(['Zee']).AddSyst(cb,'CMS_vhcc_eff_e_Zll_13TeV_2016','lnN',ch.SystMap()(1.04))

    #  cb.cp().channel(['Wmn']).AddSyst(cb,'CMS_Lep_S','shape',ch.SystMap()(1.0))
    #  cb.cp().channel(['Wen']).AddSyst(cb,'CMS_Lep_S','shape',ch.SystMap()(1.0))
    #  cb.cp().channel(['Zmm']).AddSyst(cb,'CMS_Lep_S','shape',ch.SystMap()(1.0))
    #  cb.cp().channel(['Zee']).AddSyst(cb,'CMS_Lep_S','shape',ch.SystMap()(1.0))


    #=============  met efficiencies
    cb.cp().channel(['Znn']).AddSyst(cb,'CMS_vhcc_trigger_MET_13TeV_2016','lnN',ch.SystMap()(1.02))

    #=============  VpT reweightings
    cb.cp().channel(['Zee','Zmm']).process(['Zj_ll','Zj_bj','Zj_cj']).AddSyst(cb,'CMS_vhcc_ptzweights_13TeV_2016','shape',ch.SystMap()(1.0))
    #  cb.cp().process(['TT']).AddSyst(cb,'CMS_vhcc_topptreweighting_13TeV_2016','shape',ch.SystMap()(1.0)) 
    #  cb.cp().channel(['Wen','Wmn']).process(['Wj_ll','Wj_bj','Wj_cl','Wj_cc','s_Top']).AddSyst(cb,'CMS_vhcc_ptwweights_13TeV_2016','shape',ch.SystMap()(1.0))
    #  cb.cp().channel(['Zee','Zmm','Znn']).process(['Zj_ll','Zj_bj','Zj_cl','Zj_cc']).AddSyst(cb,'CMS_vhcc_ptzweights_13TeV_2016','shape',ch.SystMap()(1.0))
    #  cb.cp().channel(['Zee','Zmm']).process(['s_Top']).AddSyst(cb,'CMS_vhcc_ptzweights_13TeV_2016','shape',ch.SystMap()(1.0))

    
    #  cb.cp().AddSyst(cb,
    #      'CMS_vhbb_EWK_Zll','shape',ch.SystMap('channel','bin_id','process')
    #      (['Zee','Zmm'],[1,2,3,4,5,6,7,8],['ZH_hbb'],1.0))


    #============= Jet energy scale and resolution

    cb.cp().AddSyst(cb,'CMS_res_j_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().channel(['Wen','Wmn','Znn']).AddSyst(cb,'CMS_METUnclustEn','shape',ch.SystMap()(1.0)) 
    #  cb.cp().AddSyst(cb,'CMS_res_j_reg_13TeV_2016','shape',ch.SystMap()(1.0)) 

    cb.cp().process(['ZH_hcc','WH_hcc','ggZH_hcc','ZH_hbb','WH_hbb','ggZH_hbb','VVother','VZcc']).AddSyst(cb,'CMS_j_PtCReg_Scale','shape',ch.SystMap()(1.0))
    cb.cp().process(['ZH_hcc','WH_hcc','ggZH_hcc','ZH_hbb','WH_hbb','ggZH_hbb','VVother','VZcc']).AddSyst(cb,'CMS_j_PtCReg_Smear','shape',ch.SystMap()(1.0))

    if splitJEC:
        #split as JET/MET recommends - NEW 11-splitting scheme
        cb.cp().AddSyst(cb,'CMS_scale_j_Absolute','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_BBEC1','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_EC2','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_FlavorQCD','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_H','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_RelativeBal','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_Absolute_2016','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_BBEC1_2016','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_EC2_2016','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_HF_2016','shape',ch.SystMap()(1.0))
        cb.cp().AddSyst(cb,'CMS_scale_j_RelativeSample_2016','shape',ch.SystMap()(1.0))


    #    # split as JET/MET recommends
    #    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpDataMC_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpPtRef_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpPtBB_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpPtEC1_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpPtEC2_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpPtHF_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeBal_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeJEREC1_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeJEREC2_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeJERHF_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeFSR_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeStatFSR_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeStatEC_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeStatHF_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_RelativePtBB_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_RelativePtHF_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_RelativePtEC1_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_RelativePtEC2_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_AbsoluteScale_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_AbsoluteMPFBias_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_AbsoluteStat_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_SinglePionECAL_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_SinglePionHCAL_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_Fragmentation_13TeV_2016','shape',ch.SystMap()(1.0))
    #    cb.cp().AddSyst(cb,'CMS_scale_j_FlavorQCD_13TeV_2016','shape',ch.SystMap()(1.0))
        
    else:
        cb.cp().AddSyst(cb,'CMS_scale_j_13TeV_2016','shape',ch.SystMap()(1.0))

    #============= c-tagger uncertainties - inclusive in pt/eta


    #  cb.cp().AddSyst(cb,'CMS_cTagWeight_JEC','shape',ch.SystMap()(1.0))

    cb.cp().AddSyst(cb,'CMS_cTagWeight_JER','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_cTagWeight_JES','shape',ch.SystMap()(1.0))

    #Luca special test
    #  cb.cp().channel(['Zee','Zmm']).bin_id([1,2,5,6,9,10]).AddSyst(cb,'CMS_cTagWeight_JER','shape',ch.SystMap()(1.0))
    #  cb.cp().channel(['Zee','Zmm']).bin_id([1,2,5,6,9,10]).AddSyst(cb,'CMS_cTagWeight_JES','shape',ch.SystMap()(1.0))
    #  cb.cp().channel(['Wen','Wmn','Znn']).bin_id([1,5,9]).AddSyst(cb,'CMS_cTagWeight_JER','shape',ch.SystMap()(1.0))
    #  cb.cp().channel(['Wen','Wmn','Znn']).bin_id([1,5,9]).AddSyst(cb,'CMS_cTagWeight_JES','shape',ch.SystMap()(1.0))


    cb.cp().AddSyst(cb,'CMS_cTagWeight_PU','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_cTagWeight_muR','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_cTagWeight_mu','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_cTagWeight_Stat_2016','shape',ch.SystMap()(1.0))    
    cb.cp().AddSyst(cb,'CMS_cTagWeight_EleId','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_cTagWeight_MuId','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_cTagWeight_XSecDYJets','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_cTagWeight_XSecST','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_cTagWeight_XSecWJets','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_cTagWeight_XSecTTbar','shape',ch.SystMap()(1.0))

    #============= post-cTagWeight uncertainties

    cb.cp().AddSyst(cb,'CMS_PostCTagWeight_13TeV_2016','shape',ch.SystMap()(1.0))
    #  cb.cp().channel(['Zee','Zmm']).process(['ZH_hcc','WH_hcc','ggZH_hcc','ZH_hbb','WH_hbb','ggZH_hbb','Zj_ll','Zj_bj','Zj_cj','Wj_ll','Wj_bj','Wj_cj','VVother','VZcc']).bin_id([1,2,3,4,5,6,7,8,9,10]).AddSyst(cb,'CMS_PostCTagWeight_13TeV_2016','shape',ch.SystMap()(1.0))
    #  cb.cp().channel(['Wen','Wmn','Znn']).process(['ZH_hcc','WH_hcc','ggZH_hcc','ZH_hbb','WH_hbb','ggZH_hbb','Zj_ll','Zj_bj','Zj_cj','Wj_ll','Wj_bj','Wj_cj','VVother','VZcc']).bin_id([1,3,5,7,9]).AddSyst(cb,'CMS_PostCTagWeight_13TeV_2016','shape',ch.SystMap()(1.0))
    #  cb.cp().channel(['Zee','Zmm']).process(['s_Top','TT']).bin_id([1,2,5,6,9,10]).AddSyst(cb,'CMS_PostCTagWeight_13TeV_2016','shape',ch.SystMap()(1.0))
    #  cb.cp().channel(['Wen','Wmn','Znn']).process(['s_Top','TT']).bin_id([1,5,9]).AddSyst(cb,'CMS_PostCTagWeight_13TeV_2016','shape',ch.SystMap()(1.0))

    #fit uncertainties on DY(ll)+jets process (taken from 2L, but applied to DY+jets in all the channels)
    cb.cp().channel(['Zee','Zmm','Wen','Wmn','Znn']).process(['Zj_ll','Zj_bj','Zj_cj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_fit_Zll_2016','shape',ch.SystMap()(1.0))

    #fit uncertainties on W+jets process (taken from 1L, but applied to W+jets in all the channels: 1L and 0L)
    cb.cp().channel(['Wen','Wmn','Znn']).process(['Wj_ll','Wj_bj','Wj_cj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_fit_Wln_2016','shape',ch.SystMap()(1.0))

    #fit uncertainties on Z(nn)+jets process (taken from 0L, but applied to Z(nn)+jets in all the channels: 0L only in this case)
    cb.cp().channel(['Znn']).process(['Zj_ll','Zj_bj','Zj_cj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_fit_Znn_2016','shape',ch.SystMap()(1.0))
    
    cb.cp().channel(['Zee','Zmm']).process(['Zj_cj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_Flavour_Zj_cj_2016','shape',ch.SystMap()(1.0))
    cb.cp().channel(['Zee','Zmm']).process(['Zj_bj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_Flavour_Zj_bj_2016','shape',ch.SystMap()(1.0))  
    cb.cp().channel(['Wen','Wmn','Znn']).process(['Zj_cj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_Flavour_Zj_cj_2016','shape',ch.SystMap()(1.0))
    cb.cp().channel(['Wen','Wmn','Znn']).process(['Zj_bj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_Flavour_Zj_bj_2016','shape',ch.SystMap()(1.0))
    cb.cp().channel(['Wen','Wmn','Znn']).process(['Wj_cj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_Flavour_Wj_cj_2016','shape',ch.SystMap()(1.0))
    cb.cp().channel(['Wen','Wmn','Znn']).process(['Wj_bj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_Flavour_Wj_bj_2016','shape',ch.SystMap()(1.0))

########################################################################################################################################
### Uncertainties for 2017
########################################################################################################################################
def AddSystematics2017(cb, chn,splitJEC=False):

####################### SCALE FACTORS RATEPARAM
    cb.cp().channel([chn]).process(["ttbar"]).AddSyst(
            cb, "CMS_SF_tt_%s_2017" % (chn), "rateParam", ch.SystMap()(1.0)
        )
    cb.GetParameter("CMS_SF_tt_%s_2017" % (chn)).set_range(0.0, 5.0)
    if chn != "emu":
        cb.cp().channel([chn]).process(["vjets"]).AddSyst(
            cb, "CMS_SF_vjets_%s_2017" % (chn), "rateParam", ch.SystMap()(1.0)
        )
        cb.GetParameter("CMS_SF_vjets_%s_2017" % (chn)).set_range(0.0, 5.0)


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%% EXPERIMENTAL UNCERTAINTIES
    cb.cp().AddSyst(cb,'lumi_13TeV_2017','lnN', ch.SystMap()(1.020))
    cb.cp().AddSyst(cb,'lumi_13TeV_1718','lnN', ch.SystMap()(1.006))
    cb.cp().AddSyst(cb,'lumi_13TeV_correlated','lnN', ch.SystMap()(1.009))  
    for proc in ["st", "vv", "vjets", "ttbar", "higgs","hc"]:
      cb.cp().process([proc]).AddSyst(cb,'puweight_%s' %(proc),'shape',ch.SystMap()(1.0))

#============= Prefire efficiencies
      cb.cp().process([proc]).AddSyst(cb,'L1prefireweight_%s' %(proc),'shape',ch.SystMap()(1.0))

#============= lepton efficiencies

      cb.cp().process([proc]).channel(['ee','emu']).AddSyst(cb,'eleSFs_%s' %(proc),'shape',ch.SystMap()(1.0))
      cb.cp().process([proc]).channel(['mumu','eum']).AddSyst(cb,'muSFs_%s' %(proc),'shape',ch.SystMap()(1.0))

#============= Jet energy scale and resolution
      cb.cp().process([proc]).AddSyst(cb,'JES_%s' %(proc),'shape',ch.SystMap()(1.0))
      cb.cp().process([proc]).AddSyst(cb,'JER_%s' %(proc),'shape',ch.SystMap()(1.0))
      cb.cp().process([proc]).AddSyst(cb,'UES_%s' %(proc),'shape',ch.SystMap()(1.0)) 


#============= tagger uncertainties

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

#   cb.cp().AddSyst(cb,'CMS_PostCTagWeight_13TeV_2017','shape',ch.SystMap()(1.0))
      cb.cp().process([proc]).AddSyst(cb,'cjetSFs_%s' %(proc),'shape',ch.SystMap()(1.0))


########################################################################################################################################
### Uncertainties for 2018
########################################################################################################################################
def AddSystematics2018(cb, splitJEC=False):

  cb.cp().process(['Wj_bj']).AddSyst(cb,'Norm_Wj_bj_2018', 'lnN', ch.SystMap()(1.50))

####################### SCALE FACTORS RATEPARAM
  
  # TT Zll
  cb.cp().channel(['Zee','Zmm']).process(['TT']).AddSyst(cb,
     'SF_TT_high_Zll_2018', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  cb.cp().channel(['Zee','Zmm']).process(['TT']).AddSyst(cb,
     'SF_TT_low_Zll_2018', 'rateParam', ch.SystMap('bin_id')
     ([2,4,6,8,10],1.0))

  # Zj_ll Zll
  cb.cp().channel(['Zee','Zmm']).process(['Zj_ll']).AddSyst(cb,
     'SF_Zj_ll_high_Zll_2018', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  cb.cp().channel(['Zee','Zmm']).process(['Zj_ll']).AddSyst(cb,
     'SF_Zj_ll_low_Zll_2018', 'rateParam', ch.SystMap('bin_id')
     ([2,4,6,8,10],1.0))

  # Zj_bj Zll
  cb.cp().channel(['Zee','Zmm']).process(['Zj_bj']).AddSyst(cb,
     'SF_Zj_bj_high_Zll_2018', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  cb.cp().channel(['Zee','Zmm']).process(['Zj_bj']).AddSyst(cb,
     'SF_Zj_bj_low_Zll_2018', 'rateParam', ch.SystMap('bin_id')
     ([2,4,6,8,10],1.0))

  # Zj_cj Zll
  cb.cp().channel(['Zee','Zmm']).process(['Zj_cj']).AddSyst(cb,
     'SF_Zj_cj_high_Zll_2018', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  cb.cp().channel(['Zee','Zmm']).process(['Zj_cj']).AddSyst(cb,
     'SF_Zj_cj_low_Zll_2018', 'rateParam', ch.SystMap('bin_id')
     ([2,4,6,8,10],1.0))

  # TT Znn
  cb.cp().channel(['Znn']).process(['TT']).AddSyst(cb,
     'SF_TT_Znn_2018', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  # Zj_ll Znn
  cb.cp().channel(['Znn']).process(['Zj_ll']).AddSyst(cb,
     'SF_Zj_ll_Znn_2018', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  # Zj_bj Znn
  cb.cp().channel(['Znn']).process(['Zj_bj']).AddSyst(cb,
     'SF_Zj_bj_Znn_2018', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  # Zj_cj Znn
  cb.cp().channel(['Znn']).process(['Zj_cj']).AddSyst(cb,
     'SF_Zj_cj_Znn_2018', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  # TT Wln
  cb.cp().channel(['Wen','Wmn']).process(['TT']).AddSyst(cb,
     'SF_TT_Wln_2018', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  # Wj_ll Wln
  cb.cp().channel(['Wen','Wmn','Znn']).process(['Wj_ll']).AddSyst(cb,
     'SF_Wj_ll_Wln_2018', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

#BASELINE-RESTORE  # Wj_bj Wln
#BASELINE-RESTORE  cb.cp().channel(['Wen','Wmn','Znn']).process(['Wj_bj']).AddSyst(cb,
#BASELINE-RESTORE     'SF_Wj_bj_Wln_2018', 'rateParam', ch.SystMap('bin_id')
#BASELINE-RESTORE     ([1,3,5,7,9],1.0))

  # Wj_cj Wln
  cb.cp().channel(['Wen','Wmn','Znn']).process(['Wj_cj','Wj_bj']).AddSyst(cb,
     'SF_Wj_cj_Wln_2018', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))


  #Set a sensible range for the rate params
  for syst in cb.cp().syst_type(["rateParam"]).syst_name_set():
    if not (syst=='SF_Wj_ll_Znn_2018' or syst=='SF_Wj_cj_Znn_2018'):
      cb.GetParameter(syst).set_range(0.0,5.0)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%% EXPERIMENTAL UNCERTAINTIES
  cb.cp().AddSyst(cb,'lumi_13TeV_2018','lnN', ch.SystMap()(1.015))
  cb.cp().AddSyst(cb,'lumi_13TeV_1718','lnN', ch.SystMap()(1.002))
  cb.cp().AddSyst(cb,'lumi_13TeV_correlated','lnN', ch.SystMap()(1.020))
  cb.cp().AddSyst(cb,'CMS_vhcc_puWeight_2018','shape',ch.SystMap()(1.0))
#  cb.cp().AddSyst(cb,'CMS_vhcc_puBackupWeight_2018','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_PUIDWeight_13TeV_2018','shape',ch.SystMap()(1.0))

#============= HEM 15/16 uncertainties

  cb.cp().AddSyst(cb,'CMS_scale_j_HEMIssue_13TeV_2018','shape',ch.SystMap()(1.0))

#============= lepton efficiencies

  cb.cp().channel(['Wmn']).AddSyst(cb,'CMS_vhcc_eff_m_Wln_13TeV_2018','lnN',ch.SystMap()(1.02))
  cb.cp().channel(['Wen']).AddSyst(cb,'CMS_vhcc_eff_e_Wln_13TeV_2018','lnN',ch.SystMap()(1.02))
  cb.cp().channel(['Zmm']).AddSyst(cb,'CMS_vhcc_eff_m_Zll_13TeV_2018','lnN',ch.SystMap()(1.04))
  cb.cp().channel(['Zee']).AddSyst(cb,'CMS_vhcc_eff_e_Zll_13TeV_2018','lnN',ch.SystMap()(1.04))

#=============  met efficiencies
  cb.cp().channel(['Znn']).AddSyst(cb,'CMS_vhcc_trigger_MET_13TeV_2018','lnN',ch.SystMap()(1.02))

#=============  VpT reweightings - to comment for NLO
#  cb.cp().process(['TT']).AddSyst(cb,'CMS_vhcc_topptreweighting_13TeV_2018','shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['Zee','Zmm']).process(['Zj_ll','Zj_bj','Zj_cj']).AddSyst(cb,'CMS_vhcc_ptzweights_13TeV_2018','shape',ch.SystMap()(1.0))
#uncomment for LO  cb.cp().channel(['Wen','Wmn']).process(['Wj_ll','Wj_blc','Wj_bbc','Wj_cc','s_Top']).AddSyst(cb,'CMS_vhcc_ptwweights_13TeV_2016','shape',ch.SystMap()(1.0))
#uncomment for LO  cb.cp().channel(['Zee','Zmm','Znn']).process(['Zj_ll','Zj_blc','Zj_bbc','Zj_cc']).AddSyst(cb,'CMS_vhcc_ptzweights_13TeV_2016','shape',ch.SystMap()(1.0))
#uncomment for LO  cb.cp().channel(['Zee','Zmm']).process(['s_Top']).AddSyst(cb,'CMS_vhcc_ptzweights_13TeV_2016','shape',ch.SystMap()(1.0))

  
#  cb.cp().AddSyst(cb,
#      'CMS_vhbb_EWK_Zll','shape',ch.SystMap('channel','bin_id','process')
#      (['Zee','Zmm'],[1,2,3,4,5,6,7,8],['ZH_hbb'],1.0))


#============= Jet energy scale and resolution
  cb.cp().AddSyst(cb,'CMS_res_j_13TeV_2018','shape',ch.SystMap()(1.0))
  cb.cp().channel(['Wen','Wmn','Znn']).AddSyst(cb,'CMS_METUnclustEn','shape',ch.SystMap()(1.0)) 

  cb.cp().process(['ZH_hcc','WH_hcc','ggZH_hcc','ZH_hbb','WH_hbb','ggZH_hbb','VVother','VZcc']).AddSyst(cb,'CMS_j_PtCReg_Scale','shape',ch.SystMap()(1.0))
  cb.cp().process(['ZH_hcc','WH_hcc','ggZH_hcc','ZH_hbb','WH_hbb','ggZH_hbb','VVother','VZcc']).AddSyst(cb,'CMS_j_PtCReg_Smear','shape',ch.SystMap()(1.0))

  if splitJEC:
    #split as JET/MET recommends - NEW 11-splitting scheme
    cb.cp().AddSyst(cb,'CMS_scale_j_Absolute','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_BBEC1','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_EC2','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_FlavorQCD','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_H','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeBal','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_Absolute_2018','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_BBEC1_2018','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_EC2_2018','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_HF_2018','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeSample_2018','shape',ch.SystMap()(1.0))

#    # split as JET/MET recommends
#    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpDataMC_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpPtRef_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpPtBB_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpPtEC1_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpPtEC2_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpPtHF_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeBal_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeJEREC1_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeJEREC2_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeJERHF_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeFSR_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeStatFSR_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeStatEC_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeStatHF_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_RelativePtBB_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_RelativePtHF_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_RelativePtEC1_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_RelativePtEC2_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_AbsoluteScale_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_AbsoluteMPFBias_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_AbsoluteStat_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_SinglePionECAL_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_SinglePionHCAL_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_Fragmentation_13TeV_2016','shape',ch.SystMap()(1.0))
#    cb.cp().AddSyst(cb,'CMS_scale_j_FlavorQCD_13TeV_2016','shape',ch.SystMap()(1.0))
    
  else:
    cb.cp().AddSyst(cb,'CMS_scale_j_13TeV_2018','shape',ch.SystMap()(1.0))

#============= tagger uncertainties
#  cb.cp().AddSyst(cb,'CMS_cTagWeight_JEC','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_JER','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_JES','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_PU','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_EleId','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_MuId','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_muR','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_mu','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_XSecDYJets','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_XSecST','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_XSecWJets','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_XSecTTbar','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_Stat_2018','shape',ch.SystMap()(1.0))  


#============= post-cTagWeight uncertainties

  cb.cp().AddSyst(cb,'CMS_PostCTagWeight_13TeV_2018','shape',ch.SystMap()(1.0))

#  cb.cp().channel(['Zee','Zmm']).process(['ZH_hcc','WH_hcc','ggZH_hcc','ZH_hbb','WH_hbb','ggZH_hbb','Zj_ll','Zj_bj','Zj_cj','Wj_ll','Wj_bj','Wj_cj','VVother','VZcc']).bin_id([1,2,3,4,5,6,7,8,9,10]).AddSyst(cb,'CMS_PostCTagWeight_13TeV_2018','shape',ch.SystMap()(1.0))
#  cb.cp().channel(['Wen','Wmn','Znn']).process(['ZH_hcc','WH_hcc','ggZH_hcc','ZH_hbb','WH_hbb','ggZH_hbb','Zj_ll','Zj_bj','Zj_cj','Wj_ll','Wj_bj','Wj_cj','VVother','VZcc']).bin_id([1,3,5,7,9]).AddSyst(cb,'CMS_PostCTagWeight_13TeV_2018','shape',ch.SystMap()(1.0))
#  cb.cp().channel(['Zee','Zmm']).process(['s_Top','TT']).bin_id([1,2,5,6,9,10]).AddSyst(cb,'CMS_PostCTagWeight_13TeV_2018','shape',ch.SystMap()(1.0))
#  cb.cp().channel(['Wen','Wmn','Znn']).process(['s_Top','TT']).bin_id([1,5,9]).AddSyst(cb,'CMS_PostCTagWeight_13TeV_2018','shape',ch.SystMap()(1.0))


#============= dRjj-Reweighting uncertainties

#fit uncertainties on DY(ll)+jets process (taken from 2L, but applied to DY+jets in all the channels)
#  cb.cp().channel(['Zee','Zmm','Wen','Wmn','Znn']).process(['Zj_ll','Zj_bj','Zj_cj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_fit_Zll_2018','shape',ch.SystMap('bin_id')([1,2,3,4,5,6],1.0))
  cb.cp().channel(['Zee','Zmm']).process(['Zj_ll','Zj_bj','Zj_cj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_fit_Zll_2018','shape',ch.SystMap('bin_id')([1,2,3,4,5,6,9,10],1.0))

#fit uncertainties on W+jets process (taken from 1L, but applied to W+jets in all the channels: 1L and 0L)
  cb.cp().channel(['Wen','Wmn','Znn']).process(['Wj_ll','Wj_bj','Wj_cj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_fit_Wln_2018','shape',ch.SystMap('bin_id')([1,2,3,4,5,6,9,10],1.0))

#fit uncertainties on Z(nn)+jets process (taken from 0L, but applied to Z(nn)+jets in all the channels: 0L only in this case)
  cb.cp().channel(['Znn']).process(['Zj_ll','Zj_bj','Zj_cj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_fit_Znn_2018','shape',ch.SystMap('bin_id')([1,2,3,4,5,6,9,10],1.0))

  cb.cp().channel(['Zee','Zmm']).process(['Zj_cj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_Flavour_Zj_cj_2018','shape',ch.SystMap('bin_id')([1,2,3,4,5,6,9,10],1.0))
  cb.cp().channel(['Zee','Zmm']).process(['Zj_bj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_Flavour_Zj_bj_2018','shape',ch.SystMap('bin_id')([1,2,3,4,5,6,9,10],1.0)) 
  cb.cp().channel(['Wen','Wmn','Znn']).process(['Zj_cj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_Flavour_Zj_cj_2018','shape',ch.SystMap('bin_id')([1,2,3,4,5,6,9,10],1.0))
  cb.cp().channel(['Wen','Wmn','Znn']).process(['Zj_bj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_Flavour_Zj_bj_2018','shape',ch.SystMap('bin_id')([1,2,3,4,5,6,9,10],1.0))
  cb.cp().channel(['Wen','Wmn','Znn']).process(['Wj_cj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_Flavour_Wj_cj_2018','shape',ch.SystMap('bin_id')([1,2,3,4,5,6,9,10],1.0))
  cb.cp().channel(['Wen','Wmn','Znn']).process(['Wj_bj']).AddSyst(cb,'CMS_vhcc_dRjjReweight_Flavour_Wj_bj_2018','shape',ch.SystMap('bin_id')([1,2,3,4,5,6,9,10],1.0))
