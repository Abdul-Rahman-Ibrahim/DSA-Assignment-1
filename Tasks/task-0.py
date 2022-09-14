#!/usr/bin/env python3
#STUDENT 340
class Obj:
    def __init__(self, var: int):
        '''
        Simple constructor
        '''
        self.var: int = var

    def __eq__(self, other: "Obj") -> bool:
        '''
        TODO: ==
        '''
        assert(isinstance(other, Obj))
        if self.var == other.var:
            return 1
        return 0
    
    def __gt__(self, other: "Obj") -> bool:
        '''
        TODO: >
        '''
        assert(isinstance(other, Obj))
        if self.var > other.var:
            return 1
        return 0
        raise NotImplementedError

    def __lt__(self, other: "Obj") -> bool:
        '''
        TODO: <
        '''
        assert(isinstance(other, Obj))
        if self.var < other.var:
            return 1
        return 0
        raise NotImplementedError

    def __le__(self, other: "Obj") -> bool:
        '''
        TODO: <=
        '''
        assert(isinstance(other, Obj))
        if self.var <= other.var:
            return 1
        return 0
        raise NotImplementedError
    
    def __ge__(self, other: "Obj") -> bool:
        '''
        TODO: >=
        '''
        assert(isinstance(other, Obj))
        if self.var >= other.var:
            return 1
        return 0
        raise NotImplementedError

if __name__ == '__main__':

    '''
    Retrieve input
    '''
    data = input()
    left_obj, op, right_obj = data.split(' ')

    '''
    Create Objects
    '''
    left_obj  = Obj(int(left_obj))
    right_obj = Obj(int(right_obj))

    '''
    Perform operations
    '''
    if op == "==":
        print(left_obj == right_obj)
    elif op == ">":
        print(left_obj > right_obj)
    elif op == "<":
        print(left_obj < right_obj)
    elif op == "<=":
        print(left_obj <= right_obj)
    elif op == ">=":
        print(left_obj >= right_obj)
    else:
        raise NotImplementedError
    
