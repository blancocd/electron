## Running and plotting 3D accretion disk simulation with electron heating models on Delta
For a quick overview on the equations that govern the electron heating models and how to manage the parameter file which here is called `parfile.par` go to the repository's README. This document is only concerned on how to run the KHARMA code on the Delta supercomputer and how to plot the resulting dumps.

#### Compiling KHARMA for GPU
To make a clean installation of KHARMA on Delta follow the steps from [KHARMA's repository](https://github.com/AFD-Illinois/kharma). The only change is that instead of running `./make.sh clean cuda` it should be `./make.sh clean hdf5 cuda`.

#### Batch job
Once you have logged in to Delta you can start running the simulation determined by the `parfile.par` file with `sbatch ./delta.sb -i ./parfile.par` or restart a run running `sbatch ./delta.sb -r dumps/torus.out1.xxxxx.rhdf` as you would do in any machine to run KHARMA. You should edit the batch file to specify the directory where KHARMA was compiled.

#### Checking on your job
You can check your job in two ways. First by running `squeue -u yourusername` to see its state, how long it has been running for and the job number. The printed output of your job will be written to `out-numberOfJob.txt`.

#### Ranges for your plots
The `get_vmin.py` and `get_vmax.py` return the 5th percentile of the 5th percentiles and the 99th percentile of the 99th percentiles of each scanned file's specified variable respectively. The first argument then is the variable to be scanned and follows the naming convention as in `parthenon/output0` from the parameter file. The third and optional argument determines the number of files to be scanned, they are evenly spaced, its use is recommended to speed up this process. 

Running the parameter file in this directory I obtained the ranges at `ranges.txt`. I set the ranges of the electron temperature from `5e-05 to 0.8` as shown in `tel.sh` and of the theta electron temperature from `5e-01 to 1400` as shown in `thel.sh`

#### Shell scripts to plot using pyHARM
These scripts are a quick way to use the `pyharm-movie` script which takes all dumps from a specified directory and plots a variable for all the snapshots, thus creating a evolution in time. My shell scripts use it to plot a lot variables that should have a colorbar range in common. I recommend checking the [excellent documentation](https://pyharm.readthedocs.io/en/latest/) of `pyHARM` or at least checking the functionality of `pyharm-movie` with `pyharm-movie --help`.

The scripts take the dumps at `dumps`, save the images to the `frames_w25` directory as the default window is 25 which are square. The values are plotted in log scale, and they plot across the xz plane. 

Lastly, these should not be run using the Delta login nodes in the same way that we had to call `delta.sb` to indicate what computers we wanted to use. In this case, I have used `srun --account=bbhr-delta-cpu --partition=cpu --nodes=1 --tasks=1 --tasks-per-node=1 --cpus-per-task=8 --mem=16g --time=24:00:00 --pty bash` and you may want to increase the memory if you run out of it. Another piece of advice is that these scripts generally take a lot of time so you want to call `tmux` in the login node and then the `srun` command to keep the session alive.


#### A lazy way to put plots side by side
Since the `pyharm-movie` script is so easy to use and I never took the time to understand subplots in matplotlib, the `stitch.py` is the perfect solution to putting images with the same time together as a mosaic. The code is assuming that:
<ul>
    <li> you are calling from a directory which has the directories that contain the images you want to merge </li>
    <li>corresponding images all have the same name across directories</li>
    <li>they are the same resolution</li>
</ul>
These are all true for our use of `pyharm-movie`. 

Now you are ready to make your movies using `ffmpeg`! 