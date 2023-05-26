from queue import PriorityQueue

def aStarAlgo(start_node, stop_node, capacity):
    open_set = PriorityQueue(capacity=capacity)
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node
    
    open_set.put((0, start_node))
    
    while not open_set.empty():
        current_cost, n = open_set.get()
        
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found:', path)
            return path
        
        closed_set.add(n)
        
        if n in Graph_nodes and Graph_nodes[n] is not None:
            for (m, weight) in Graph_nodes[n]:
                new_cost = g[n] + weight
                
                if m not in closed_set:
                    if m not in g or new_cost < g[m]:
                        g[m] = new_cost
                        f = new_cost + heuristic(m)
                        open_set.put((f, m))
                        parents[m] = n
                else:
                    if m in parents and new_cost < g[m]:
                        closed_set.remove(m)
                        g[m] = new_cost
                        f = new_cost + heuristic(m)
                        open_set.put((f, m))
                        parents[m] = n

    print('Path does not exist!')
    return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
    
def heuristic(n):
    H_dist = {'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}
    return H_dist[n]

Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}

capacity = 5  # Set the capacity of the open list

aStarAlgo('A', 'G', capacity)