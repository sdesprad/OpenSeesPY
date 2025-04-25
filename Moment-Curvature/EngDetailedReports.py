# Engineering Plots
# Date: Feb 13, 2025


import matplotlib.pyplot as plt

import numpy as np
import math
import pandas as pd

def execute(K, moment, EIsecant, c, StrainConfc, StrainConft, StrainUncfc, StrainUncft, StrainRebc, 
            StrainRebt, StressConfc, StressConft, StressUncfc, StressUncft, StressRebc, StressRebt):

    # ----------------------------------------
    # Display Results Table:
    # ----------------------------------------

    ResultMatrix = {'Curvature [mrad/ft]': np.round(K*1000*12,2), 
                    'Moment [k-ft]': moment,
                    'EIsec  [k-ft2]': EIsecant,
                    'c [in]': c,
                    '\u03B5Confc [--]': StrainConfc,
                    '\u03B5Conft [--]': StrainConft,
                    '\u03B5Uncfc [--]': StrainUncfc,
                    '\u03B5Uncft [--]': StrainUncft,
                    '\u03B5Rebc [--]': StrainRebc,
                    '\u03B5Rebt [--]': StrainRebt,
                    '\u03C3Confc [ksi]': StressConfc,
                    '\u03C3Conft [ksi]': StressConft,
                    '\u03C3Uncfc [ksi]': StressUncfc,
                    '\u03C3Uncft [ksi]': StressUncft,
                    '\u03C3Rebc [ksi]': StressRebc,
                    '\u03C3Rebt [ksi]': StressRebt}
    
    df = pd.DataFrame(ResultMatrix, columns = ['Curvature [mrad/ft]', 'Moment [k-ft]', "EIsec  [k-ft2]", 'c [in]', 
                                               '\u03B5Confc [--]', '\u03B5Conft [--]', '\u03B5Uncfc [--]',
                                               '\u03B5Uncft [--]', '\u03B5Rebc [--]', '\u03B5Rebt [--]',
                                               '\u03C3Confc [ksi]', '\u03C3Conft [ksi]', '\u03C3Uncfc [ksi]',
                                               '\u03C3Uncft [ksi]', '\u03C3Rebc [ksi]', '\u03C3Rebt [ksi]'])                  
    
    df['EIsec  [k-ft2]'] = df['EIsec  [k-ft2]'].map('{:,.0f}'.format)
    
    df['\u03B5Confc [--]'] = df['\u03B5Confc [--]'].map('{:.5f}'.format)
    df['\u03B5Conft [--]'] = df['\u03B5Conft [--]'].map('{:.5f}'.format)
    df['\u03B5Uncfc [--]'] = df['\u03B5Uncfc [--]'].map('{:.5f}'.format)
    df['\u03B5Uncft [--]'] = df['\u03B5Uncft [--]'].map('{:.5f}'.format)
    df['\u03B5Rebc [--]'] = df['\u03B5Rebc [--]'].map('{:.5f}'.format)
    df['\u03B5Rebt [--]'] = df['\u03B5Rebt [--]'].map('{:.5f}'.format)
    
    df['\u03C3Confc [ksi]'] = df['\u03C3Confc [ksi]'].map('{:.1f}'.format)
    df['\u03C3Conft [ksi]'] = df['\u03C3Conft [ksi]'].map('{:.1f}'.format)
    df['\u03C3Uncfc [ksi]'] = df['\u03C3Uncfc [ksi]'].map('{:.1f}'.format)
    df['\u03C3Uncft [ksi]'] = df['\u03C3Uncft [ksi]'].map('{:.1f}'.format)
    df['\u03C3Rebc [ksi]'] = df['\u03C3Rebc [ksi]'].map('{:.1f}'.format)
    df['\u03C3Rebt [ksi]'] = df['\u03C3Rebt [ksi]'].map('{:.1f}'.format)
    
    pd.set_option('display.max_rows', None)     # Set to None to display all rows
    pd.set_option('display.max_columns', None)  # Set to None to display all columns
    
    display(df)