"""
Problem: Clone Graph (LeetCode 133)
-------------------------------------
Given a reference to a node in a connected undirected graph, return a deep copy
(clone) of the graph.

Approach: DFS with visited map
- Use a dict mapping original node -> cloned node.
- Recursively clone neighbors; skip already-cloned nodes.

Time:  O(V + E)
Space: O(V)
"""
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    if not node:
        return None
    visited = {}

    def dfs(n: Node) -> Node:
        if n in visited:
            return visited[n]
        clone = Node(n.val)
        visited[n] = clone
        for neighbor in n.neighbors:
            clone.neighbors.append(dfs(neighbor))
        return clone

    return dfs(node)


def clone_graph_bfs(node: Optional[Node]) -> Optional[Node]:
    """BFS variant."""
    from collections import deque
    if not node:
        return None
    visited = {node: Node(node.val)}
    q = deque([node])
    while q:
        n = q.popleft()
        for neighbor in n.neighbors:
            if neighbor not in visited:
                visited[neighbor] = Node(neighbor.val)
                q.append(neighbor)
            visited[n].neighbors.append(visited[neighbor])
    return visited[node]


def _build_cycle(n):
    """Build a cycle graph with n nodes labeled 1..n."""
    nodes = [Node(i + 1) for i in range(n)]
    for i in range(n):
        nodes[i].neighbors = [nodes[(i - 1) % n], nodes[(i + 1) % n]]
    return nodes[0]


if __name__ == "__main__":
    # Simple 4-node cycle: 1-2-3-4-1
    head = _build_cycle(4)
    clone = clone_graph(head)
    assert clone.val == 1
    assert clone is not head
    assert clone.neighbors[0] is not head.neighbors[0]
    assert clone.neighbors[0].val in (2, 4)
    assert clone.neighbors[1].val in (2, 4)
    assert clone_graph(None) is None
    # Single node
    single = Node(1)
    assert clone_graph(single).val == 1
    assert clone_graph_bfs(head).val == 1
    print("All Clone Graph tests passed.")
