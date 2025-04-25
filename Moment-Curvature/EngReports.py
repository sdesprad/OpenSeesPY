# Engineering Plots
# Date: Feb 13, 2025


import matplotlib.pyplot as plt

import numpy as np
import math
import pandas as pd

def execute(esp, ecu_UL, esc_UL, est_UL, ecu_LL, est_LL, K1y, Ky, Ksp, 
            Ku, EI_1y, M1y, Mp, Mu, Kcu_UL, K_Rebc_UL, K_Rebt_UL, Kcu_LL, K_Rebt_LL):

    # ----------------------------------------
    # Display Results Table:
    # ----------------------------------------

    RMatrix1 = {'Concrete Spalling Strain, esp [--]': esp, 
                 'Concrete Ultimate Strain, ecu_UL [--]': ecu_UL,
                 'Reinf. buckling Strain, esc_UL [--]': esc_UL,
                 'Reinf. tensile limit Strain, est_UL [--]': est_UL,
                 'LL Unconf. Conc. Comp. Strain Limit, ecu_LL [--]': ecu_LL,
                 'LL Reinf. tensile limit Strain Limit, est_LL [--]': est_LL,
                 'Curvature at First Yield, K1y [--]': K1y,
                 'Effective Yield Curvature, Ky [mrad/ft]': Ky,
                 'Curvature at Cover Spalling, Ksp [--]': Ksp,                 
                 'Ultimate Curvature, Ku [mrad/ft]': Ku,
                 '1st Yield Secant Stiffness, EI_1y [k-ft2]': EI_1y,                
                 '1st Yield Moment, M1y [k-ft]': M1y,
                 'Plastic Moment, Mp [k-ft]': Mp,
                 'Ultimate Moment, Mu [k-ft]': Mu,
                 'UL Curvature for Conf. concrete ultimate strain, Kcu_UL [--]': Kcu_UL,
                 'UL Curvature for Rebar compr. Limit Strain, K_Rebc_UL [--]': K_Rebc_UL,
                 'UL Curvature for Rebar compr. Limit Strain, K_Rebt_UL [--]': K_Rebt_UL,
                 'LL Curvature for Unconf. Concr. compr. Limit Strain, Kcu_LL [--]': Kcu_LL,
                 'LL Curvature for Rebar Tens. Limit Strain, K_Rebt_LL [--]': K_Rebt_LL}

    df1 = pd.DataFrame(RMatrix1, columns = ['Concrete Spalling Strain, esp [--]',
                                        'Concrete Ultimate Strain, ecu_UL [--]', 
                                        'Reinf. buckling Strain, esc_UL [--]', 
                                        'Reinf. tensile limit Strain, est_UL [--]', 
                                        'LL Unconf. Conc. Comp. Strain Limit, ecu_LL [--]', 
                                        'LL Reinf. tensile limit Strain Limit, est_LL [--]',
                                        'Curvature at First Yield, K1y [--]', 
                                        'Effective Yield Curvature, Ky [mrad/ft]',
                                        'Curvature at Cover Spalling, Ksp [--]',                                             
                                        'Ultimate Curvature, Ku [mrad/ft]',
                                        '1st Yield Secant Stiffness, EI_1y [k-ft2]',                                            
                                        '1st Yield Moment, M1y [k-ft]',
                                        'Plastic Moment, Mp [k-ft]',
                                        'Ultimate Moment, Mu [k-ft]',
                                        'UL Curvature for Conf. concrete ultimate strain, Kcu_UL [--]',
                                        'UL Curvature for Rebar compr. Limit Strain, K_Rebc_UL [--]',
                                        'UL Curvature for Rebar tension Limit Strain, K_Rebt_UL [--]',
                                        'LL Curvature for Unconf. Concr. compr. Limit Strain, Kcu_LL [--]',
                                        'LL Curvature for Rebar Tens. Limit Strain, K_Rebt_LL [--]'], index=[0])

    df1['Concrete Spalling Strain, esp [--]'] = df1['Concrete Spalling Strain, esp [--]'].map('{:.4f}'.format)
    df1['Concrete Ultimate Strain, ecu_UL [--]'] = df1['Concrete Ultimate Strain, ecu_UL [--]'].map('{:.4f}'.format)
    df1['Reinf. buckling Strain, esc_UL [--]'] = df1['Reinf. buckling Strain, esc_UL [--]'].map('{:.4f}'.format)
    df1['Reinf. tensile limit Strain, est_UL [--]'] = df1['Reinf. tensile limit Strain, est_UL [--]'].map('{:.4f}'.format)
    df1['LL Unconf. Conc. Comp. Strain Limit, ecu_LL [--]'] = df1['LL Unconf. Conc. Comp. Strain Limit, ecu_LL [--]'].map('{:.4f}'.format)
    df1['LL Reinf. tensile limit Strain Limit, est_LL [--]'] = df1['LL Reinf. tensile limit Strain Limit, est_LL [--]'].map('{:.4f}'.format)
    
    df1['1st Yield Secant Stiffness, EI_1y [k-ft2]'] = df1['1st Yield Secant Stiffness, EI_1y [k-ft2]'].map('{:,.0f}'.format)
    
    #pd.options.display.float_format = '{:.4f}'.format
    #pd.set_option('display.max_rows', None)     # Set to None to display all rows
    #pd.set_option('display.max_columns', None)  # Set to None to display all columns
    
    df1_transposed = df1.T
    
    #left_aligned_df = df1_transposed.style.set_properties(**{'text-align': 'left'})
    display(df1_transposed)