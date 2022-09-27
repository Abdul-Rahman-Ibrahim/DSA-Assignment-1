#merge sort
def merge_sort(array):
    if len(array)>1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        
        merge_sort(left)
        merge_sort(right)
        merge(array,left,right)

def merge(array,left,right):
    i,j,k = 0,0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i<len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j<len(right):
        array[k] = right[j]
        j += 1
        k += 1
##test
array = [9,2,3,9,4,1,0,3,78,9,7]
x = array.copy()
merge_sort(array)
x.sort()
print(array==x)
