import numpy as np
arr = np.array([0,5,7,1,9])
encoded_arr = np.zeros((arr.size, arr.max()+1), dtype=int)  #array of all values equal to zero of size range(0,10)
encoded_arr[np.arange(arr.size),arr] = 1    #assigning values of rows and column to 1 acc to values in arr 
print(encoded_arr)


