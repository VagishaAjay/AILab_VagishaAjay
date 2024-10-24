import heapq

# Define the goal state and the initial state for the puzzle
goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Helper functions for A* algorithm
def misplaced_tiles(state, goal_state):
    """Calculate the number of misplaced tiles."""
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count

def manhattan_distance(state, goal_state):
    """Calculate the Manhattan distance heuristic."""
    distance = 0
    # Create a dictionary to map each tile to its goal coordinates
    goal_positions = {goal_state[i][j]: (i, j) for i in range(3) for j in range(3)}
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_x, goal_y = goal_positions[state[i][j]]
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def is_goal(state):
    """Check if the current state is the goal state."""
    return state == goal_state

def get_neighbors(state):
    """Generate neighbors for a given state."""
    neighbors = []
    x, y = [(ix, iy) for ix, row in enumerate(state) for iy, i in enumerate(row) if i == 0][0]
    moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for move_x, move_y in moves:
        if 0 <= move_x < 3 and 0 <= move_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[move_x][move_y] = new_state[move_x][move_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# A* algorithm
def a_star(initial_state, heuristic='misplaced'):
    """A* algorithm implementation for 8-puzzle problem."""
    open_list = []
    closed_set = set()
    
    # Heuristic selector
    if heuristic == 'misplaced':
        h = misplaced_tiles
    elif heuristic == 'manhattan':
        h = manhattan_distance
    
    # Initial cost
    g = 0
    f = g + h(initial_state, goal_state)
    heapq.heappush(open_list, (f, g, initial_state, []))
    
    while open_list:
        f, g, current_state, path = heapq.heappop(open_list)
        if is_goal(current_state):
            return path + [current_state]
        closed_set.add(tuple(map(tuple, current_state)))
        
        for neighbor in get_neighbors(current_state):
            if tuple(map(tuple, neighbor)) in closed_set:
                continue
            new_g = g + 1
            new_f = new_g + h(neighbor, goal_state)
            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [current_state]))
    
    return None

# Helper function to print a state
def print_state(state):
    for row in state:
        print(row)
    print()

# Initial state
initial_state = [[5, 4, 0], [6, 1, 8], [7, 3, 2]]

# Run the A* algorithm with both heuristics
print("Solution using misplaced tiles heuristic:")
solution_misplaced = a_star(initial_state, 'misplaced')
for step in solution_misplaced:
    print_state(step)

print("Solution using Manhattan distance heuristic:")
solution_manhattan = a_star(initial_state, 'manhattan')
for step in solution_manhattan:
    print_state(step)
