import numpy as np

def strided_matrix(arr, w, s):
    #formula = [((arr length - w)/s)] + 1
    #length-w gives maxx length of rows, then we divide it by strides and add 1 to get number of rows
    rows = (len(arr) - w) // s + 1 #using floor division (//) for getting nearest integer
    #creating a empty array
    res = [] 
    for i in range(rows):
        start = i * s
        end = start + w
        res.append(arr[start:end])
    return np.array(res)


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
w = 4
s = 2
result = strided_matrix(arr, w, s)
print(result)
