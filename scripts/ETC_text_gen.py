"""
Filename: ETC_text_gen.py
Author: Quin Aicken Davies
Date Created: 2025-07-27
Description: File to generate the defaults files for both the exposure time calculator and the spectrum generator.
Version: 0.1
"""

#%%
import os
import numpy as np

def generate_ETC_defaults(seeing=0.8,zenith_angle=45.00,moon_zenith_angle=30.0,moon_target_angle=60.0,
                          moon_phase=0,exp_time=450,mag_file=22.5,galactic_extinction=0.00,exp_num=8,field_angle=0.675,reff=0.3,line_flux=1.0e-17,line_width=70):
    """
    Generates the ETC defaults file. Defaults defined in the input. 
    """
    # Check if the output directory exists, if not create it
    if not os.path.exists('run_etc.defaults'):
        os.makedirs('run_etc.defaults')

    # Write to the defaults file
    with open(os.path.join('run_etc.defaults'), 'w') as f:
        f.write(f"""
    ########################
    ## PFS ETC Parameters ##
    ########################

    SEEING           {seeing}               #  Seeing FWHM size             [arcsec]
    ZENITH_ANG       {zenith_angle}              #  Zenith angle                 [deg.]
    GALACTIC_EXT     {galactic_extinction}               #  Galactic extinction          [ABmag.]
    MOON_ZENITH_ANG  {moon_zenith_angle}               #  Moon zenith angle            [deg.]
    MOON_TARGET_ANG  {moon_target_angle}               #  Moon-target separation       [deg.]
    MOON_PHASE       {moon_phase}                  #  Moon phase                   [0=New,0.25=quarter,0.5=full]
    EXP_TIME         {exp_time}                #  Single exposure time         [sec.]
    EXP_NUM          {exp_num}                  #  The number of exposures
    FIELD_ANG        {field_angle}              #  Field angle                  [deg.; center=0, edge=0.675]

    MAG_FILE         {mag_file}               #  Magnitude or input spectrum  [ABmag] or <filename>
    REFF             {reff}                #  Effective radius             [arcsec]
    LINE_FLUX        {line_flux}            #  Emission line flux           [erg/s/cm^2]
    LINE_WIDTH       {line_width}                #  Emission line width sigma    [km/s]

    NOISE_REUSED     N                  #  Noise Vector Reused?               [Y/N] (If Y, please specify file name used in OUTFILE_NOISE)
    OUTFILE_NOISE    out/ref.noise.dat  #  Output file for noise vector       <filename>
    OUTFILE_SNC      out/ref.snc.dat    #  Output file for continuum S/N      <filename>
    OUTFILE_SNL      out/ref.snl.dat    #  Output file for emission line S/N  <filename>
    OUTFILE_OII      -                  #  Output file for [OII] doublet S/N  <filename>
    MR_MODE          N                  #  Medium resolution mode switch      [Y/N]
    OVERWRITE        Y                  #  Overwrite switch                   [Y/N]
    """)
    print("ETC defaults file generated: etc_defaults.txt")
    
    
def generate_spectrum_defaults(exp_num=8,mag_file=22.5,count_min=0.8):
    """Once the ETC has found the correct exposure time then generate the spectrum for further analysis if required."""
    # Check if the output directory exists, if not create it
    if not os.path.exists('gen_sim_spec.defaults'):
        os.makedirs('gen_sim_spec.defaults')
    # Write to the defaults file
    with open(os.path.join('gen_sim_spec.defaults'), 'w') as f:
        f.write(f"""
    #########################
    ## Spectral Simulation ##
    #########################
    EXP_NUM          {exp_num}                  #  The number of exposures
    MAG_FILE         {mag_file}               #  Magnitude or input spectrum  [ABmag] or <filename> #Can also be the filename of a already recorded specturm
    countsMin        {count_min}                #  Minimum counts per pixel when calculating noise

    etcFile          out/ref.snc.dat    #  Input noise file for the simulator (from Chris Hirata's ETC)
    nrealize         1                  #  The number of realization
    outDir           out                #  Output directory
    asciiTable       None               #  Output ASCII table name without extension ("None" to omit writing table)
    tract            0                  #  Tract
    patch            0,0                #  Patch
    visit0           1                  #  Visit number
    catId            0                  #  Catalogue ID
    objId            1                  #  Object ID
    spectrograph     1                  #  The spectrograph that we are simulating (1-4)

    writeFits        t                  # If present, this keyword suppresses writing fits files
    """)
    print("Spectrum defaults file generated: spectrum_defaults.txt")
    
