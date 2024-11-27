class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i+1] for i in range(n)]
        def shortest_path():
            q = deque()
            q.append((0,0))
            visit = set()
            visit.add((0,0))


            while q:
                current_node, length = q.popleft()
                if current_node == n-1:
                    return length
                for neighbor in adj[current_node]:
                    if neighbor not in visit:
                        q.append((neighbor, length + 1))

        results = []
        for src, dst in queries:
            adj[src].append(dst)
            results.append(shortest_path())
        return results