import numpy as np

#Basic array creation
arr1 = np.array([1,2,3])
print("Simple array: ",arr1)

#converting already existing list into array
list = [1,2,3,4,5]
arr2 = np.array(list)
print("Array of list: ",arr2)

#creating array with default values
arr_zeros = np.zeros((2,3)) #array of 2 rows and 3 columns with all values as zero will be created
print("Array of zeros: ",arr_zeros)

arr_ones = np.ones((3)) #flatten array of 3 elements with all values as one will be created
print("Array of 1's: ",arr_ones)

arr_value = np.full(4,3) #flatten array of 4 elements with all values as 3 will be created
print("Array of default value 3: ",arr_value)


#creating a sequenced array
arr_sequence = np.arange(1,11,2) #flatten array with numbers 1,3,5.. till 10 will be created


#creating identity matrix
arr_identity = np.eye((4))
print("Identity array: ",arr_identity)
