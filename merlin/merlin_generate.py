#!/usr/bin/python3
# Script that runs the CalibrationFits.py 
# Enters settings for MerlinEM calibrations with DACs:
from merlin_fits_highIkrum import run_CalibrationFits
path_to_file = '/Users/richard/merlin/merlin-tcp-calibration/CaliTools/generateCalibFiles.py'

def main():
    
    ChipID_select = ['7']
    Scan_select   = ['0']
    Opmode_select = ['0','1']
    Gain_select   = ['0','1','2','3']
    Chip1_yes   = ['1']
    Chip2_yes   = ['1']
    Chip3_yes   = ['1']
    Chip4_yes   = ['1']
    # Generate calibration files for all settings
    for opmode in Opmode_select:
        for gain in Gain_select:
            opts = ChipID_select + Scan_select + [opmode] + [gain] + Chip1_yes + Chip2_yes + Chip3_yes + Chip4_yes
            run_CalibrationFits(opts,path_to_file)
    

if __name__=='__main__':
    main()





