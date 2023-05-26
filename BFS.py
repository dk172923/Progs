graph = eval(input("Enter your graph: "))
node = input("Enter your starting node: ")
visited = []
queue = []

def bfs( graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("BFS:")
bfs(graph, node)
