columns = int(input("Enter number of columns: ")) 
rows = int(input("Enter number of rows: "))
bombs= eval(input("Enter bomb location, sample: [[0,0],[1,1]] : "))

    
import time 
import numpy as np

start_time = time.time()
    
list2 = np.zeros((rows,columns))


for mines in bombs:
    i= mines[0]
    j= mines[1]

    check_points = [[i-1, j], [i+1, j], [i , j+1], [i , j-1], [i-1, j+1], [i+1, j+1], [i+1, j-1], [i-1, j-1]]

    for column in check_points:
        if column[0]>=0 and column[0] < rows and column[1]>=0 and column[1] < columns:
            list2[column[0]][column[1]]+=1

for i in bombs:
    list2[i[0]][i[1]] = -1
        

print(list2)
print(time.time()- start_time)
