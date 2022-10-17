#student340

class MinHeap:
    def __init__(self,capacity):
        self.heap = [0]*capacity
        self.capacity = capacity
        self.size = 0

    def insert(self,data):
        if self.isFull():
            raise Exception("Heap is full")
        self.heap[self.size] = data
        self.size += 1
        self.heapifyUp(self.size-1)

    def extractMin(self):
        if self.size == 0:
            raise Exception("Heap is empty")
        data = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.heapifyDown(0)
        self.size -= 1
        return data

    #recursive version of heapifyup
    def heapifyUp(self,index):
        if self.hasParent(index) and self.parent(index)>self.heap[index]:
            self.swap(self.getParentIndex(index),index)
            self.heapifyUp(self.getParentIndex(index))

    #recursive version of heapify down
    def heapifyDown(self,index):
        sm_chld_index = index
        if self.hasLeftChild(index) and self.heap[sm_chld_index]>self.leftChild(index):
            sm_chld_index = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.heap[sm_chld_index]>self.rightChild(index):
                sm_chld_index = self.getRightChildIndex(index)
            if sm_chld_index != index:
                self.swap(index,sm_chld_index)
                self.heapifyDown(sm_chld_index)

    def getParentIndex(self,index):
        return (index-1)//2

    def getLeftChildIndex(self,index):
        return 2*index+1

    def getRightChildIndex(self,index):
        return 2*index+2

    def hasParent(self,index):
        return self.getParentIndex(index)>=0

    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index)<self.size

    def hasRightChild(self,index):
        return self.getRightChildIndex(index)<self.size

    def parent(self,index):
        return self.heap[self.getParentIndex(index)]

    def leftChild(self,index):
        return self.heap[self.getLeftChildIndex(index)]

    def rightChild(self,index):
        return self.heap[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size==self.capacity

    def swap(self,index1,index2):
        tmp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = tmp


def make_graph():
    dic = {}
##    f = open('4.in')
##    _nodes = f.readline().strip().split('; ')
##    _edges = f.readline().strip().split('; ')
    _nodes = input().split('; ')
    _edges = input().split('; ')
    all_nodes = []
    
    for node in _nodes:
        id, weight = node.split(', ')
        all_nodes.append(int(id))
        dic[int(id)] = []

    for edge in _edges:
        s, e, w = edge.split(', ')
        dic[int(s)].append((int(w), int(e), int(s)))
        dic[int(e)].append((int(w), int(s), int(e)))
    return dic


def prims(G, start=0):
    unvisited = list(G.keys())
    visited = []
    total_cost = 0
    MST = []

    unvisited.remove(start)
    visited.append(start)

    heap = G[start]
    heap.sort()
    
    while unvisited:
        (cost, n2, n1) = heap.pop(0)
        new_node = None

        if n1 in unvisited and n2 in visited:
            new_node = n1
            MST.append((cost, n1, n2))

        elif n1 in visited and n2 in unvisited:
            new_node = n2
            MST.append((cost, n1, n2))

        if new_node != None:
            unvisited.remove(new_node)
            visited.append(new_node)
            total_cost += cost

            for node in G[new_node]:
                heap.append(node)
                heap.sort()

    return MST, total_cost


def main():
    G = make_graph()
    mst, total_cost = prims(G, 0)
    mst.sort()
    s = ''
    for edge in mst:
        w, n1, n2 = edge
        if n1<n2:
            s += str(n1)+', '+str(n2) + ', ' + str(w) + '; '
        else:
            s += str(n2)+', '+str(n1) + ', ' + str(w) + '; '
    s = s[:-2]
    print(s+'\n')

main()
