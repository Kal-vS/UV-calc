import numpy as np

def place_facade(facade_h = 0, facade_v = 0, facade_l=0, nmbr_rows = 0, nmbr_columns=0 ,grid = 0):
    '''Placing the facade in the matrix based on the given horizontal-, vertical position and length'''
    # Lengte van facade aanmaken
    len_arr = np.ones(facade_l)
    


    #Placing zeroes before the facade equal to the begin number
    for i in range(facade_v):
        len_arr = np.insert(len_arr, 0, 0)
    
    #Making the facade size equal to the length of the vertical grid border
    if nmbr_rows > nmbr_columns:
        for i in range(nmbr_rows-len(len_arr)+2):
            len_arr = np.append(len_arr,0)
    else:
        for i in range(nmbr_columns-len(len_arr)+2):
            len_arr = np.append(len_arr,0)


    #Reorienting the facade array to match the vertical border of the grid
    len_arr = np.vstack(len_arr)
    print(grid)
    print(len_arr)

    if facade_h == 'l':
        #places a vertical array along the grid. In this array the facade is represented with 1's
        #Placing the facade on the left if so desired
        grid = np.concatenate((grid,len_arr), axis=1)
        
        grid = np.flip(grid, 1)
        grid = np.delete(grid,1,axis=1)
        
        
    else:
        #placing the facade on the right
        grid = np.concatenate((grid,len_arr), axis=1)
        delete_index = nmbr_columns + 1
        grid = np.delete(grid,delete_index,axis=1)
      
    return grid
   



