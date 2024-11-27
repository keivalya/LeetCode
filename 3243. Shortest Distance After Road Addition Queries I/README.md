You are given an integer `n` and a 2D integer array `queries`.

There are `n` cities numbered from `0` to `n - 1`. Initially, there is a **unidirectional** road from city `i` to city `i + 1` for all `0 <= i < n - 1`.

`queries[i] = [ui, vi]` represents the addition of a new unidirectional road from city $`u_i`$ to city $`v_i`$. After each query, you need to find the length of the shortest path from city `0` to city `n - 1`.

Return an array `answer` where for each `i` in the range `[0, queries.length - 1]`, `answer[i]` *is the length of the shortest path* from city `0` to city `n - 1` after processing the **first** `i + 1` queries.

Faster Code:
```python
from collections import deque, defaultdict
from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Initialize adjacency list
        adj = defaultdict(list)
        for i in range(n - 1):
            adj[i].append(i + 1)

        # Precompute shortest paths using BFS
        def bfs_shortest_paths():
            dist = [-1] * n
            dist[0] = 0
            q = deque([0])
            while q:
                current = q.popleft()
                for neighbor in adj[current]:
                    if dist[neighbor] == -1:
                        dist[neighbor] = dist[current] + 1
                        q.append(neighbor)
            return dist

        # Initialize results and shortest path distances
        results = []
        shortest_paths = bfs_shortest_paths()

        # Process queries
        for src, dst in queries:
            adj[src].append(dst)
            # Only recompute shortest paths if the new edge might affect them
            if shortest_paths[dst] == -1 or shortest_paths[src] + 1 < shortest_paths[dst]:
                shortest_paths = bfs_shortest_paths()
            results.append(shortest_paths[-1])  # Shortest distance to node n-1

        return results
```