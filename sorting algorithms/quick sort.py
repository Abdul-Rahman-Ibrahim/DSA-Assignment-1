import random
def partition(arr,low,high):
    p = arr[high]
    i = low
    for j in range(low,high):
        if arr[j]<=p:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1
    tmp = arr[i]
    arr[i] = p
    arr[high] = tmp
    return i

def quick_sort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
            

arr = []
for i in range(10):
    arr.append(random.randint(0,10))
print(arr)
quick_sort(arr,0,len(arr)-1)
print(arr)
