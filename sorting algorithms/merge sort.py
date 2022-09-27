#!/usr/bin/env python3

class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time:  int = shipping_time


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

if __name__ == '__main__':
    '''
    Retrieves and splits the input
    '''
    data = input()
    data = data.split('; ')
    orders = []
    for d in data:
        id, selection_t, shipping_t = d.split(', ', 2)
        order: Order = Order(int(id), int(selection_t), int(shipping_t))
        '''
        TODO: Append the `order` object to your structure.
        '''
        orders.append(order)
    
    '''
    TODO: Call your sorting function
    '''
    merge_sort(orders)

    '''
    TODO: Print in stdout the id's of the sorted list (order.id) in one line separated by spaces.
    Terminate with a new line.
            i.e: 1 2 3 4 5 6\n
    '''
    for order in orders:
        print(order.id, end=" ")
    print("\n")
