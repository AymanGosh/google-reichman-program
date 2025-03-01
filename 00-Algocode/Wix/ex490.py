def hasPath(maze, start, destination):
    rows, cols = len(maze), len(maze[0])
    visited = set()

    def dfs(x, y):
        if (x, y) in visited:
            return False
        if [x, y] == destination:
            return True
        visited.add((x, y))

        directions = [(0,1), (0,-1), (1,0), (-1,0)]  # Right, Left, Down, Up

        for dx, dy in directions:
            nx, ny = x, y
            # Roll the ball until it hits a wall
            while 0 <= nx + dx < rows and 0 <= ny + dy < cols and maze[nx + dx][ny + dy] == 0:
                nx += dx
                ny += dy
            # Recur from the last valid position
            if dfs(nx, ny):
                return True

        return False

    return dfs(start[0], start[1])
def test_hasPath():
    # Test Case 1: Ball can reach the destination
    maze1 = [
        [1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,1,0,0,0,1],
        [1,1,1,1,1,1,1]
    ]
    start1 = [1,1]
    destination1 = [4,5]
    assert hasPath(maze1, start1, destination1) == True, "Test Case 1 Failed"

    # Test Case 2: Ball cannot reach the destination due to walls
    maze2 = [
        [1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1],
        [1,1,1,1,1,1,1]
    ]
    start2 = [1,1]
    destination2 = [4,5]
    assert hasPath(maze2, start2, destination2) == False, "Test Case 2 Failed"

    # Test Case 3: Ball starts at the destination
    maze3 = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]
    start3 = [1,1]
    destination3 = [1,1]
    assert hasPath(maze3, start3, destination3) == True, "Test Case 3 Failed"

    # Test Case 4: Large open space with no obstacles
    maze4 = [
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]
    ]
    start4 = [1,1]
    destination4 = [3,3]
    assert hasPath(maze4, start4, destination4) == True, "Test Case 4 Failed"

    print("All test cases passed!")


# Run the tests
test_hasPath()
