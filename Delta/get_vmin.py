import multiprocessing
import numpy as np
import glob
import psutil
import sys
import pyharm

def min_limit(n):
    n = n + 1
    fn = dump_path+"torus.out0."+f"{int(n*multiplier):05}"+".phdf"
    var_dump = pyharm.load_dump(fn)[var]
    return np.nanpercentile(var_dump, 5)

if __name__ == "__main__":
    dump_path = "./dumps/"
    nthreads,nfiles,var=psutil.cpu_count(),len(glob.glob1(dump_path,"*.phdf"))-2,sys.argv[1]
    nsamples = nfiles
    if (len(sys.argv)==3 and int(sys.argv[2])<=nfiles):
        nsamples = int(sys.argv[2])
    multiplier = nfiles//nsamples

    with multiprocessing.Pool(nthreads) as pool:
        mins = list(pool.imap_unordered(min_limit, range(nsamples)))
        print(np.nanpercentile(mins, 5))