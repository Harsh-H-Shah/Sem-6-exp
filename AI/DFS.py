def dfs(start, goal):
    global graph
    stack = [start]
    visited = set()
    path = []

    while stack:
        current = stack.pop()
        path.append(current)

        if current == goal:
            return path

        visited.add(current)

        print("Open list:", stack)
        print("Closed list:", visited)
        print("Current node:", current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)

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

    path = dfs(start, goal)
    if path:
        print("Path found:", path)
    else:
        print("No path found.")
