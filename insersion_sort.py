#Avijit Saha
#Algorithm and Data Structure
#Assignment 1
#Insersion Sort with Decennding Order


def insersion_sort(arr):    # Defining a function for insersion sort
    for i in range(1, len(arr)):    # Looping from the 2nd element to the last element which is outer loop
        key  = arr[i] # for current element
        j = i - 1 
        while j >= 0 and key > arr[j] :    
             arr[j + 1] = arr[j]   
             j -= 1    #decreasing by 1
        arr[j + 1] = key

arr = [4, 5, 3, 23, 10, 2]    # Decleare the array
insersion_sort(arr)    # Call the function
print("Sorted array in decreasing order:", arr)    #Print the sorted array