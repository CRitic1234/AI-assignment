import numpy as np
arr = np.array([0,5,7,1,9])
encoded_arr = np.zeros((arr.size, arr.max()+1), dtype=int)
encoded_arr[np.arange(arr.size),arr] = 1
print(encoded_arr)


