def adjust_shape(proc,nbins):
  new_hist = proc.ShapeAsTH1F();
  new_hist.Scale(proc.rate())
  for i in range(1,new_hist.GetNbinsX()+1-nbins):
    new_hist.SetBinContent(i,0.)
  proc.set_shape(new_hist,True)

def drop_zero_procs(chob,proc):
  null_yield = not (proc.rate() > 0.)
  if(null_yield):
    chob.FilterSysts(lambda sys: matching_proc(proc,sys)) 
  return null_yield

# def drop_zero_systs(syst):
#   null_yield = (not (syst.value_u() > 0. and syst.value_d()>0.) ) and syst.type() in 'shape'
#   if(null_yield):
#     print 'Dropping systematic ',syst.name(),' for region ', syst.bin(), ' ,process ', syst.process(), '. up norm is ', syst.value_u() , ' and down norm is ', syst.value_d()
#     #chob.FilterSysts(lambda sys: matching_proc(proc,sys)) 
#   return null_yield

def matching_proc(p,s):
  return ((p.bin()==s.bin()) and (p.process()==s.process()) and (p.signal()==s.signal()) 
          and (p.analysis()==s.analysis()) and  (p.era()==s.era()) 
          and (p.channel()==s.channel()) and (p.bin_id()==s.bin_id()) and (p.mass()==s.mass()))


def remove_norm_effect(syst):
  syst.set_value_u(1.0)
  syst.set_value_d(1.0)

def symm(syst,nominal):
  print 'Symmetrising systematic ', syst.name(), ' in region ', syst.bin(), ' for process ', syst.process()
  hist_u = syst.ShapeUAsTH1F()
  hist_u.Scale(nominal.Integral()*syst.value_u())
  hist_d = nominal.Clone()
  hist_d.Scale(2)
  hist_d.Add(hist_u,-1)
  syst.set_shapes(hist_u,hist_d,nominal)
  
  
def symmetrise_syst(chob,proc,sys_name):
  nom_hist = proc.ShapeAsTH1F()
  nom_hist.Scale(proc.rate())
  chob.ForEachSyst(lambda s: symm(s,nom_hist) if (s.name()==sys_name and matching_proc(proc,s)) else None)

def increase_bin_errors(proc):
  print 'increasing bin errors for process ', proc.process(), ' in region ', proc.bin()
  new_hist = proc.ShapeAsTH1F();
  new_hist.Scale(proc.rate())
  for i in range(1,new_hist.GetNbinsX()+1):
    new_hist.SetBinError(i,np.sqrt(2)*new_hist.GetBinError(i))
  proc.set_shape(new_hist,False)

def decrease_bin_errors(proc):
  print 'decreasing bin errors for process ', proc.process(), ' in region ', proc.bin()
  new_hist = proc.ShapeAsTH1F();
  new_hist.Scale(proc.rate())
  for i in range(1,new_hist.GetNbinsX()+1):
    new_hist.SetBinError(i,new_hist.GetBinError(i)/2.0)
  proc.set_shape(new_hist,False)


def drop_noRealShape_systs(proc,syst):
  diff_lim=0.00025
  if syst.type()=='shape' : 
    hist_u = syst.ShapeUAsTH1F()
    hist_d = syst.ShapeDAsTH1F()
    hist_nom = proc.ShapeAsTH1F()
    hist_nom.Scale(1./hist_nom.Integral())
    up_diff=0
    down_diff=0
    print "SYSTEMATICS = ",syst.name(),syst.process(),syst.bin()
    for i in range(1,hist_u.GetNbinsX()+1):
      if hist_nom.GetBinContent(i)!=0:
        up_diff+=2*(abs(hist_u.GetBinContent(i)-hist_nom.GetBinContent(i)))/(abs(hist_u.GetBinContent(i))+abs(hist_nom.GetBinContent(i)))
        down_diff+=2*(abs(hist_d.GetBinContent(i)-hist_nom.GetBinContent(i)))/(abs(hist_u.GetBinContent(i))+abs(hist_nom.GetBinContent(i)))
    else:
        up_diff+=0
        down_diff+=0
    null_yield = (up_diff<diff_lim and down_diff<diff_lim)
    if(null_yield):
      #print "Uncertainty has no real shape effect. Summed rel. diff. per bin between norm. nominal and up/down shape: ",up_diff, down_diff
      print 'Dropping systematic ',syst.name(),' for region ', syst.bin(), ' ,process ', syst.process(), '. up int ', hist_u.Integral() , ' and down int is ', hist_d.Integral()
    return null_yield  

def PrintProc(proc):
  print  proc.channel(), proc.bin_id(), proc.process()

def PrintSyst(syst,proc):
  print  syst.channel(), syst.bin_id(), syst.process(), syst.name(), proc.process()
  
