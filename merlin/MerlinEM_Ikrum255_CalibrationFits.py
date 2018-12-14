#!/usr/bin/python3
# Script that runs the CalibrationFits.py 
# Enters options without further human interaction for MerlinX calibrations 
# Preamp = 100
# Shaper = 100
# Ikrum = 255

import sys
import os
from subprocess import PIPE, Popen
import time
from matplotlib import pyplot
from numpy import arange

sys.path.insert(0, '/Users/richard/merlin/merlin-tcp-calibration/CaliTools')
sys.path.insert(0, '/Users/richard/merlin/merlin-tcp-calibration/inputParams')
path_to_file = '/Users/richard/merlin/merlin-tcp-calibration/CaliTools/CalibrationFits.py'

# options is a list of strings with options as asked for when running CalibrationFits.py 
def run_CalibrationFits(options,filepath):
    child_env = os.environ.copy()
    child_env['DONT_SHOW_PLOT'] = '1'
    child = Popen(['python', filepath], stdin=PIPE, env=child_env)
    input='\n'.join(options)+'\n'
    child.communicate(input.encode())

def main():
    
# Single
# 21
# 0-12 except 3
# SPM: 0 5 7 8 9 12
# CSM: 1 2 4 6 10 11
# 
#

    ChipID_select = ['21']
    # Options 1-24 for metal select
    All_modes     = [str(i) for i in arange(13)]
    SPM           = ['0','5','7','8','9','12']
    CSM           = list(set(All_modes)-set(SPM)-set('3'))
    Scan_select   = SPM+CSM
    Fit_select    = ['2'] #1 for Doublegauss, 2 for single, 3 for singlep, 4 for doublep
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
    for scan in Scan_select:
        opts = ChipID_select + [scan] + Fit_select + Fit_options
        run_CalibrationFits(opts,path_to_file)
    

if __name__=="__main__":
    main()
