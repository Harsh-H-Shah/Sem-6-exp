import random

GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

MOVES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7],
}


def get_new_state(current_state):
    blank_index = current_state.index(0)
    possible_moves = MOVES[blank_index]
    new_index = random.choice(possible_moves)
    new_state = current_state[:]
    new_state[blank_index], new_state[new_index] = (
        new_state[new_index],
        new_state[blank_index],
    )

    return new_state


def get_heuristic(state):
    misplaced_tiles = sum([1 for i in range(9) if state[i] != GOAL_STATE[i]])

    return misplaced_tiles


def hill_climbing(start_state):
    current_state = start_state
    current_h = get_heuristic(current_state)

    while True:
        print("Current state:", current_state)
        print("Heuristic:", current_h)
        if current_state == GOAL_STATE:
            print("Reached the goal state!")
            return current_state

        best_state = None
        best_h = current_h
        for neighbor in MOVES[current_state.index(0)]:
            new_state = current_state[:]
            new_state[current_state.index(0)], new_state[neighbor] = (
                new_state[neighbor],
                new_state[current_state.index(0)],
            )
            new_h = get_heuristic(new_state)

            if new_h < best_h:
                best_state = new_state
                best_h = new_h

        if best_h >= current_h:
            print("No better move!")
            return current_state

        current_state = best_state
        current_h = best_h


if __name__ == "__main__":
    start_state = []
    print("Enter the initial state (0 for blank space):")
    for i in range(3):
        row = input().split()
        start_state.extend([int(x) for x in row])

    final_state = hill_climbing(start_state)
    print("Final state:", final_state)
    print("Depth:", get_heuristic(final_state))
