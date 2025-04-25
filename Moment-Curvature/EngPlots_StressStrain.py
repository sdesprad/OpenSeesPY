# Engineering Plots
# Date: Feb 3, 2025


import matplotlib.pyplot as plt

import numpy as np
import math
import pandas as pd

def execute(Legend, e_min, f_min, e_max, f_max, strain_1, stress_1, strain_2, stress_2, 
            lab_x, lab_y, plot_title, 
            ConfStrain_xtract, ConfStress_xtract,UncfStrain_xtract, UncfStress_xtract):

    plt.figure()
    
    # Major ticks every 20, minor ticks every 5
    major_xticks = np.arange(e_min, e_max, (e_max - e_min)/10)
    minor_xticks = np.arange(e_min, e_max, (e_max - e_min)/50)
    major_yticks = np.arange(f_min, f_max, (f_max - f_min)/10)
    minor_yticks = np.arange(f_min, f_max, (f_max - f_min)/50)    

    ax = plt.axes()
    ax.set_xticks(major_xticks)
    ax.set_xticks(minor_xticks, minor=True)
    ax.set_yticks(major_yticks)
    ax.set_yticks(minor_yticks, minor=True)

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)

    plt.xlim(e_min, e_max)
    plt.ylim(f_min, f_max)
    plt.plot(strain_1, stress_1, marker = 'o', markersize=2)
    plt.plot(strain_2, stress_2, marker = 'o', markersize=2)

    plt.plot(ConfStrain_xtract, ConfStress_xtract, color = 'gray')
    plt.plot(UncfStrain_xtract, UncfStress_xtract, color = 'cyan')

    plt.legend(Legend, loc='lower right')    
    
    plt.xlabel(lab_x)
    plt.ylabel(lab_y)
    plt.title(plot_title)
    current_values = plt.gca().get_xticks()
    plt.gca().set_xticklabels(['{:.4f}'.format(x) for x in current_values])  
    current_values = plt.gca().get_yticks()
    plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

    plt.xticks(rotation=90)
    
    plt.show()
