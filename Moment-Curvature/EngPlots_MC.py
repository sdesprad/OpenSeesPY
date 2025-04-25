# Engineering Plots
# Date: Feb 3, 2025
#

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import numpy as np
import math
import pandas as pd

def execute(Kmax, Mmax, curvature, moment, lab_x, lab_y, plot_title, 
            K1y, Ksp, Kcu_UL, K_Rebc_UL, K_Rebt_UL, Kcu_LL, K_Rebt_LL,
            M1y, Msp, Mcu_UL, M_Rebc_UL, M_Rebt_UL, Mcu_LL, M_Rebt_LL,
            Ky, Ku, Mp, P, r):


    fig, ax = plt.subplots()

    Ydiv = 1000
    Xdiv = 1
    Ymax = math.ceil(1.05*abs(Mmax)/Ydiv)*Ydiv
    Xmax = math.ceil(1.05*abs(Kmax)/Xdiv)*Xdiv
    
    # Major ticks every 20, minor ticks every 5
    major_xticks = np.arange(0, Xmax, Xdiv)
    minor_xticks = np.arange(0, Xmax, Xdiv/5)
    major_yticks = np.arange(0, Ymax, Ydiv)
    minor_yticks = np.arange(0, Ymax, Ydiv/5)

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
    plt.plot([0, Ky, Ku], [0, Mp, Mp], color = 'red')

    # strain limit MC plots
    plt.plot([K1y, K1y], [0, M1y], marker="o", markersize=4, markevery=[1])
    plt.plot([Ksp, Ksp], [0, Msp], marker="o", markersize=4, markevery=[1])
    plt.plot([K_Rebt_UL, K_Rebt_UL], [0, M_Rebt_UL], marker="o", markersize=4, markevery=[1])
    plt.plot([K_Rebt_LL, K_Rebt_LL], [0, M_Rebt_LL], linestyle='--', marker="o",
             markersize=4, markevery=[1])
    
    plt.plot([Kcu_LL, Kcu_LL], [0, Mcu_LL], linestyle='--', color='magenta',
             marker="o",markersize=4, markevery=[1])

    ax.fill_between(curvature, moment, alpha = 0.2)
    message = f"Axial Load = {P} kip\nAxial Ratio = {round(r, 2)}"
    plt.text(4.5, 4000, message, fontsize = 12, bbox=dict(facecolor='white', edgecolor='black'))

    
    plt.legend(["Moment-Curvature", "Idealized", "First Yield", "Cover Spalling", 
                "UL Reinf. Tens. Limit (PL2)", "LL Reinf. Tens. Limit (PL3)", 
                "LL Conc. Compr. Limit (PL3)"], loc='lower center')
    
    plt.xlabel(lab_x)
    plt.ylabel(lab_y)
    plt.title(plot_title)
    current_values = plt.gca().get_yticks()
    plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])
    
    plt.show()
