from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency matrix and seen
        # For each node, loop through neighbors and do dfs
        # Check size of seen and if not equal to n, traverse again until you find an undiscovered node and add count += 1
        # Time: O(V + E). Space: O(V + E)

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = 0
        seen = set()

        # def bfs(node: int):
        #     queue = deque([node])
        #     seen.add(node)

        #     while queue:
        #         curr = queue.popleft()

        #         for nei in adj[curr]:
        #             if nei not in seen:
        #                 queue.append(nei)
        #                 seen.add(nei)
        def dfs(node: int):
            seen.add(node)

            for nei in adj[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
            
        for node in range(n):
            if node not in seen:
                dfs(node)
                count += 1
        
        return count
            



