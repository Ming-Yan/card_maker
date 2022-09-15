## checking s/b scripts
import uproot
import matplotlib.pyplot as plt
# import mplhep as hep
# from matplotlib.offsetbox import AnchoredText
import numpy as np

f=uproot.open("cards/corrsyst_2017/inputhc_emu_2_13TeV.root")
f2=uproot.open("cards/corrPU_2017/inputhc_emu_2_13TeV.root")
bkg_proc = [ "vjets","ttbar","st", "vv", "ttbar", "higgs"]
# bkgup,bkg,bkgdn=[]
bkgup=np.zeros(len(f['hc_emu_2_13TeV/hc_CMS_puweight_13TeV_2017Up'].values()))
bkgdn=np.zeros(len(f['hc_emu_2_13TeV/hc_CMS_puweight_13TeV_2017Up'].values()))
bkg=np.zeros(len(f['hc_emu_2_13TeV/hc_CMS_puweight_13TeV_2017Up'].values()))
bkgup2=np.zeros(len(f['hc_emu_2_13TeV/hc_CMS_puweight_13TeV_2017Up'].values()))
bkgdn2=np.zeros(len(f['hc_emu_2_13TeV/hc_CMS_puweight_13TeV_2017Up'].values()))
bkg2=np.zeros(len(f['hc_emu_2_13TeV/hc_CMS_puweight_13TeV_2017Up'].values()))
for proc in bkg_proc:
    bkgup = f['hc_emu_2_13TeV/%s_CMS_puweight_13TeV_2017Up' %(proc)].values()+bkgup
    bkgdn = f['hc_emu_2_13TeV/%s_CMS_puweight_13TeV_2017Down' %(proc)].values()+bkgdn
    bkg = f['hc_emu_2_13TeV/%s' %(proc)].values()+bkg
    bkgup2 = f2['hc_emu_2_13TeV/%s_CMS_puweight_13TeV_2017Up' %(proc)].values()+bkgup2
    bkgdn2 = f2['hc_emu_2_13TeV/%s_CMS_puweight_13TeV_2017Down' %(proc)].values()+bkgdn2
    bkg2 = f2['hc_emu_2_13TeV/%s' %(proc)].values()+bkg2

sigup=f['hc_emu_2_13TeV/hc_CMS_puweight_13TeV_2017Up'].values()
sigdn=f['hc_emu_2_13TeV/hc_CMS_puweight_13TeV_2017Down'].values()
sig=f['hc_emu_2_13TeV/hc'].values()
sigup2=f2['hc_emu_2_13TeV/hc_CMS_puweight_13TeV_2017Up'].values()
sigdn2=f2['hc_emu_2_13TeV/hc_CMS_puweight_13TeV_2017Down'].values()
sig2=f2['hc_emu_2_13TeV/hc'].values()
edges= np.zeros(len(f['hc_emu_2_13TeV/hc_CMS_puweight_13TeV_2017Up'].values()))
for i in range(len(f['hc_emu_2_13TeV/hc_CMS_puweight_13TeV_2017Up'].values())):
    edges[i] = (f['hc_emu_2_13TeV/hc_CMS_puweight_13TeV_2017Up'].axis().edges()[i]+f['hc_emu_2_13TeV/hc_CMS_puweight_13TeV_2017Up'].axis().edges()[i+1])/2.
fig, ((ax), (rax)) = plt.subplots(
                2,1,
                figsize=(6, 6),
                gridspec_kw={"height_ratios": (3, 1)},
                 sharex=True,
                )
fig.subplots_adjust(hspace=0.05)
#ax.plot(edges,sig/np.sqrt(bkg),'ro',label="nominal")
#ax.plot(edges,sigup/np.sqrt(bkgup),'go',label="puwei Up" )
##ax.plot(edges,sigdn/np.sqrt(bkgdn),'bo',label="puwei Down")
ax.plot(edges,sig,'ro',label="nominal")
ax.plot(edges,sigup,'go',label="puwei Up" )
ax.plot(edges,sigdn,'bo',label="puwei Down")
ax.legend()
ax.set_ylabel("$s/\sqrt{b}$")
rax.plot(edges,sigup/sig,'go')
rax.plot(edges,sigdn/sig,'bo')
#rax.plot(edges,sigdn/np.sqrt(bkgdn)/(sig/np.sqrt(bkg)),'bo')
rax.set_ylabel("variation/nominal")
print(max(sigdn2/np.sqrt(bkgdn2)/(sig2/np.sqrt(bkg2))),max(sigup2/np.sqrt(bkgup2)/(sig2/np.sqrt(bkg2))))
print(max(sigdn/np.sqrt(bkgdn)/(sig/np.sqrt(bkg))),max(sigup/np.sqrt(bkgup)/(sig/np.sqrt(bkg))))
print(max(max(sigdn/sig),max(sigup/sig)),max(max(bkgdn/bkg),max(bkgup/bkg)))
print(np.sum(sig)/np.sum(sigdn),np.sum(sig)/np.sum(sigup),np.sum(bkg)/np.sum(bkgup),np.sum(bkg)/np.sum(bkgdn))
rax.set_xlabel("BDT")
#fig.savefig("sig_corrsyst_emu_SR2.png")
