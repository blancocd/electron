## Electron Heating in KHARMA
#### Quick recap
This is a quick recap on the work I did during my last months at Charles Gammie’s Astrophysical Fluid Dynamics group. Thanks to Charles, Vedant, Ben, and everyone in the group who helped me navigate through these amazing simulations and its code!

It all starts with the following paper by Sean Ressler et al. which leverages the unavoidable numerical errors of the plasma evolution by treating them as the dissipation of energy in the plasma: [Electron Thermodynamics in GRMHD Simulations of Low-Luminosity Black Hole Accretion](https://arxiv.org/pdf/1509.04717.pdf).

[KHARMA](https://github.com/AFD-Illinois/kharma) implements their equation 27 in `electrons.cpp` which describes the heating update to the electrons: 
$\kappa_{n+1}^e = \hat{\kappa}_{n+1}^e + \frac{\gamma_e - 1}{\gamma - 1} \left(\rho^{\gamma - \gamma_e} f_e\right)^{n+1/2} (\kappa_g - \hat{\kappa}_g)^{n+1}$
The second term is dissipation, the hat variables are entropy conserving, and the other ones are energy conserving. The $f_e$ term is the fraction of heating from the gas that the electrons receive. 

These ratios can be dependent on the density, magnetic field, internal energy, and any other variables in the simulation. Plasma physicists come up with electron heating models that describe relevant phenomena and their effect on the electron heating ratio $f_e$. We care about the heating of electrons as it can be used to image black hole accretion systems with [ipole](https://github.com/AFD-Illinois/ipole).

#### Running
In a KHARMA run, the electron heating models can be enabled in the parameter file of the simulation to be run as follows:
```
<electrons>
on = true
constant = true
fel_constant = 0.5
sharma = true
gamma_e = 1.333333
```
Here we have enabled electrons, enabled the constant $f_e$ model to 0.5, enabled Sharma’s model, and set the adiabatic constant of the electrons to 4/3. Once enabled, we also need to tell KHARMA to output the heating models entropy $\kappa$ and other variables:
```
<parthenon/output0>
file_type = hdf5
dt = 5.
single_precision_output = true
variables = prims.rho, prims.u, prims.uvec, prims.B, &
prims.Ktot, prims.Kel_Constant, prims.Kel_Sharma
```
Here we specify the dumps `<parthenon/output0>` to have a hdf5 format, output every 5 time code units, the output to be single precision at 32 bits including density, internal energy, velocity, magnetic field, total entropy of the gas, entropy of the electrons with a constant ratio, and entropy of the electrons using Sharma’s model. The `&` is a line break to tell KHARMA that we should consider the following line as a continuation of the current line.

