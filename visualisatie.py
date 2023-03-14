import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from  UVcalculation import UV_calc, shadow_calc
from albedocalculation import albedocalc
from placefacade import place_facade

# this is the starter array. If this doesn't exist then the programm has nothing to add to.
grid = np.array([0,0])

# ask to user to input the dimensions of the street as columns and rows of an array. 
# keep in mind that first and last row are always a list of zero's. This marks the border
nmbr_columns = int(input("number of columns: "))
nmbr_rows = int(input('number of rows: '))
time_var = int(input('Stand van de zon, geef 1,2,3 of 4 (hele zon beweging): '))
mat_choice = input('Choose material: as = asphalt, ag = aged pavement, g = grass: ')
facade_h = input('Place a facade in a column (l or r): ')
facade_v = int(input('Location of facade in rows (begin number): '))
facade_l = int(input('Lenght of facade: '))
facade_height = int(input('Height of the facade: '))

# This creates the top border of the array. 
# A list made from zero's the length of which is determined by the user

for i in range(nmbr_columns):
    gridborder_to_add = np.array([0])
    grid = np.append(grid, gridborder_to_add,0)


# This adds a new list to the array with the actual calculated values. 
# Note that the list always starts with a 0 and ends with a 0, to mark the border



for i in range(nmbr_rows):  
  
    cell_grid = list(0 for i in range(nmbr_columns+2))

    #insert calculated value into the grid with values. Do this for every column 
    for i in range(nmbr_columns):
        #UV_calc is in Joule/m2
        #albedocalc calculates a percentage of 
        cell_value = int(UV_calc(time_var,mat_choice))
        cell_grid = np.insert(cell_grid,i+1,cell_value)
        cell_grid = np.delete(cell_grid,-1)
    # print(grid)
    grid = np.vstack((grid,cell_grid))
else:

    zero_border = list(0 for i in range(nmbr_columns+2))
    grid = np.vstack((grid,zero_border))



grid = place_facade(facade_h, facade_v, facade_l,nmbr_rows,nmbr_columns,grid)
print(grid)

grid = shadow_calc(grid,facade_height,facade_v, facade_l, facade_h, nmbr_columns)
print(grid)
hm = plt.imshow(grid, cmap = 'viridis', interpolation='spline16')


#PLT lay-out

plt.title("UV-straling in J/m^2")
plt.xlabel("Width")
plt.ylabel("Length")
plt.colorbar(hm)



plt.show()