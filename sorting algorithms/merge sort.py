#!/usr/bin/env python3
def merge_sort(orders):
    '''
    TODO: Implement your sorting function and add the parameters you need.
    '''
    if len(orders)>1:
        mid = len(orders)//2
        left = orders[:mid]
        right = orders[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(orders,left,right)

def merge(arr,left,right):
    i,j,k = 0,0,0
    while i<len(left) and j<len(right):
        if left[i].selection_time+left[i].shipping_time<=right[j].selection_time+right[j].shipping_time:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i<len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j<len(right):
        arr[k] = right[j]
        j += 1
        k += 1
