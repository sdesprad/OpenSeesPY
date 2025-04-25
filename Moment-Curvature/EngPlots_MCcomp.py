# Engineering Plots
# Date: Feb 3, 2025
#

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import numpy as np
import math
import pandas as pd

def execute(Kmax, Mmax, curvature, moment, lab_x, lab_y, plot_title, 
            K_xtract, M_xtract, K_csibridge, M_csibridge):

    plt.figure()

    # Major ticks every 20, minor ticks every 5
    major_xticks = np.arange(0, Kmax, Kmax/10)
    minor_xticks = np.arange(0, Kmax, Kmax/50)
    major_yticks = np.arange(0, Mmax, Mmax/10)
    minor_yticks = np.arange(0, Kmax, Mmax/50)    

    ax = plt.axes()
    ax.set_xticks(major_xticks)
    ax.set_xticks(minor_xticks, minor=True)
    ax.set_yticks(major_yticks)
    ax.set_yticks(minor_yticks, minor=True)

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)
#   ax.fill_between(curvature, moment, alpha = 0.2)

    plt.xlim(0, Kmax)
    plt.ylim(0, Mmax)
    plt.plot(curvature, moment, color = 'mediumblue', marker = 'o', markersize=2)
    plt.plot(K_xtract, M_xtract, color = 'gray', marker = 'o', markersize=2)
    plt.plot(K_csibridge, M_csibridge, color = 'cyan', marker = 'o', markersize=2)
    
    plt.legend(["Moment-Curvature", "XTRACT", "CSIbridge"], loc='lower center')
    
    plt.xlabel(lab_x)
    plt.ylabel(lab_y)
    plt.title(plot_title)
    current_values = plt.gca().get_yticks()
    plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])
    
    plt.show()
