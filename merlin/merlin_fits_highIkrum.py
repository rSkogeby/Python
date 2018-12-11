#!/usr/bin/python3
# Python 3 script that runs the CalibrationFits.py 
# Enters settings for MerlinEM calibrations with DACs:
# Preamp = 100
# Shaper = 100
# Ikrum = 255

#import CalibrationFits
import sys
sys.path.insert(0, '/Users/richard/merlin/merlin-tcp-calibration/CaliTools)
sys.path.insert(0, '/Users/richard/merlin/merlin-tcp-calibration/inputParams)
import os
import CalibrationFits

def main():

    print '\n\n\n'
    dictFiles = {}
    with open('/Users/richard/merlin/merlin-tcp-calibration/inputParams/inpars.json') as inputfile:
        dictFiles = json.load(inputfile)
    baseDir= dictFiles['baseDir']


    moduleName, GainMode, OpMode, Target, TotalFilename, chipNames  = GetModule(baseDir)

    print moduleName , "  " , GainMode , "   ", OpMode , "   ", Target, "    " ,TotalFilename, "     ", chipNames


    dictEner =  EnergyDict()
    FitsDict = LoadFitsDict(baseDir, moduleName)

    # auto select of Fitting type
#FunctionType = 'doubleGauss'
#    if Target=='Cu' or OpMode=='CHARGESUMMING':
#        FunctionType = 'singleGauss'

    FunctionType =  selectFitFuction()

    print FunctionType

    # Load Thresold Scan
    dicAu = {}
    with open(TotalFilename) as inputFile:
        data = json.load(inputFile)
        dicAu = data[1]


    print " -- Before Fitting "
    print  FitsDict[OpMode][GainMode][Target]

    # Fitting ---------------------------
    xmins = {}
    xmaxs = {}

    fig = plt.figure('Threshold Scans ')

    # Fitting  and saving -----------------
    CalibrationDict = {}

    for chips in dicAu.keys():              #['Chip1','Chip2','Chip3','Chip4']:
        if chips == 'DACS': continue          # because one of the keys in the Dcitionary is DACS
        plt.plot(dicAu['DACS'],dicAu[chips],DictStyles[chips],label=chips)
        plt.show(block=False)
        fig.canvas.draw()

        popt, lims = fit_scan(dicAu['DACS'],dicAu[chips],FunctionType) #, min = xmins[chips], MAX = xmaxs[chips])

        print " The Fits went well "

        CalibrationDict[chips] = list(popt)

        minimum = lims[0] #CalibrationDict[chips][1] - 2.7*CalibrationDict[chips][2]    #xmins[chips]
        maximum = lims [1] #CalibrationDict[chips][1] + 5* CalibrationDict[chips][2]    #xmins[chips]

            #if minimum < xmins[chips]:
            #minimum =  xmins[chips]

        x = np.linspace(minimum,  maximum,200)
        Yvals = []

        if FunctionType == 'singleGauss' or FunctionType == 'singleGaussP':
            Yvals =gauss_function(x, *popt)
        if FunctionType == 'doubleGauss' or FunctionType == 'doubleGaussP':
            Yvals =Gauss_Zr_fucntion(x, *popt)


        plt.plot(x,Yvals,DictStyles[chips][1],label=chips)
        plt.show(block=False)

    plt.legend()
    plt.savefig(baseDir+'/'+moduleName+'/Plots/scnan_'+OpMode+'_'+Target+'_'+GainMode+'.png')
    fig.canvas.draw()
    plt.show()


    print " -- After Fitting "
    print  CalibrationDict

    FitsDict[OpMode][GainMode][Target] = CalibrationDict


    saveFits(FitsDict, baseDir, moduleName)


if __name__=="__main__":
    main()

#impFile.main()

