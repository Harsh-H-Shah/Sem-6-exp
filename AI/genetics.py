import random


# Function to create an initial population
def create_population(population_size, chromosome_size):
    population = []
    for i in range(population_size):
        chromosome = []
        for j in range(chromosome_size):
            chromosome.append(random.randint(0, 1))
        population.append(chromosome)
    return population


# Function to evaluate the fitness of each chromosome in the population
def evaluate_population(population, fitness_func):
    fitness_values = []
    for chromosome in population:
        fitness_values.append(fitness_func(chromosome))
    return fitness_values


# Function to select the fittest individuals from the population
def selection(population, fitness_values, num_parents):
    parents = []
    for i in range(num_parents):
        max_fitness_index = fitness_values.index(max(fitness_values))
        parents.append(population[max_fitness_index])
        fitness_values[max_fitness_index] = -1
    return parents


# Function to perform crossover between two parents to create a new offspring
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    offspring = parent1[:crossover_point] + parent2[crossover_point:]
    return offspring


# Function to perform mutation on a chromosome
def mutation(chromosome, mutation_probability):
    for i in range(len(chromosome)):
        if random.random() < mutation_probability:
            chromosome[i] = 1 - chromosome[i]
    return chromosome


# Function to evolve the population for a given number of generations
def evolve_population(
    initial_population, fitness_func, num_generations, num_parents, mutation_probability
):
    population = initial_population
    for i in range(num_generations):
        fitness_values = evaluate_population(population, fitness_func)
        parents = selection(population, fitness_values, num_parents)
        offspring_population = []
        for j in range(len(parents) // 2):
            parent1 = parents[j]
            parent2 = parents[len(parents) - 1 - j]
            offspring1 = crossover(parent1, parent2)
            offspring2 = crossover(parent2, parent1)
            offspring_population.append(mutation(offspring1, mutation_probability))
            offspring_population.append(mutation(offspring2, mutation_probability))
        population = offspring_population
    return population


# Example fitness function to maximize the number of 1's in the chromosome
def fitness_function(chromosome):
    return sum(chromosome)


if __name__ == "__main__":
    # Take user inputs
    population_size = int(input("Enter population size: "))
    chromosome_size = int(input("Enter chromosome size: "))
    num_generations = int(input("Enter number of generations: "))
    num_parents = int(input("Enter number of parents selected: "))
    mutation_probability = float(input("Enter mutation probability: "))

    # Create initial population
    initial_population = create_population(population_size, chromosome_size)

    # Evolve the population
    final_population = evolve_population(
        initial_population,
        fitness_function,
        num_generations,
        num_parents,
        mutation_probability,
    )

    # Print the final population and its fitness values
    fitness_values = evaluate_population(final_population, fitness_function)
    for i in range(len(final_population)):
        print(
            "Chromosome {}: {} (Fitness value: {})".format(
                i + 1, final_population[i], fitness_values[i]
            )
        )
