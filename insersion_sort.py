#Avijit Saha
#Algorithm and Data Structure
#Assignment 1
#Insersion Sort with Decennding Order


def insersion_sort(arr):    # Defining a function for insersion sort
    for i in range(1, len(arr)):    # Looping from the 2nd element to the last element which is outer loop
        j = i     # for the inner loop to compare the element to the left 
        while arr[j-1] < arr[j] and j > 0 :    # Comparing the left and the right element of the array
             arr[j-1] , arr[j] = arr[j], arr[j-1]    #Swapping with each other 
             j -= 1    #decreasing by 1

arr = [4, 5, 3, 23, 10, 2]    # Decleare the array
insersion_sort(arr)    # Call the function
print(arr)    #Print the sorted array