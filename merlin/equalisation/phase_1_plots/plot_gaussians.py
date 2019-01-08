# %%
#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib.mlab as mlab
import math
#import seaborn as sns
import pandas as pd
from scipy.stats import norm

from toolbox.plot.default_style import apply_default_plot_style

apply_default_plot_style()


class Gaus:
    def __init__(self, x, amp: float, mu: float, sigma: float):
        self.x = x
        self.amp = amp
        self.mu = mu
        self.sigma = sigma
        self.y = self.amp/np.sqrt(2*np.pi*self.sigma**2) * \
            np.exp(-(self.x-self.mu)**2/(2*self.sigma**2))

    def equation(self):
        return 'f(x)=amp/sqrt(2 pi sigma^2) exp(-(x-mu)^2/(2 sigma^2))'

    def generate(self):
        self.y = self.amp/np.sqrt(2*np.pi*self.sigma**2) * \
            np.exp(-(self.x-self.mu)**2/(2*self.sigma**2))


def main():

    # Function to be plotted
    xs = [(0,40),(60,100)]
    func_1 = Gaus(np.linspace(xs[0][0], xs[0][1], 1000), amp=150., mu=20., sigma=4.)
    func_2 = Gaus(np.linspace(xs[1][0], xs[1][1], 1000), amp=150., mu=80., sigma=4.)

    # Determine min and max y values from functions
    ys=[(np.amin(func_1.y),np.amax(func_1.y)),(np.amin(func_2.y),np.amax(func_2.y))]

    # Colour scheme
    colors = [[0, 0, 0], [230/255, 159/255, 0], [86/255, 180/255, 233/255], [0, 158/255, 115/255], [213/255, 94/255, 0], [0, 114/255, 178/255]]

    # Set figure size, and assign axis handle to ax
    fig = plt.figure(figsize=(12, 8))
    ax = plt.gca()

    # Plot
    f1h = ax.plot(func_1.x, func_1.y, color=colors[0])
    f2h = ax.plot(func_2.x, func_2.y, color=colors[1])

    # Formatting ax
    ax.set_xlim(np.min(xs)-0.03*np.max(xs), np.max(xs)+np.max(xs)*0.1)
    ax.set_ylim(np.min(ys)-0.05*np.max(ys), np.max(ys)+np.max(ys)*0.25)
    ax.set_xlabel('Summed noise peaks over all pixels [DAC]')
    ax.set_ylabel('Amplitude')
    ax.tick_params(axis='both', which='major', labelsize=18)
    ax.axhline(y=0, color='black', linewidth=1.3, alpha=.7)
    facecolor = (0.9, 0.9, 0.9)  # Default: '#f0f0f0'
    fig.set_facecolor(facecolor)
    ax.set_facecolor(facecolor)

    # Disable spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(bottom="off", left="off")

    # Getting x and y limits for formatting and annotation usage
    xlims = ax.get_xlim()
    ylims = ax.get_ylim()

    # Annotate noise peaks
    func_1.legend = 'Low DACDiscL'
    func_2.legend = 'High DACDiscL'
    # Annotated point set to top of Gaussian
    xy = (func_1.mu, np.amax(func_1.y))
    x_str = xy[0] - (xlims[1]-xlims[0])*0.07
    y_str = xy[1] - (ylims[1]-ylims[0])*0.4  # Offset annotated point by 3%
    xy_str = (x_str, y_str)
    ax.annotate(func_1.legend, xy, xy_str, ha='center', va='bottom',
                color=colors[0], weight='bold', backgroundcolor=facecolor,
                rotation=80)

    # Annotated point set to top of Gaussian
    xy = (func_2.mu, np.amax(func_2.y))
    x_str = xy[0] - (xlims[1]-xlims[0])*0.07
    y_str = xy[1] - (ylims[1]-ylims[0])*0.4  # Offset annotated point by 3%
    xy_str = (x_str, y_str)
    ax.annotate(func_2.legend, xy, xy_str, ha='center', va='bottom',
                color=colors[1], weight='bold', backgroundcolor=facecolor,
                rotation=80)

    # Set title
    main_title = 'Two towers - an alternative story.'
    sub_title = 'Simulated cumulative noise peaks over all pixels of a Merlin detector using a low\nand a high DACDiscL setting respectively.'
    x_centre = (xlims[1]-xlims[0])/2
    y_main = (ylims[1]-ylims[0])*1.10
    y_sub = y_main-(ylims[1]-ylims[0])*0.10
    xy_main_title = (x_centre, y_top)
    ax.text(x_centre, y_main, main_title, fontsize=26,
            weight='bold', alpha=.75, ha='center', va='bottom')
    ax.text(x_centre, y_sub, sub_title, fontsize=19,
            alpha=.85, ha='center', va='bottom')

    # Thesignature bar
    y_bottom_bar = ylims[0] - (ylims[1]-ylims[0])*0.12
    y_bottom_text = y_bottom_bar - (ylims[1]-ylims[0])*0.05
    x_bottom_bar = xlims[0] - (xlims[1]-xlims[0])*0.10
    ax.text(x_bottom_bar, y_bottom_bar,
            s='____________________________________________________________________________________________________________________________',
            color='grey', alpha=.7, ha='left')

    ax.text(x_bottom_bar, y_bottom_text,
            s='         ©Quantum Detectors                                                                                                          Source: dummy data   ',
            fontsize=14, color='grey', alpha=.7, ha='left')

    plt.show()

if __name__ == '__main__':
    main()
