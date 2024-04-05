declare -A unc=( ["stat"]="'--freezeParameters allConstrainedNuisances'" ) #["theo"]="'--freezeParameters rgx{BR.*},rgx{UEPS.*},FS_hc,rgx{PDFalphaS.*},rgx{UEPS.*},rgx{QCDscale_hc.*},flavor_composition_ggH,rgx{pdf.*},rgx{scale.*},rgx{theo.*}'")
# ["fr_theory+lepID"]="--freezeParameters BR_HWW_alphas,BR_HWW_mq,BR_HWW_theo,UEPS_FSR_higgs_13TeV,UEPS_FSR_st_13TeV,UEPS_FSR_ttbar_13TeV,UEPS_FSR_vv_13TeV,UEPS_FSR_zjets_13TeV,UEPS_ISR_higgs_13TeV,UEPS_ISR_st_13TeV,UEPS_ISR_ttbar_13TeV,UEPS_ISR_vv_13TeV,UEPS_ISR_zjets_13TeV,pt_weight,CMS_eff_HLT_2016_postVFP_13TeV,CMS_eff_HLT_2016_preVFP_13TeV,CMS_eff_HLT_2017_13TeV,CMS_eff_HLT_2018_13TeV,rgx{prop.*} --freezeNuisanceGroups theory_sig,theory_bkg,exp_lepID,exp_lumi,exp_other_weights" ) #unc=( ["fr_theory"]="--freezeParameters BR_HWW_alphas,BR_HWW_mq,BR_HWW_theo,UEPS_FSR_higgs_13TeV,UEPS_FSR_st_13TeV,UEPS_FSR_ttbar_13TeV,UEPS_FSR_vv_13TeV,UEPS_FSR_zjets_13TeV,UEPS_ISR_higgs_13TeV,UEPS_ISR_st_13TeV,UEPS_ISR_ttbar_13TeV,UEPS_ISR_vv_13TeV,UEPS_ISR_zjets_13TeV,pt_weight --freezeNuisanceGroups theory_sig,theory_bkg" ["fr_theoryHc"]="--freezeNuisanceGroups theory_sig" )
# unc=( ["fr_mcstat"]="'--freezeParameters rgx{prop.*}'" ["fr_theory"]="--freezeParameters BR_HWW_alphas,BR_HWW_mq,BR_HWW_theo,UEPS_FSR_higgs_13TeV,UEPS_FSR_st_13TeV,UEPS_FSR_ttbar_13TeV,UEPS_FSR_vv_13TeV,UEPS_FSR_zjets_13TeV,UEPS_ISR_higgs_13TeV,UEPS_ISR_st_13TeV,UEPS_ISR_ttbar_13TeV,UEPS_ISR_vv_13TeV,UEPS_ISR_zjets_13TeV,pt_weight,rgx{prop.*} --freezeNuisanceGroups theory_sig,theory_bkg" ["fr_theoryHc"]="--freezeParameters rgx{prop.*} --freezeNuisanceGroups theory_sig" ["fr_theory+lepID"]="--freezeParameters BR_HWW_alphas,BR_HWW_mq,BR_HWW_theo,UEPS_FSR_higgs_13TeV,UEPS_FSR_st_13TeV,UEPS_FSR_ttbar_13TeV,UEPS_FSR_vv_13TeV,UEPS_FSR_zjets_13TeV,UEPS_ISR_higgs_13TeV,UEPS_ISR_st_13TeV,UEPS_ISR_ttbar_13TeV,UEPS_ISR_vv_13TeV,UEPS_ISR_zjets_13TeV,pt_weight,CMS_eff_HLT_2016_postVFP_13TeV,CMS_eff_HLT_2016_preVFP_13TeV,CMS_eff_HLT_2017_13TeV,CMS_eff_HLT_2018_13TeV,rgx{prop.*} --freezeNuisanceGroups theory_sig,theory_bkg,exp_lepID,exp_lumi,exp_other_weights,"  ["fr_theory+lepID+met"]="--freezeParameters BR_HWW_alphas,BR_HWW_mq,BR_HWW_theo,UEPS_FSR_higgs_13TeV,UEPS_FSR_st_13TeV,UEPS_FSR_ttbar_13TeV,UEPS_FSR_vv_13TeV,UEPS_FSR_zjets_13TeV,UEPS_ISR_higgs_13TeV,UEPS_ISR_st_13TeV,UEPS_ISR_ttbar_13TeV,UEPS_ISR_vv_13TeV,UEPS_ISR_zjets_13TeV,pt_weight,CMS_eff_HLT_2016_postVFP_13TeV,CMS_eff_HLT_2016_preVFP_13TeV,CMS_eff_HLT_2017_13TeV,CMS_eff_HLT_2018_13TeV,CMS_scale_met_2016_13TeV,CMS_scale_met_2017_13TeV,CMS_scale_met_2018_13TeV,rgx{prop.*} --freezeNuisanceGroups theory_sig,theory_bkg,exp_lepID,exp_lumi,exp_other_weights" ["fr_theory+lepID+met+jerc"]="--freezeParameters BR_HWW_alphas,BR_HWW_mq,BR_HWW_theo,UEPS_FSR_higgs_13TeV,UEPS_FSR_st_13TeV,UEPS_FSR_ttbar_13TeV,UEPS_FSR_vv_13TeV,UEPS_FSR_zjets_13TeV,UEPS_ISR_higgs_13TeV,UEPS_ISR_st_13TeV,UEPS_ISR_ttbar_13TeV,UEPS_ISR_vv_13TeV,UEPS_ISR_zjets_13TeV,pt_weight,CMS_eff_HLT_2016_postVFP_13TeV,CMS_eff_HLT_2016_preVFP_13TeV,CMS_eff_HLT_2017_13TeV,CMS_eff_HLT_2018_13TeV,CMS_res_j_2016_13TeV,CMS_res_j_2017_13TeV,CMS_res_j_2018_13TeV,CMS_scale_met_2016_13TeV,CMS_scale_met_2017_13TeV,CMS_scale_met_2018_13TeV,rgx{prop.*} --freezeNuisanceGroups theory_sig,theory_bkg,exp_lepID,exp_lumi,exp_other_weights,exp_split_JERC")

