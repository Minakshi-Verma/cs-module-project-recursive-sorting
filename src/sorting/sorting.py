# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    
    # Sorting happens here...
  
    a = 0 #from arrA
    b = 0 #from arrB
    #k from merged_arr

    for k in range(0, elements):
        # start comparisons
        # If a is out of range, push b and iterate.
        if a >= len(arrA):
            # we're done with a, push b
            merged_arr[k] = arrB[b]
            b += 1
            
        # If b is out of range, push a and iterate.
        elif b >= len(arrB):
            merged_arr[k] = arrA[a]
            a += 1
           
        # If a is smaller, but it in array and iterate both.
        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a += 1
            
        # If b is smaller put it in array and iterate both.
        else:          
            merged_arr[k] = arrB[b]
            b += 1
            
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    
    # Your code here
    if len(arr)>1:  #basecase
        
        middle= len(arr)//2    #gives the middle of the array
        left= arr[:middle]  # gives the left side of array
        right= arr[middle:]  #gives the right side of the array
   
        #recursively call merge_sort() on Left array
        L= merge_sort(left)
        #recursively call merge_sort() on Right array        
        R= merge_sort(right)  
       #merge left and right array
        arr = merge(L,R) 
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

