# GenericHistFit
Tool using scipy.optimize.minimize to fit histograms to useful functional forms, with uncertainties on fit parameters reported.

Features include simple expansion to user-defined functional forms, ability to freeze parameters and apply priors, ability to create arbitrary combinations of distributions, hessian and gradient functions created and passed to scipy.optimize.minimize by default, ...

See `examples.py` for usage

## Installing the package

### Option 1: Cloning repository and install via pip
First, clone the repository:
```
git clone git@github.com:cericdahl/GenericHistFit.git
```

Move into the repository and install the package:
```
cd GenericHistFit
pip install -e .
```
Note that this installs the package in "editable" mode, meaning you can make changes to the source code that will be reflected each time you run the code.

Once the package has been installed in this way, you can `import` this package into your python scripts in any directory:
```
import GenericHistFit.GHF as ghf
```