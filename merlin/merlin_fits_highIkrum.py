#!/usr/bin/python3
# Script that runs the CalibrationFits.py 
# Enters settings for MerlinEM calibrations with DACs:
# Preamp = 100
# Shaper = 100
# Ikrum = 255

import sys
sys.path.insert(0, '/Users/richard/merlin/merlin-tcp-calibration/CaliTools')
sys.path.insert(0, '/Users/richard/merlin/merlin-tcp-calibration/inputParams')
#sys.path.insert(0, '/Users/richard/analysis/python/merlin')
#import os
#import pexpect
#import subprocess
#import impFile
from subprocess import PIPE, Popen
import time
path_to_file = '/Users/richard/merlin/merlin-tcp-calibration/CaliTools/CalibrationFits.py'

def main():
    child = Popen(['python', path_to_file], stdin=PIPE)
    child.stdin.write(b'7\n')
    child.stdin.write(b'1\n')
    child.stdin.write(b'1\n')
    #print 'Running Merlin script'
    #impFile.main()
    #ChipIDs = 'W548_I5-W548_E4-W548_G3-W548_D3'
    #child = pexpect.spawn('python CalibrationFits.py')

    #child.expect(ChipIDs)
    #child.sendline('7')
    #options = '7\n0'
    #os.system('echo {0}| python CalibrationFits.py',options)
    

    child.communicate()
if __name__=="__main__":
    main()
