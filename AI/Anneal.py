import random
import math


def annealing(initial_state, get_neighbors, get_cost, temperature, alpha):
    current_state = initial_state
    current_cost = get_cost(current_state)

    while temperature > 0.1:
        neighbor_state = random.choice(get_neighbors(current_state))
        neighbor_cost = get_cost(neighbor_state)
        delta = neighbor_cost - current_cost

        if delta < 0:
            current_state, current_cost = neighbor_state, neighbor_cost
        elif math.exp(-delta / temperature) > random.uniform(0, 1):
            current_state, current_cost = neighbor_state, neighbor_cost

        temperature *= alpha

    return current_state, current_cost


if __name__ == "__main__":
    # get input from user
    initial_state = input("Enter the initial state: ")
    get_neighbors = input("Enter the function to generate neighboring states: ")
    get_cost = input("Enter the function to calculate the cost of a state: ")
    temperature = float(input("Enter the initial temperature: "))
    alpha = float(input("Enter the cooling rate: "))

    # run the annealing algorithm
    final_state, final_cost = annealing(
        initial_state, get_neighbors, get_cost, temperature, alpha
    )

    # print the final solution
    print(f"Final state: {final_state}")
    print(f"Final cost: {final_cost}")
