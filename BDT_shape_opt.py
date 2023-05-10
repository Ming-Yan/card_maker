import pandas as pd
import argparse,os,pickle,sys
import numpy as np
from scipy.stats.distributions import poisson
import hist


# Setup argparse
parser = argparse.ArgumentParser(description = "Tool to find best BDT shape otimization", usage = "")
parser.add_argument("-r", "--region", type=str, default = "SR2_LM", choices=["SR2_LM","SR_LM","HM"], help = "Sample to pick up ")
parser.add_argument("-u", "--sig", type=float, default=1., help="Signal strength parameter that BDT is optimized towards. For VZ optimization use -u=1")
parser.add_argument("-x", type=float, default = -1, help = "Value of parameter x")
# parser.add_argument("-y", type=float, default = -1, help = "Value of parameter y")
parser.add_argument("-nbins", type=float, default = -1, help = "Value of parameter nbins")
parser.add_argument("--makecondor", action="store_true", default = False, help = "List x, y and nbins values for batch run")
# parser.add_argument("-p", "--path", type=str, default = ".", help = "Directory containing all pkl files.")
parser.add_argument("-v","--version", type=str, default = ".", help = "version name")
parser.add_argument('-be', '--errB', type=float, default=1., help = 'Maximum background error')
parser.add_argument('-se', '--errS', type=float, default=1., help = 'Maximum signal error')
parser.add_argument("--params", default = [], type=str)
opt = parser.parse_args()
print(opt)

maxerrB = opt.errB
maxerrS = opt.errS


sigdf = pd.read_csv(f"opt_data/sig_{opt.version}_{opt.region}.csv")
bkgdf = pd.read_csv(f"opt_data/bkg_{opt.version}_{opt.region}.csv")

# def histoErrs(arr,binning,weights):
#     weights = np.array(weights)
#     binidx = np.digitize(arr, binning)
#     errs = []
#     for ibin in range(1,len(binning)):
#         # print np.where(binidx==ibin)
#         thisbinwts = weights[np.where(binidx==ibin)[0]]
#         #print np.average(thisbinwts), np.average(thisbinwts**2), len(thisbinwts)
#         #print thisbinwts.shape
#         # Add extra sqrt(2) to account for the fact that half of the events are used for BDT training
#         thisbinerr = np.sqrt(2*np.sum(thisbinwts**2.))
#         errs.append(thisbinerr) 
#     return np.array(errs)


def makeHisto(x,y,nbins,bin1,binn):
    # nbins = 10
    '''if bin1 > 0:
        binning = [0.]
        binning.extend(np.arange(bin1,binn,(binn-bin1)/(nbins-2)))
    else:
        binning = list(np.arange(0,binn,binn/(nbins-1)))
    if abs(binning[-1]-binn) < 1e-5:
        binning.extend([1.])
    else:
        binning.extend([binn,1.])
    print(binning)'''
    binning = np.arange(0,1,1./nbins)
    #print(binning)
    #print binning
    # sigarr = sigdf["BDT"].values #,1.)+np.power(sigdf["BDT"].values,y))/2
    # bkgarr = bkgdf["BDT"].values #(np.power(bkgdf["BDT"].values,1.)+np.power(bkgdf["BDT"].values,y))/2
    sigarr = (np.power(sigdf["BDT"].values ,x)+np.power(sigdf["BDT"].values,y))/2
    bkgarr = (np.power(bkgdf["BDT"].values ,x)+np.power(bkgdf["BDT"].values,y))/2
    # print(binning)
    histosig = hist.Hist(hist.axis.Variable(binning, name="BDT", label="discr"),
            hist.storage.Weight()
        )
    histobkg = hist.Hist(hist.axis.Variable(binning, name="BDT", label="discr"),
            hist.storage.Weight()
        )
    histosig.fill(sigarr,weight=sigdf["weight"].values)
    histobkg.fill(bkgarr,weight=bkgdf["weight"].values)
    return histosig.values(), histobkg.values(),np.sqrt(2*histosig.variances()),np.sqrt(2*histobkg.variances()) ,binning

