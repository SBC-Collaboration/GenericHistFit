import GHF as ghf
import numpy as np

#%% Gaussian
x = np.random.randn((1000))*3 + 7
hist_out = np.histogram(x, bins=1000, range=(5,30))

thisfit = ghf.HistFit(*hist_out)

thisfit.addfun(ghf.GHF_Gaussian(), [100, 7, 3])
trueparams = np.float64([1000/(np.sqrt(2*np.pi)*3), 7, 3])

thisfit.fit()

sigma_off = (thisfit.bestfit - trueparams) / thisfit.bestfit_err
print('*** Gaussian Fit ***')
print('Success:  ' + str(thisfit.fit_out.success))
print('Fit values:  ' + str(thisfit.bestfit))
print('Fit uncertainty:  ' + str(thisfit.bestfit_err))
print('Sigma deviation:  ' + str(sigma_off))
print('Reduced Chi^2:  ' + str(thisfit.chisq_nd))

#%% Exponential with flat background
x = -2*np.log(np.random.random((10000)))
y = 10*np.random.random((1000))
d = np.append(x,y)
hist_out = np.histogram(d, bins=1000, range=(0,10))

thisfit = ghf.HistFit(*hist_out)

thisfit.addfun(ghf.GHF_exp(), [10000, -1])
thisfit.addfun(ghf.GHF_flat(), 500)
trueparams = np.float64([5000, -2, 100])

thisfit.fit()

sigma_off = (thisfit.bestfit - trueparams) / thisfit.bestfit_err
print('*** Exponential with Background ***')
print('Success:  ' + str(thisfit.fit_out.success))
print('Fit values:  ' + str(thisfit.bestfit))
print('Fit uncertainty:  ' + str(thisfit.bestfit_err))
print('Sigma deviation:  ' + str(sigma_off))
print('Reduced Chi^2:  ' + str(thisfit.chisq_nd))

#%% Gaussian with fixed mean
x = np.random.randn((1000)) * 75
hist_out = np.histogram(x, bins=100, range=(-50, 150))

thisfit = ghf.HistFit(*hist_out)

constrained_gaussian = ghf.GHF_Gaussian(mask=[1,0,1],
                                        fixedparams = [0])
thisfit.addfun(constrained_gaussian, [1, 100])
trueparams = np.float64([1000/(np.sqrt(2*np.pi)*75), 75])

thisfit.fit()

sigma_off = (thisfit.bestfit - trueparams) / thisfit.bestfit_err
print('*** Constrained Gaussian ***')
print('Success:  ' + str(thisfit.fit_out.success))
print('Fit values:  ' + str(thisfit.bestfit))
print('Fit uncertainty:  ' + str(thisfit.bestfit_err))
print('Sigma deviation:  ' + str(sigma_off))
print('Reduced Chi^2:  ' + str(thisfit.chisq_nd))
