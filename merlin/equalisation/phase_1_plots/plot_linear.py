#%%
#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


def interpolate(*args, **kwargs):
    return np.interp(args[0], [args[1][0], args[2][0]], [args[1][1], args[2][1]])
    
def main():
    mu_low = 20
    mu_high = 80
    DACDiscL_low = 80
    DACDiscL_high = 120
    p1 = (mu_low, DACDiscL_low)
    p2 = (mu_high, DACDiscL_high)
    x = np.linspace(0,100,1000)
    fit_1 = interpolate(x,p1,p2)
    print(fit_1)
    plt.plot(x,fit_1)
    plt.show()
    

if __name__ == '__main__':
    main()
