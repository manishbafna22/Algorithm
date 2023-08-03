def hasPath(maze, start, destination):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(row, col):
        if visited[row][col]:
            return False
        visited[row][col] = True
        if [row, col] == destination:
            return True
        # Move Up
        i, j = row, col
        while i > 0 and maze[i - 1][j] == 0:
            i -= 1
        if dfs(i, j):
            return True
        # Move Down
        i, j = row, col
        while i < rows - 1 and maze[i + 1][j] == 0:
            i += 1
        if dfs(i, j):
            return True
        # Move Left
        i, j = row, col
        while j > 0 and maze[i][j - 1] == 0:
            j -= 1
        if dfs(i, j):
            return True
        # Move Right
        i, j = row, col
        while j < cols - 1 and maze[i][j + 1] == 0:
            j += 1
        if dfs(i, j):
            return True
        return False
    return dfs(start[0], start[1])
# Test cases
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
test_case_1 = [0, 4]
test_case_2 = [0, 4]
test_case_3 = [4, 3]

print(hasPath(maze, test_case_1, [4, 4]))  
print(hasPath(maze, test_case_2, [3, 2]))  
print(hasPath(maze, test_case_3, [0, 1]))  

