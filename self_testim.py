# def is_valid(board, neighbor, initial_point):  # neighbor[0]=row index, neighbor[1]=col index,
#     return 0 <= neighbor[0] < len(board) and 0 <= neighbor[1] < len(board[neighbor[0]]) \
#            and board[neighbor[0]][neighbor[1]] is not None and \
#            board[neighbor[0]][neighbor[1]] > board[initial_point[0]][initial_point[1]]
#
#
# def solve_maze_monotonic_rec(board, current_point, goal_point, solution_path):
#     if current_point == goal_point:  # solution found
#         solution_path.append(current_point)
#         return solution_path
#     row = current_point[0]
#     col = current_point[1]
#     if is_valid(board, [row, col + 1], current_point):
#         solution_path.append(current_point)
#         board[current_point[0]][current_point[1]] = None
#         solve_maze_monotonic_rec(board, [row, col + 1], goal_point, solution_path)
#     elif is_valid(board, [row + 1, col], current_point):
#         solution_path.append(current_point)
#         board[current_point[0]][current_point[1]] = None
#         solve_maze_monotonic_rec(board, [row + 1, col], goal_point, solution_path)
#     elif is_valid(board, [row, col - 1], current_point):
#         solution_path.append(current_point)
#         board[current_point[0]][current_point[1]] = None
#         solve_maze_monotonic_rec(board, [row, col - 1], goal_point, solution_path)
#     elif is_valid(board, [row - 1, col], current_point):
#         solution_path.append(current_point)
#         board[current_point[0]][current_point[1]] = None
#         solve_maze_monotonic_rec(board, [row - 1, col], goal_point, solution_path)
#     else:
#         return []
#
#
# def solve_maze_monotonic(board):
#     solution_path = []
#     goal_point = [len(board) - 1, len(board[0]) - 1]
#     solve_maze_monotonic_rec(board, [0, 0], goal_point, solution_path)
#     return solution_path


# print(solve_maze_monotonic([[1, 2, 3], [2, 0, 4], [3, 4, 5]]))
# print(solve_maze_monotonic([[1, 2, 3], [2, 0, 5], [3, 4, 5]]))
# print(solve_maze_monotonic(
#     [[1, 2, 3, 4, 5], [12, 11, 10, 4, 6], [13, 9, 9, 8, 7], [14, 9, 9, 8, 7], [15, 16, 17, 18, 19]]))
# print(solve_maze_monotonic([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]))
# print(solve_maze_monotonic([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 6]]))
# print(solve_maze_monotonic([[19]]))
# board[neighbor[0]][neighbor[1]] is not None and
# board[current_point[0]][current_point[1]] = None

def is_valid(board, neighbor, initial_point):  # neighbor[0]=row index, neighbor[1]=col index,
    return 0 <= neighbor[0] < len(board) and 0 <= neighbor[1] < len(board[neighbor[0]]) \
           and board[neighbor[0]][neighbor[1]] > board[initial_point[0]][initial_point[1]]


def solve_maze_monotonic_rec(board, current_point, goal_point, solution_path):
    if current_point == goal_point:  # solution found
        solution_path.append(current_point)
        return solution_path
    row = current_point[0]
    col = current_point[1]
    if is_valid(board, [row, col + 1], current_point) and solve_maze_monotonic_rec(board, [row, col + 1], goal_point, solution_path):
        solution_path1 = solution_path.copy()
        solution_path1.append(current_point)
    elif is_valid(board, [row + 1, col], current_point) and solve_maze_monotonic_rec(board, [row + 1, col], goal_point, solution_path):
        solution_path2 = solution_path.copy()
        solution_path2.append(current_point)
    elif is_valid(board, [row, col - 1], current_point) and solve_maze_monotonic_rec(board, [row, col - 1], goal_point, solution_path):
        solution_path3 = solution_path.copy()
        solution_path3.append(current_point)
    elif is_valid(board, [row - 1, col], current_point) and solve_maze_monotonic_rec(board, [row - 1, col], goal_point, solution_path):
        solution_path4 = solution_path.copy()
        solution_path4.append(current_point)
    else:
        return []


def solve_maze_monotonic(board):
    solution_path = []
    goal_point = [len(board) - 1, len(board[0]) - 1]
    solve_maze_monotonic_rec(board, [0, 0], goal_point, solution_path)
    return solution_path


print(solve_maze_monotonic([[1, 5, 2], [7, 3, 4], [8, 9, 10]]))