def getAsimov(params): #x,y,nbins,bin1,binn):
    x,y,nbins,bin1,binn = params
    s, b, sigS, sigB,binning = makeHisto(x,y,nbins,bin1,binn) #, ss, sigB
    #if np.product(s) < 0. or np.product(b) < 0.: return 999
    #if np.min(b) < minYield: return 999
    #sigB = np.sqrt(sigB**2 + (systUnc*b)**2)    #sigB is sigma(b), bad choice of variable name, I know
    #print np.vstack((b,sigB)).T
    #print np.vstack((s/opt.sig,sigS)).T
    if np.any(sigB[1:]/b[1:]>maxerrB):
        #print('Too large background uncertainty')
        # print('bkg unc too high')
        return 999,999
    # if s[-1] < 0.5 or np.any(sigS[-2:]/(s[-2:]/opt.sig) > maxerrS):
    if np.any(sigS[-2:]/(s[-2:]/opt.sig) > maxerrS):
        # print('sig unc too high')
        return 999,999
    #if np.any(sigS[-3:]/s[-3:]>maxerr):
    #    return 999
    if np.any(b <= 1.) or np.any(s<=0):
        # print("bkg <1 or s < 0")
        return 999,999
    #if b[-1]<=0 or sigB[-1]/b[-1]>maxerr: return 999

    #epsilon = np.finfo(float).eps
    # Constructing a liklihood ratio to obtain asimov significance
    # Poisson assumes integer number of events, so need to use rint for asimov dataset
    #posB = poisson.logpmf(np.rint(b), np.rint(b))
    #posSB = poisson.logpmf(np.rint(s+b), np.rint(s+b))
    #posB = poisson.logpmf(np.rint(b), b)
    #posSB = poisson.logpmf(np.rint(s)+np.rint(b), s+b)
    #b = b[s >= 0.5]
    #s = s[s >= 0.5]
    intS = np.rint(s)
    intB = np.rint(b)
    posB = poisson.logpmf(intB, b)
    posSB = poisson.logpmf(intB+intS, b+s)
    #posB = poisson.logpmf(intB, intB)
    #posSB = poisson.logpmf(intB+intS, intB+intS)
    
    #print(posSB)
    #print(posB)
    #As = np.prod(posSB)/np.prod(posB)
    #print((s+b)[-2:], np.rint(s+b)[-2:], b[-2:], np.rint(b)[-2:])
    #print(posSB[-2:], posB[-2])
    #invAs = 2*(np.sum(posSB[-5:]) - np.sum(posB[-5:]))
    invAs = 2*(np.sum(posSB) - np.sum(posB))
    #invAs = 2*np.sum(posSB)
    #As = np.exp(As)
    #print(np.sum(posSB), np.sum(posB), As)
    #if As > 1.: return 999

    #invAs = -2*np.log(As)

    #print samp, s[-1],b[-1],sigB[-1]
    #ss = np.where(s > 0, np.sqrt(s), 1.)
    #sigB = np.where(b > 0, np.sqrt(b), 1.)
    '''
    model = pyhf.simplemodels.hepdata_like(
        signal_data=list([s[1]]), bkg_data=list([b[1]]), bkg_uncerts=list([sigB[1]])
    )
    observations = list((s+b).astype(int))
    print (list(s))
    print (list(b))
    print (list(sigB))
    print (observations)
    data = pyhf.tensorlib.astensor([observations[1]] + model.config.auxdata)
    test_mu = 1.0
    
    CLs_obs, CLs_exp = pyhf.infer.hypotest(
        test_mu, data, model, qtilde=True, return_expected=True
    ) 
    '''
    # term1 = (s+b)*np.log( ((s+b)*(b+np.power(sb,2)))  / ((np.power(b,2)) + (s+b)*np.power(sb,2)) )
    # term2 = (np.power(b,2)/np.power(sb,2)) * np.log(1 + np.power(sb,2)*s / (b*(b+np.power(sb,2)))  )
    # print term1
    # print term2
    # Asig = np.sqrt(2*(term1 - term2))
    #return np.sum(s/np.sqrt(s+b))
    # print epsilon

    #Asig = np.sqrt(2*((s+b)*np.log((s+b)*(b+sigB*sigB)/(b*b+(s+b)*sigB*sigB+epsilon)+epsilon)-b*b*np.log(1+sigB*sigB*s/(b*(b+sigB*sigB)+epsilon))/(sigB*sigB+epsilon))) #Add the epsilon to avoid dividing by 0

    #approxAs = np.sqrt(  2*((s+b)*np.log(1.+s/b)- s )  )

    #print s,b,sigB #s[-1]/(1-binn),b[-1]/(1-binn)

    #As = np.where(np.isnan(Asig),approxAs,Asig)
    #As = s/np.sqrt(b+sigB**2)
    #invAs = -np.sqrt(np.sum(np.nan_to_num(As)**2))
    #print ("test",invAs,CLs_obs, CLs_exp)
    return invAs,binning

