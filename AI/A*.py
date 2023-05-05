import heapq


def astar_search(start, goal, h):
    global graph, cost
    queue = [(0, start, [])]
    visited = set()

    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == goal:
                return cost, path
            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(
                        queue,
                        (cost + cost[(node, neighbor)] + h[neighbor], neighbor, path),
                    )

    return float("inf"), []


if __name__ == "__main__":
    nodes = int(input("Enter the number of nodes in the graph: "))
    graph, cost = [[] for i in range(nodes)], {}

    answer = "y"
    while answer == "y":
        answer = input("Add an edge by typing y, otherwise n: ")
        if answer.lower() != "y":
            break
        first = int(input("Enter the first node: "))
        second = int(input("Enter the second node: "))
        graph[first].append(second)
        cost_edge = int(input("Enter the cost of the edge: "))
        cost[(first, second)] = cost_edge

    start = int(input("Enter the starting node: "))
    goal = int(input("Enter the goal node: "))

    heuristic = {}
    for i in range(nodes):
        heuristic[i] = int(input("Enter the heuristic for node " + str(i) + ": "))

    cost, path = astar_search(start, goal, heuristic)

    print("Minimum cost from", start, "to", goal, "is:", cost)
