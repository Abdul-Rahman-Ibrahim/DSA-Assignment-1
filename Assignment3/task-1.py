#student340

class Node:
    def __init__(self, id, w):
        self.id = id
        self.w = w
        self.cost = float("inf")
        self.parents = []
        self.f = 0
        
class Edge:
    def __init__(self):
        self.edges = {}

    def add_edge(self, node1, node2, weight):
        if node1 in self.edges:
            self.edges[node1].append((node2, weight))
        else:
            self.edges[node1] = [(node2, weight)]

        if node2 in self.edges:
            self.edges[node2].append((node1, weight))
        else:
            self.edges[node2] = [(node1, weight)]


def find_path(start_id, end, e, nodes):
    visited = []
    queue = []
    nodes[start_id].cost = 0+distance(start_id,end)
    queue.append((nodes[start_id].cost, 0, start_id))
    while len(queue) > 0:
        cost, path_so_far, node = queue.pop(0)
        visited.append(node)
        if node == end:
            return
        for neighbour, path_weight in e.edges[node]:
            if neighbour not in visited:
                d = distance(neighbour, end)
                tmp = path_weight + d + path_so_far
                if tmp < nodes[neighbour].cost:
                    nodes[neighbour].cost = tmp
                    queue.append((tmp, tmp-d, neighbour))
                    queue.sort()
            nodes[neighbour].parents.append((cost, node))
            nodes[neighbour].parents.sort()
                

def distance(a, b):
    x1, x2 = a[0], b[0]
    y1, y2 = a[1], b[1]

    return ((x2-x1)**2 + (y2-y1)**2)**(1/2)
           


if __name__=='__main__':
    e = Edge()
    nodes = {}
    n = []

##    f = open('3.in')
##    _nodes = f.readline().strip().split('; ')
##    _edges = f.readline().strip().split('; ')

    _nodes = input().split('; ')
    
    _edges = input().split('; ')

    for node in _nodes:
        x,y,w = node.split(', ')
        nodes[(int(x),int(y))] = Node((int(x),int(y)), int(w))
        n.append((int(w), (int(x),int(y))))

    for ed in _edges:
        x1,y1,x2,y2, w = ed.split(', ')
        e.add_edge((int(x1),int(y1)), (int(x2),int(y2)), int(w))

    n.sort(reverse=True)
    w, start = n[0]
    w, end = n[1]
    find_path(start, end, e, nodes)
    k = end
    path = []
    j = 0
    while nodes[end].cost!=distance(start,k):
        path.append(end)
        if j!=0:
            end = nodes[end].parents[0][1]
        else:
            end = nodes[end].parents[1][1]
        j = 1
    path.append(start)

    s = ''
    for x, y in path[::-1]:
        s+= "{0}, {1}->".format(x,y)
    s = s[:-2] + '\n'
    print(s)

    #f.close()