#  params = [0.5,1,.1,.9]
# getAsimov(params)

# mn = minimize(getAsimov, params, bounds = [(0,1),(1,50),(0.02,0.4),(0.5,0.98)], method= "SLSQP", options = {'eps': 1e-2})
# print mn

graph = {}
# graph["x"] = np.arange(0,1.,0.1)
# graph["y"] = np.arange(2,5,1)
graph["x"] =  [1.] # np.arange(0.5,1.5,0.1)#[1.]
graph["y"] =  [1.] #np.arange(1,3,1)#[1.]
graph["nbins"] = np.arange(10,61,5)
#graph["bin1"] = np.arange(0.00,0.02,0.01)
#graph["binn"] = np.arange(0.9,1.,0.01)
graph["bin1"]=[0.0]
graph["binn"]=[1.]
# graph["bin1"] = ['deprecated']
# if opt.params == []:
#     params = [1,1,30,1./15,1-1./15]
# else:
#     exec("params = "+opt.params)
# if opt.params != []: sys.exit()
# #

if opt.makecondor:
    condf = open("condorparams.txt",'w')
paramlist = []
vallist = []
minval = 1e5
minout=[]
iparam = []
y=1
for x in graph["x"]:
    if opt.x > 0: x = opt.x
    # for y in graph["y"]:
    #         if opt.y > 0: y = opt.y
    for nbins in graph["nbins"]:
        if opt.nbins > 0: nbins = opt.nbins
        if opt.makecondor:
            for sm in sampchoices:
                condf.write('%s %f %f\n'%(sm,x,y))
        else:
            for nbins in graph["nbins"]:
                for binn in graph["binn"]:
                    bin1 = 0 
                    params = [x,y,nbins,bin1,binn]
                    out = getAsimov(params)
                    paramlist.append(params)
                    vallist.append(out)
                    print(out[0], params)
                    if out[0] < minval:
                        minval = out[0]
                        iparam = params
                        
                        minout=out
                            # lockname = ".lock_%s"%samp
                            # while os.path.isfile(lockname):
                            #     sleep(1)
                            # lockfl = open(lockname,'w')
                            # lockfl.write("Stahp")
                            # lockfl.close()

                            # doUpdate = False
                            # outname = "out_%s.txt"%samp
                            # if os.path.isfile(outname):
                            #     outfl = open(outname,'r')
                            #     bestval = float(outfl.readlines()[0].strip())
                            #     if minval < bestval:
                            #         doUpdate = True
                            # else:
                            #     doUpdate = True

                            # if doUpdate:                                
                            #     outfl = open(outname,'w')
                            #     outfl.write('%f\n'%minval)
                            #     outfl.write(str(params))
                            #     outfl.close()

                            # os.system("rm -f %s"%lockname)

#            if opt.nbins > 0: break 
            # if opt.y > 0: break 
    if opt.x > 0: break

if opt.makecondor:
    condf.close()
    sys.exit(0)

print ("Final result:")
print (minval,np.round(np.array(minout[1]),3), iparam)


# m = Minuit(getAsimov,x=0.5,y=12,nbins=10,bin1=0.1,binn=0.9,
#             error_x=0.5,error_y=1,error_nbins=1,error_bin1=0.1,error_binn=0.1,
#             limit_x=(0.0,1),limit_y=(1,50),limit_nbins=(6,20),limit_bin1=(0.02,0.4),limit_binn=(0.6,0.98))

# m.migrad()  # run optimiser
# print(m.values)
