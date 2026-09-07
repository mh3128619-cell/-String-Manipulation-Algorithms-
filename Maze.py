def solve_maze(maze, x, y):
    rows = len(maze)
    cols = len(maze[0])

    if x == rows - 1 and y == cols - 1:
        return True

    if x < 0 or x >= rows or y < 0 or y >= cols or maze[x][y] != 0:
        return False

    maze[x][y] = 2

    if (solve_maze(maze, x + 1, y) or 
        solve_maze(maze, x, y + 1) or 
        solve_maze(maze, x - 1, y) or 
        solve_maze(maze, x, y - 1)):
        return True

    return False

my_maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 0, 0]
]

if solve_maze(my_maze, 0, 0):
    print("Path found!")
else:
    print("No solution for this maze.")
