#!/usr/bin/env python3
#STUDENT 340
class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time:  int = shipping_time

def sort(orders):
    '''
    TODO: Implement your sorting function and add the parameters you need.
    '''
    
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * (n1)
        R = [0] * (n2)

        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        i = 0	 
        j = 0	 
        k = l

        while i < n1 and j < n2:
            if L[i].selection_time + L[i].shipping_time <= R[j].selection_time + R[j].shipping_time:
                    arr[k] = L[i]
                    i += 1
            else:
                    arr[k] = R[j]
                    j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def mergeSort(arr, l, r):
        if l < r:
            m = l+(r-l)//2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)

    n = len(orders)
    mergeSort(orders, 0, n-1)


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
    sort(orders)

    '''
    TODO: Print in stdout the id's of the sorted list (order.id) in one line separated by spaces.
    Terminate with a new line.
            i.e: 1 2 3 4 5 6\n
    '''
    for order in orders:
        print(order.id, end=" ")
    print("\n")