# 
# combineCards.py  cards/2016_preVFP_updated_2016_preVFP/hc_emu_all_13TeV.txt  cards/2016_postVFP_updated_2016_postVFP/hc_emu_all_13TeV.txt  cards/2017_updated_2017/hc_emu_all_13TeV.txt  cards/2018_updated_2018/hc_emu_all_13TeV.txt>cards/run2_updated_run2/hc_emu_all_13TeV.txt
# sed -i 's/cards\/2016_preVFP_updated_2016_preVFP\/cards\/2016_preVFP_updated_2016_preVFP/cards\/2016_preVFP_updated_2016_preVFP/g' cards/run2_updated_run2/hc_emu_all_13TeV.txt
# sed -i 's/cards\/2016_postVFP_updated_2016_postVFP\/cards\/2016_postVFP_updated_2016_postVFP/cards\/2016_postVFP_updated_2016_postVFP/g' cards/run2_updated_run2/hc_emu_all_13TeV.txt
# sed -i 's/cards\/2017_updated_2017\/cards\/2017_updated_2017/cards\/2017_updated_2017/g' cards/run2_updated_run2/hc_emu_all_13TeV.txt
# sed -i 's/cards\/2018_updated_2018\/cards\/2018_updated_2018/cards\/2018_updated_2018/g' cards/run2_updated_run2/hc_emu_all_13TeV.txt
# combineCards.py  cards/2016_preVFP_updated_2016_preVFP/hc_emu_all1D_13TeV.txt  cards/2016_postVFP_updated_2016_postVFP/hc_emu_all1D_13TeV.txt  cards/2017_updated_2017/hc_emu_all1D_13TeV.txt  cards/2018_updated_2018/hc_emu_all1D_13TeV.txt>cards/run2_updated_run2/hc_emu_all1D_13TeV.txt
# sed -i 's/cards\/2016_preVFP_updated_2016_preVFP\/cards\/2016_preVFP_updated_2016_preVFP/cards\/2016_preVFP_updated_2016_preVFP/g' cards/run2_updated_run2/hc_emu_all1D_13TeV.txt
# sed -i 's/cards\/2016_postVFP_updated_2016_postVFP\/cards\/2016_postVFP_updated_2016_postVFP/cards\/2016_postVFP_updated_2016_postVFP/g' cards/run2_updated_run2/hc_emu_all1D_13TeV.txt
# sed -i 's/cards\/2017_updated_2017\/cards\/2017_updated_2017/cards\/2017_updated_2017/g' cards/run2_updated_run2/hc_emu_all1D_13TeV.txt
# sed -i 's/cards\/2018_updated_2018\/cards\/2018_updated_2018/cards\/2018_updated_2018/g' cards/run2_updated_run2/hc_emu_all1D_13TeV.txt
# 
for frunc in "${!unc[@]}"
do 
	version=unc
	
	for year in 2018 #run2 #run2 #2016_preVFP  #2017 2018  2016_postVFP 2016_preVFP 
	do
		for m in  limit #impact #scan #scan fit_diag 
		do
		
		for card in hc_emu_all_13TeV hc_emu_all1D_13TeV   #hc_emu_2_13TeV.txt #hc_emu_SR_1D_LM_comb_13TeV #
		do
		
			# combineCards.py  cards/2016_preVFP_${version}_2016_preVFP/${card}.txt  cards/2016_postVFP_${version}_2016_postVFP/${card}.txt  cards/2017_${version}_2017/${card}.txt  cards/2018_${version}_2018/${card}.txt>cards/run2_${version}_run2/${card}.txt
			# sed -i 's/cards\/2016_preVFP_${version}_2016_preVFP\/cards\/2016_preVFP_${version}_2016_preVFP/cards\/2016_preVFP_${version}_2016_preVFP/g' cards/run2_${version}_run2/${card}.txt
			# sed -i 's/cards\/2016_postVFP_${version}_2016_postVFP\/cards\/2016_postVFP_${version}_2016_postVFP/cards\/2016_postVFP_${version}_2016_postVFP/g' cards/run2_${version}_run2/${card}.txt
			# sed -i 's/cards\/2017_${version}_2017\/cards\/2017_${version}_2017/cards\/2017_${version}_2017/g' cards/run2_${version}_run2/${card}.txt
			# sed -i 's/cards\/2018_${version}_2018\/cards\/2018_${version}_2018/cards\/2018_${version}_2018/g' cards/run2_${version}_run2/${card}.txt
				
			
			echo $frunc
			config=$year
			if grep -q "2016" <<< "$year"; then
			config="2016"
			fi
			if  grep -q "1D" <<< "$card"  #|| [ "$card"=="hc_emu_2_13TeV" ] || [ "$card"=="inputhc_emu_4_13TeV" ]
			#if [ "$card"=="hc_emu_2_13TeV" ] || [ "$card"=="inputhc_emu_4_13TeV" ]
			then
			python run_combine.py  -d cards/${year}_${version}_${year}/${card} -M $m --t2w #--cbs="${unc[$frunc]}"  -p ${frunc}
			else
			echo $cbs
			python run_combine.py -d cards/${year}_${version}_${year}/${card} -M $m --twoPOI #--t2w #--cbs="=${unc[$frunc]}"  -p ${frunc}
			fi
			
		done
		done    
	done
done
#plot1DScan.py higgsCombinemu1_.r.MultiDimFit.mH125.root --main-label "Total Uncert." --others higgsCombinemu1_theo.r.MultiDimFit.mH125.root:"Stat.+Exp. Stat.":4 higgsCombinemu1_stat.r.MultiDimFit.mH125.root:"Stat.":2 --output scan_r_all --breakdown "theo.,exp.,stat." &
