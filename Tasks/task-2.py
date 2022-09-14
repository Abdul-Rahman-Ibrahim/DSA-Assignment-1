#!/usr/bin/env python3
#STUDENT 340
class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time:  int = shipping_time

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j].selection_time+array[j].shipping_time <= pivot.selection_time+pivot.shipping_time:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


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
    quick_sort(orders, 0, len(orders)-1)

    '''
    TODO: Print in stdout the id's of the sorted list (order.id) in one line separated by spaces.
    Terminate with a new line.
            i.e: 1 2 3 4 5 6\n
    '''
    for order in orders:
        print(order.id, end=" ")
    print("\n")
