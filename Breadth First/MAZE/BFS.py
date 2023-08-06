def hasPath(maze, start, destination):
    if not maze or not maze[0]:
        return False
    rows, cols = len(maze), len(maze[0])
    queue = [start]
    visited = set(tuple(start))
    while queue:
        row, col = queue.pop(0)
        # Check if the current position is the destination
        if [row, col] == destination:
            return True
        # Find valid neighbors and add them to the queue
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            r, c = row, col
            while 0 <= r + dr < rows and 0 <= c + dc < cols and maze[r + dr][c + dc] == 0:
                r += dr
                c += dc
            if (r, c) not in visited:
                queue.append([r, c])
                visited.add((r, c))
    return False
# Test Case 3
maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [4, 3]
destination = [0, 1]
print(hasPath(maze, start, destination))  # Output: False



