PFS Exposure Time Calculator and Spectrum Simulator 
============================================================

This package is developed by the following people
---------------------------------
The original ETC was developed and written by Christopher Hirata (Ohio State University), which is based on the package developed for WFIRST (C. Hirata; arXiv:1204.5151) and altered for use in PFS project.

The code modification, the python wrapping, and the development of the spectral simulator were mainly done by Kiyoto Yabe, Yuki Moritani, Masato Onodera (Subaru Telescope), Atsushi Shimono (Kavli IPMU) and Robert Lupton (Princeton University).

Modification to work with HERCULES spectrograph was performed by Quin Aicken Davies.

Requirements
------------
* Standard C compiler (e.g., GCC) with OpenMP support
* Python3 is recommended (Python2 is NOT fully supported)
* numpy   (1.20 and higher)  see https://numpy.org/
* pyfits  (3.3 and higher)  see http://www.stsci.edu/institute/software_hardware/pyfits
* matplotlib (if you use the plotting options)
* Sufficient computing power
 (Note1) pyfits is required only for using gen_sim_spec.py and the PFS datamodel package. If you don't have these modules, please install them from the above website. The version of the module is the minimum one that we confirmed so far. If you have any updates, let me know please.
 (Note2) Standard unix system including Linux and Mac OSX is recommended. There has been reported that this code does not work properly on a Linux system mounted on a Windows drive. This package is at least tested under macOS 14.5 on MacBookPro with Apple M3 Pro machine and CentOS7 on AMD EPYC 7542 32-Core Processor machine. Python 3.8.13 and 3.12.3 have been tested.

Installation
------------
To install the package, get the git repository by typing the following command on the terminal (if you have git installed):
  
    git clone --recursive https://github.com/qai11/spt_ExposureTimeCalculator.git
    cd spt_ExposureTimeCalculator
    make
    python setup.py install

Exposure Time Calculator (ETC)
------------------------------
The ETC can be run as follows: Open the Jupyter notebook Labeled 'ETC_ASTR211.ipynb' and run the first three cells of code. 

You will need to update the exposure magnitude. This will allow the exposrue time calculator to correctly estimate signal to noise for your star.
