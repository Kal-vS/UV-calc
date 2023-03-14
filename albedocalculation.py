

def albedocalc(mat_choice = 0):
    '''Takes material choice and than returns an albedo value based on material properties'''

    #albedo is defined as the percentage of incoming radiation reflected from a surface
    #Albedo values range from 0, to a perfect absorber (black body), to 1, for perfect reflectors

    #Choose material: as = asphalt, ag = aged pavement, g = grass
    if mat_choice == 'as':
        albedo = 0.05
    elif mat_choice == 'ag':
        albedo = 0.15
    elif mat_choice == 'g':
        albedo = 0.25
    else:
        albedo = 0.31
    
    
   
    return albedo