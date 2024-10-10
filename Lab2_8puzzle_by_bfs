from collections import deque

def bfs(puzzle, goal):
    queue = deque([(puzzle, [])])
    visited = set()
    visited.add(tuple(map(tuple, puzzle.board)))

    directions = ['up', 'down', 'left', 'right']

    while queue:
        current_puzzle, path = queue.popleft()

        if current_puzzle.board == goal:
            return path + [current_puzzle.board]

        for direction in directions:
            next_puzzle = current_puzzle.move(direction)
            if next_puzzle and tuple(map(tuple, next_puzzle.board)) not in visited:
                visited.add(tuple(map(tuple, next_puzzle.board)))
                queue.append((next_puzzle, path + [current_puzzle.board]))
    
    return None

# Example usage
initial_board = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]  # 0 is the empty space
goal_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

initial_puzzle = Puzzle(initial_board, (1, 1))  # Empty position at (1, 1)
solution = bfs(initial_puzzle, goal_board)
for step in solution:
    for row in step:
        print(row)
    print()
