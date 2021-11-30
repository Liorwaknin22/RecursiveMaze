def is_valid(board, neighbor, initial_point):  # neighbor[0]=row index, neighbor[1]=col index,
    return 0 <= neighbor[0] < len(board) and 0 <= neighbor[1] < len(board[neighbor[0]]) \
           and board[neighbor[0]][neighbor[1]] != -1 and [neighbor[0], neighbor[1]] > initial_point


def solve_maze_monotonic_rec(board, initial_point, goal_point, solution_path):
    if initial_point == goal_point:  # solution found
        solution_path.append(initial_point)
        return solution_path
    row = initial_point[0]
    col = initial_point[1]
    if is_valid(board, (row + 1, col), initial_point):
        solution_path.append(initial_point)
        solve_maze_monotonic_rec(board, [row + 1, col], goal_point, solution_path)
    elif is_valid(board, (row, col + 1), initial_point):
        solution_path.append(initial_point)
        solve_maze_monotonic_rec(board, [row, col + 1], goal_point, solution_path)
    elif is_valid(board, [row - 1, col], initial_point):
        solution_path.append(initial_point)
        solve_maze_monotonic_rec(board, [row - 1, col], goal_point, solution_path)
    elif is_valid(board, (row, col - 1), initial_point):
        solution_path.append(initial_point)
        solve_maze_monotonic_rec(board, [row, col - 1], goal_point, solution_path)
    else:
        return []


def solve_maze_monotonic(board):
    solution_path = []
    goal_point = [len(board) - 1, len(board[0]) - 1]
    solve_maze_monotonic_rec(board, [0, 0], goal_point, solution_path)
    return solution_path


print(solve_maze_monotonic([[1, 2, 3], [2, 0, 4], [3, 4, 5]]))
print(solve_maze_monotonic([[1, 2, 3], [2, 0, 5], [3, 4, 5]]))
print(solve_maze_monotonic(
    [[1, 2, 3, 4, 5], [12, 11, 10, 4, 6], [13, 9, 9, 8, 7], [14, 9, 9, 8, 7], [15, 16, 17, 18, 19]]))
print(solve_maze_monotonic([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]))
print(solve_maze_monotonic([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 6]]))
print(solve_maze_monotonic([[19]]))
