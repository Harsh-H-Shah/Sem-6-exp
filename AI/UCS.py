def uniform_cost_search(goal, start):
    global graph, costs
    answer = []
    queue = []

    for i in range(len(goal)):
        answer.append(10**8)

    queue.append([0, start])
    visited = {}
    closed = []

    count = 0

    while len(queue) > 0:
        queue = sorted(queue)
        p = queue[-1]
        del queue[-1]
        p[0] *= -1

        if p[1] in goal:
            index = goal.index(p[1])
            if answer[index] == 10**8:
                count += 1
            if answer[index] > p[0]:
                answer[index] = p[0]
            del queue[-1]

            queue = sorted(queue)
            if count == len(goal):
                return answer

        if p[1] not in visited:
            closed.append(p[1])
            for i in range(len(graph[p[1]])):
                queue.append(
                    [(p[0] + costs[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]]
                )

        visited[p[1]] = 1

        # Print the open and closed lists
        print(f"Open list: {queue}")
        print(f"Closed list: {closed}")
        print("-" * 50)

    return answer


if __name__ == "__main__":
    nodes = int(input("Enter the number of nodes in the graph: "))
    graph, costs = [[] for i in range(nodes)], {}

    answer = "y"
    while answer == "y":
        answer = input("Add an edge by typing y, otherwise n: ")
        if answer.lower() != "y":
            break
        first = int(input("Enter the first node: "))
        second = int(input("Enter the second node: "))
        graph[first].append(second)
        cost = int(input("Enter the cost of the edge: "))
        costs[(first, second)] = cost

    start = int(input("Enter the starting node: "))
    goal = []
    num_goals = int(input("Enter the number of goal nodes: "))
    for i in range(num_goals):
        goal_node = int(input("Enter the goal node: "))
        goal.append(goal_node)

    answer = uniform_cost_search(goal, start)
    print(f"Minimum cost from {start} to {goal} is: {answer[0]}")
