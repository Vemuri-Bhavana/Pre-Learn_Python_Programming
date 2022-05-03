import numpy as np
np_arr=np.array([1,2,3,4])
S=sum(np_arr)
print(S)
np_arr1=np_arr[np_arr>2]
print(np_arr1)
np_arr1=np_arr*2
print(np_arr1)
np_arr1=np_arr[np_arr!=2]
print(np_arr1)
print(np.subtract(23,10))
d_arr=np.array([[1,2,3,4],[5,6,7,8]])
first_arr=d_arr[0]
second_arr=d_arr[1]
third_arr=d_arr[0][0]
fourth_arr=d_arr[:,0] #':' is used to select all rows
fifth_arr=d_arr[:,1:3]  # second ':' is the slicing operation
print(first_arr)
print(second_arr)
print(third_arr)
print(fourth_arr)
print(d_arr.shape)
print(fifth_arr)
