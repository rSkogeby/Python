import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math
import seaborn as sns


def main():
    
    
    mu1 = 20
    variance1 = 4
    sigma1 = math.sqrt(variance1)
    x1 = np.linspace(mu1 - 3*sigma1, mu1 + 3*sigma1, 100)
    amplitude1 = 150

    mu2 = 80
    variance2 = 4
    sigma2 = math.sqrt(variance2)
    x2 = np.linspace(mu2 - 3*sigma2, mu2 + 3*sigma2, 100)
    amplitude2 = 150
    
    #plt.plot(x1,amplitude1*mlab.normpdf(x1, mu1, sigma1))
    #plt.plot(x2,amplitude1*mlab.normpdf(x2, mu2, sigma2))
    df = sns.load_dataset('iris')

    p1=sns.kdeplot(df['sepal_width'], shade=True, color="r")
    p1=sns.kdeplot(df['sepal_length'], shade=True, color="b")

    # plot of 2 variables
    #p1=sns.kdeplot(x1,amplitude1*mlab.normpdf(x1, mu1, sigma1), shade=True, color="r")
    #p1=sns.kdeplot(x2,amplitude1*mlab.normpdf(x2, mu2, sigma2), shade=True, color="b")
    
    plt.show()

    """ plt.xlim(0,100)
    plt.ylim(0,50)

    plt.xlabel('Summed noise peaks over all pixels [DAC]')
    plt.ylabel('Amplitude')


    plt.show() """

if __name__=='__main__':
    main()