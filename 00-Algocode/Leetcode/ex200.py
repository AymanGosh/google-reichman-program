from typing import List



def numIslands(grid: List[List[str]]) -> int:

    r_len = len(grid)
    c_len = len(grid[0])


    visit = set()

    def dfs(r,c):

        if r >= r_len or r < 0 or c >= c_len or c < 0 or (r,c) in visit:
            return 0

        v = grid[r][c]
        if v == "0":
            return 0

        visit.add((r,c))
        print(v)
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)


    dfs(0,0)
    return 0


grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
assert numIslands(grid) == 0