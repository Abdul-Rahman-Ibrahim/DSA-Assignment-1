#!/usr/bin/env python3
#STUDENT 340
class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time:  int = shipping_time

def selection_sort(orders):
    '''
    TODO: Implement your sorting function and add the parameters you need.
    '''
    for i in range(len(orders)):
        min_idx = i
        for j in range(i+1, len(orders)):
            if orders[min_idx].selection_time+orders[min_idx].shipping_time > orders[j].selection_time + orders[j].shipping_time:
                min_idx = j     
        orders[i], orders[min_idx] = orders[min_idx], orders[i]

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
    selection_sort(orders)

    '''
    TODO: Print in stdout the id's of the sorted list (order.id) in one line separated by spaces.
    Terminate with a new line.
            i.e: 1 2 3 4 5 6\n
    '''
    for order in orders:
        print(order.id, end=" ")
    print("\n")
