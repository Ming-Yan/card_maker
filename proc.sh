read -p "version: " v
for y in 2018 #2016_preVFP  #2016_preVFP 2016_postVFP 2018
do    
    '''
    python post_proc.py -r top_CR_1j -y $y -v $v -f merge_bin -b 1
    python post_proc.py -r HM_CR_1j -y $y -v $v -f merge_bin
    python post_proc.py -r top_CR_nj -y $y -v $v -f merge_bin -b 1
    python post_proc.py -r HM_CR_nj -y $y -v $v -f merge_bin 

    for c in top_CR_1j HM_CR_1j top_CR_nj HM_CR_nj SR2_LM SR2_LM_1D SR_LM SR_LM_1D
    do 
	python post_proc.py -r $c  -y $y -v $v -f remove_neg
    done
    python post_proc.py -y $y -v $v -f merge_top -r HM_CR 
    python post_proc.py -y $y -v $v -f merge_top -r top_CR -b 1
    python post_proc.py -r SR_LM -y $y -v $v -f reorder_BDT
    python post_proc.py -r SR2_LM -y $y -v $v -f reorder_BDT
    '''
    python make_card.py -y $y --doshape --splitJEC --combine_cards -v ${y}_$v
done
