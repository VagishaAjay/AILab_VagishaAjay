class Puzzle:
    def __init__(self, board, empty_pos):
        self.board = board
        self.empty_pos = empty_pos

    # Function to move the blank tile in the specified direction
    def move(self, direction):
        x, y = self.empty_pos
        if direction == 'up' and x > 0:
            new_board = [row[:] for row in self.board]  # Create a deep copy of the board
            new_board[x][y], new_board[x-1][y] = new_board[x-1][y], new_board[x][y]  # Swap tiles
            return Puzzle(new_board, (x-1, y))  # Return new puzzle state
        elif direction == 'down' and x < 2:
            new_board = [row[:] for row in self.board]
            new_board[x][y], new_board[x+1][y] = new_board[x+1][y], new_board[x][y]
            return Puzzle(new_board, (x+1, y))
        elif direction == 'left' and y > 0:
            new_board = [row[:] for row in self.board]
            new_board[x][y], new_board[x][y-1] = new_board[x][y-1], new_board[x][y]
            return Puzzle(new_board, (x, y-1))
        elif direction == 'right' and y < 2:
            new_board = [row[:] for row in self.board]
            new_board[x][y], new_board[x][y+1] = new_board[x][y+1], new_board[x][y]
            return Puzzle(new_board, (x, y+1))
        return None


def dfs_using_stack(initial_puzzle, goal):
    stack = [(initial_puzzle, [])]  # Stack stores tuples (puzzle state, path to the current state)
    visited = set()  # To track visited states

    directions = ['up', 'down', 'left', 'right']  # Possible movements of the empty tile (0)

    while stack:
        current_puzzle, path = stack.pop()  # Pop the last puzzle state from the stack

        # Convert the board to a tuple to store in visited set
        board_tuple = tuple(map(tuple, current_puzzle.board))

        # Skip if already visited
        if board_tuple in visited:
            continue

        # Mark current puzzle as visited
        visited.add(board_tuple)

        # Check if we've reached the goal state
        if current_puzzle.board == goal:
            return path + [current_puzzle.board]  # Return the full path leading to the solution

        # Explore possible movements and push resulting states onto the stack
        for direction in directions:
            next_puzzle = current_puzzle.move(direction)
            if next_puzzle and tuple(map(tuple, next_puzzle.board)) not in visited:
                # Add the new state to the stack along with the updated path
                stack.append((next_puzzle, path + [current_puzzle.board]))

    return None  # Return None if no solution is found


# Example usage
initial_board = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]  # 0 is the empty space
goal_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Target goal state

initial_puzzle = Puzzle(initial_board, (1, 1))  # Starting puzzle, empty space at (1, 1)
solution = dfs_using_stack(initial_puzzle, goal_board)  # Run DFS using stack

# Print the solution path if found
if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found")
