def dfs(node, depth, max_depth, goal_state, open_list, closed_list, graph):
    if depth > max_depth:
        return None
    open_list.append(node)
    if node == goal_state:
        return node
    for j in graph[node]:
        if j not in closed_list:
            result = dfs(
                j, depth + 1, max_depth, goal_state, open_list, closed_list, graph
            )
            if result is not None:
                return result
    closed_list.append(node)
    return None


def dfid(start_state, goal_state, graph):
    max_depth = 0
    while True:
        open_list = []
        closed_list = []
        result = dfs(
            start_state, 0, max_depth, goal_state, open_list, closed_list, graph
        )
        print(f"Max depth: {max_depth}")
        print(f"Open list: {open_list}")
        print(f"Closed list: {closed_list}")
        if result is not None:
            return result
        max_depth += 1


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

    start_state = int(input("Enter the start state: "))
    goal_state = int(input("Enter the goal state: "))

    path = dfid(start_state, goal_state, graph)
    if path:
        print("Path found:", path)
    else:
        print("No path found.")
