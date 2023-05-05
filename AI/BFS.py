from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        node, path = queue.popleft()

        if node not in visited:
            visited.add(node)
            print("Open list:", [n for n, _ in queue])
            print("Close list:", list(visited))
            print("Current node:", node)
            print("Current path:", path)

            if node == goal:
                return path + [node]

            for neighbour in graph[node]:
                queue.append((neighbour, path + [node]))

    return None


if __name__ == "__main__":
    nodes = int(input("Enter the number of nodes in the graph: "))
    graph = [[] for i in range(nodes)]

    answer = "y"
    while answer == "y":
        answer = input("Add an edge by typing y, otherwise n: ")
        if answer.lower() != "y":
            break
        first = int(input("Enter the first node: "))
        second = int(input("Enter the second node: "))
        graph[first].append(second)

    start = int(input("Enter the starting node: "))
    goal = int(input("Enter the goal node: "))

    path = bfs(graph, start, goal)
    if path is None:
        print("No path found!")
    else:
        print("Final path:", path)
        print("Depth of the path:", len(path) - 1)
