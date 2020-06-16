# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    



    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    
    # Your code here
    if len(arr)>1:
        middle= len(arr)//2    #gives the middle of the array
        arrA= arr[:middle]  # gives the left side of array
        arrB= arr[middle:]  #gives the right side of the array
   
        #recursively call merge_sort() on LHS
        merge_sort(arrA)
        #recursively call merge_sort() on RHS        
        merge_sort(arrB)  
        i = j = k = 0 
        #copy data to temp-arrA and arrB 
        # while i<len(arrA) and j<len(arrB):
        #     if arrA[i]< arrB[j]:
        #         arr[k]<arrA[i]
        #         i+=1
        #     else:
        #         arr[k]= arrB[j]
        #         j+=1
        #     k+=1 
        # #Checking if any element was left
        # while i<len(arrA):
        #     arr[k]= arrA[i]
        #     i+= 1
        #     k+=1
        # #Checking if any element was right
        # while j<len(arrB):
        #     arr[k]= arrB[j]
        #     j+= 1
        #     k+=1        
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

