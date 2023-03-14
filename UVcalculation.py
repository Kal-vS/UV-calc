
from cgi import test
import numpy as np
import math
import random
from albedocalculation import albedocalc


def UV_calc(time_var = 4, mat_choice = 0):
    '''Takes an input for position of the sun, then calculate the J/m2. Accounts for daily and yearly variation of the sun.
    Also accounts for albedo properties of material of the surface'''
#This cal assumes a a 12-hour periode
# sun constant
    s_const = 137


    days_equinox = 20
    theta = 23.5*math.sin(2*(days_equinox/365.25))
    #print('theta = ',theta)
#Latitude, netherlands is 52
    L = 52

#yearly varaition
    daily_var = s_const*math.cos(L-theta)
    #print('daily var = ',daily_var)

#calculation for daily variation
    
    if time_var == 1:
        E = daily_var*((4.3*104)/math.pi*(1/4))
    elif time_var == 2:
        E = daily_var*((4.3*104)/math.pi*(1/2))
    elif time_var == 3:
        E = daily_var*((4.3*104)/math.pi*(1/4))
    elif time_var == 4:
        E = daily_var*((4.3*104)/math.pi)
    

    # convert E [mj] to E [j]
    E = E*0.001

    albedo = albedocalc(mat_choice)
    E = E - (E*albedo)
    return E


# Test
# UV_calc()

def shadow_calc(grid = 0, facade_height=0, facade_v=0, facade_l=0, facade_h=0, nmbr_columns=0):

    
    
    z = np.where(grid == 1)[0]
    print(z)
    x = nmbr_columns - facade_l

    if (grid[:len(grid)]== 1).any():
        
        # grid = np.select(conds, [target, target], grid)
        if facade_h == 'l':
            for i in range(facade_l):
                for j in range(facade_height):
                    grid[facade_v+i][j+1] = grid[facade_v+i][j+1]*0.5
        else:
            for i in range(facade_l):
                for j in range(facade_height):  
                    grid[facade_v+i][j+x] = grid[facade_v+i][j+x]*0.5

        # for i in range(facade_height):
        #     grid[2][i+1] = grid[2][i+1]*0.5

   
    return grid


