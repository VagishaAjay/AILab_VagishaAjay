import random

def initial_state(size):
    return [random.randint(0, size-1) for _ in range(size)]
    # Create a random initial state for the chess problem

def compute_attacks(state):
    attacks = 0
    size = len(state)
    for i in range(size):
        for j in range(i + 1, size):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                attacks += 1
    return attacks
    # Create a function which calculates the conflicts in the game

def heuristic(state):
    return -compute_attacks(state)
    # Our heuristic is going to be -conflicts since we want to minimize the "attacks" of the queens

def hill_climbing(size, max_iter=1000):
    current_state = initial_state(size)
    for iteration in range(max_iter):
        if compute_attacks(current_state) == 0:
            return current_state  # Found a solution
       
        neighbors = []
        for col in range(size):
            for row in range(size):
                if row != current_state[col]:
                    neighbor = list(current_state)
                    neighbor[col] = row
                    neighbors.append(neighbor)
       
        best_neighbor = max(neighbors, key=heuristic)
        if heuristic(best_neighbor) <= heuristic(current_state):
            return current_state  # Local minimum, return current state
       
        current_state = best_neighbor
       
        # Print cost value (conflicts) for each queen
        print(f"Iteration {iteration + 1}: State: {current_state} - Attacks: {compute_attacks(current_state)}")
        for i in range(size):
            queen_cost = sum(
                1 for j in range(size) if (i != j and (current_state[i] == current_state[j] or abs(current_state[i] - current_state[j]) == abs(i - j)))
            )
            print(f"Queen {i} at position {current_state[i]} has {queen_cost} conflicts.")
   
    return None  # Failed to find a solution within max iterations

def print_board(state):
    size = len(state)
    for row in range(size):
        print(" ".join("Q" if state[row] == col else "-" for col in range(size)))
    # Function to visualize the results in the board

solution = hill_climbing(4)
if solution:
    print("Solution found:")
    print_board(solution)
else:
    print("Failed to find a solution within the maximum number of iterations.")
