# Engineering Plots
# Date: Feb 11, 2025


import matplotlib.pyplot as plt
from PIL import Image

import numpy as np
import math
import pandas as pd

def execute(n_u, r_col, r_core, r_reinf, r_core_int, D_col, es_max, ec_min, 
            StrainUncft, StrainConft, StrainRebt, Strain_int, Straincc,
            StrainRebc, StrainConfc, StrainUncfc):

    fig, ax = plt.subplots()
    image = Image.open('fibsec_rc.png')
    
    v = [-r_col,
         -r_core,
         -r_reinf,
         -r_core_int,
         0,
         r_reinf,
         r_core,
         r_col]
    
    # Major ticks every 20, minor ticks every 5
    major_xticks = np.arange(-1.1*r_col, 1.1*r_col, 1.21*D_col/30)
    major_yticks = np.arange(1.1*ec_min, 1.1*es_max, (es_max - ec_min)/20)
    ax.set_xticks(major_xticks)
    ax.set_yticks(major_yticks)
    plt.xlim(-1.1*r_col, 1.1*r_col)
    plt.ylim(1.10*ec_min, 1.10*es_max)
    
    ax.grid(which='both')
    ax.grid(which='major', alpha=0.5)
    
    for i in range (2, n_u, 5):
        plt.plot(v, 
                 [StrainUncft[i], StrainConft[i], StrainRebt[i], Strain_int[i], Straincc[i], 
                  StrainRebc[i], StrainConfc[i], StrainUncfc[i]],
                  marker = 'o', markersize=2)
    
    current_values = plt.gca().get_xticks()
    plt.gca().set_xticklabels(['{:.0f}'.format(x) for x in current_values])  
    current_values = plt.gca().get_yticks()
    plt.gca().set_yticklabels(['{:,.4f}'.format(x) for x in current_values])
    
    plt.xticks(rotation=90)
    
    plt.xlabel("Ordinate [ in]")
    plt.ylabel("Strain [--]")
    plt.title("Strain Profile for different curvature level")
    
    # Define the position and size parameters
    image_xaxis = 0.6
    image_yaxis = 0.6
    image_width = 0.3
    image_height = 0.3  # Same as width since our logo is a square
    
    # Define the position for the image axes
    ax_image = fig.add_axes( [image_xaxis,
                             image_yaxis,
                             image_width,
                             image_height] )
    
    # Display the image
    ax_image.imshow(image)
    ax_image.axis('off')  # Remove axis of the image
    
    plt.show()