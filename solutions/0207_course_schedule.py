"""
Problem: Course Schedule (LeetCode 207)
-----------------------------------------
Given numCourses courses and prerequisites pairs, determine if you can finish
all courses (i.e., detect if the directed graph has a cycle).

Approach: Kahn's algorithm (BFS topological sort)
- Build adjacency list and in-degree array.
- Repeatedly remove nodes with in-degree 0.
- If all nodes are processed, no cycle.

Time:  O(V + E)
Space: O(V + E)
"""
from collections import defaultdict, deque
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    q = deque([i for i in range(num_courses) if in_degree[i] == 0])
    visited = 0
    while q:
        node = q.popleft()
        visited += 1
        for nxt in graph[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append(nxt)
    return visited == num_courses


def can_finish_dfs(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """DFS cycle detection with WHITE/GRAY/BLACK coloring."""
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * num_courses

    def dfs(node):
        color[node] = GRAY
        for nxt in graph[node]:
            if color[nxt] == GRAY:
                return False  # back edge = cycle
            if color[nxt] == WHITE and not dfs(nxt):
                return False
        color[node] = BLACK
        return True

    for i in range(num_courses):
        if color[i] == WHITE and not dfs(i):
            return False
    return True


if __name__ == "__main__":
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    assert can_finish(3, [[1, 0], [2, 1]]) is True
    assert can_finish(1, []) is True
    assert can_finish_dfs(2, [[1, 0], [0, 1]]) is False
    print("All Course Schedule tests passed.")
