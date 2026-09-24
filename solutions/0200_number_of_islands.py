"""
Problem: Number of Islands (LeetCode 200)
-------------------------------------------
Given an m x n 2D grid of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and connected horizontally/vertically.

Approach: DFS flood fill
- For each unvisited land cell, start a DFS that marks all connected land as visited.
- Each DFS start = one island.

Time:  O(m * n)
Space: O(m * n) worst case (recursion stack)
"""
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    count = 0

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            return
        grid[i][j] = '0'  # mark visited
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count


def num_islands_bfs(grid: List[List[str]]) -> int:
    """BFS variant."""
    from collections import deque
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                grid[i][j] = '0'
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                            grid[nx][ny] = '0'
                            q.append((nx, ny))
    return count


if __name__ == "__main__":
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert num_islands([row[:] for row in grid1]) == 3
    assert num_islands_bfs([row[:] for row in grid1]) == 3
    assert num_islands([["1"]]) == 1
    assert num_islands([["0"]]) == 0
    assert num_islands([["0", "0"], ["0", "0"]]) == 0
    print("All Number of Islands tests passed.")
