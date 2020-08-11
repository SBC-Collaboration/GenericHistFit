# GenericHistFit
Tool using scipy.optimize.minimize to fit histograms to useful functional forms, with uncertainties on fit parameters reported.

Example usage:
```
import GenericHistFit.GHF as ghf
import numpy as np
x = -2*np.log(np.random.random((10000)))
y = 10*np.random.random((1000))
d = np.append(x,y)
hist_out = np.histogram(d, bins=1000, range=(0,10))

thisfit = ghf.HistFit(*hist_out)

thisfit.addfun(ghf.GHF_exp(), [10000, -1])
thisfit.addfun(ghf.GHF_flat(), 500)

thisfit.fit()

trueparams = np.float64([5000, -2, 100])

sigma_off = (thisfit.bestfit - trueparams) / thisfit.bestfit_err
print('Success:  ' + str(thisfit.fit_out.success))
print('Fit values:  ' + str(thisfit.bestfit))
print('Fit uncertainty:  ' + str(thisfit.bestfit_err))
print('Sigma deviation:  ' + str(sigma_off))
print('Reduced Chi^2:  ' + str(thisfit.chisq_nd))
```
