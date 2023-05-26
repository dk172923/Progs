graph = eval(input("Enter your graph: "))
node = input("Enter your starting node: ")

def dfs(graph, node):
    visited = set()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour)

print("DFS:")
dfs(graph, node)