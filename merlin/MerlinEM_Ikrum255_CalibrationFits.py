#!/usr/bin/python3
# Script that runs the CalibrationFits.py 
# Enters settings for MerlinEM calibrations with DACs:
# Preamp = 100
# Shaper = 100
# Ikrum = 255

import sys
sys.path.insert(0, '/Users/richard/merlin/merlin-tcp-calibration/CaliTools')
sys.path.insert(0, '/Users/richard/merlin/merlin-tcp-calibration/inputParams')
import os
from subprocess import PIPE, Popen
import time
from matplotlib import pyplot
path_to_file = '/Users/richard/merlin/merlin-tcp-calibration/CaliTools/CalibrationFits.py'
from numpy import arange

# options is a list of strings with options as asked for when running CalibrationFits.py 
def run_CalibrationFits(options,filepath):
    child_env = os.environ.copy()
    child_env['DONT_SHOW_PLOT'] = '1'
    child = Popen(['python', filepath], stdin=PIPE, env=child_env)
    input='\n'.join(options)+'\n'
    child.communicate(input.encode())

def main():
    

    ChipID_select = ['7']
    # Options 1-24 for metal select
    All_modes     = [str(i+1) for i in arange(24)]
    Cu_SPM        = ['1','3','5','6']
    Zr_SPM        = ['9','15','20','21']
    Ag_SPM        = ['7','8','10','16']
    CSM           = list(set(All_modes)-set(Cu_SPM)-set(Zr_SPM)-set(Ag_SPM))
    Metal_select  = Cu_SPM+Zr_SPM+Ag_SPM + CSM
    Fit_select    = ['1'] #1 for Doublegauss, 2 for single, 3 for singlep, 4 for doublep
    Fit_options   = []
    if '3' in Fit_select or '4' in Fit_select:
        Chip1_options = [
                    '80', # Min DAC
                    '90', # Max DAC
                    '400000', # Norm value
                    '85', # Mean value
                    '3'  # Sigma value 
                ]
        Chip2_options = Chip1_options
        Chip2_offset  = 2
        Chip2_options[0] = str(int(Chip1_options[0])+Chip2_offset)
        Chip2_options[1] = str(int(Chip1_options[1])+Chip2_offset)
        Chip2_options[3] = str(int(Chip1_options[3])+Chip2_offset)
        Chip3_options = Chip1_options
        Chip3_offset  = 2
        Chip3_options[0] = str(int(Chip1_options[0])+Chip3_offset)
        Chip3_options[1] = str(int(Chip1_options[1])+Chip3_offset)
        Chip3_options[3] = str(int(Chip1_options[3])+Chip3_offset)
        Chip4_options = Chip1_options
        Chip4_offset  = 2
        Chip4_options[0] = str(int(Chip1_options[0])+Chip4_offset)
        Chip4_options[1] = str(int(Chip1_options[1])+Chip4_offset)
        Chip4_options[3] = str(int(Chip1_options[3])+Chip4_offset)
        Fit_options = Chip1_options + Chip2_options + Chip3_options + Chip4_options
        print(Fit_options)
        input()
    for metal in Metal_select:
        if metal in Cu_SPM:
            Fit_select = ['2']
        elif metal in Zr_SPM or metal in Ag_SPM:    
            Fit_select = ['1']
        elif metal in CSM:
            Fit_select = ['2']
        opts = ChipID_select + [metal] + Fit_select + Fit_options
        run_CalibrationFits(opts,path_to_file)
    
    

    

if __name__=="__main__":
    main()
