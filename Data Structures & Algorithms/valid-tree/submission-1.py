from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(set)

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        if not (len(edges) == n - 1):
            return False
        
        seen = set()
        # Do DFS, and keep track of the parent
        def dfs(node, parent):
            seen.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in seen:
                    return False
                if not dfs(nei, node):
                    return False
            
            return True
        
        dfs(0, -1)

        # # Do BFS from any node
        # queue = deque([0])
        # seen = set()
        # seen.add(0)

        # while queue:
        #     if len(seen) == n:
        #         break

        #     node = queue.popleft()
            
        #     for nei in adj[node]:
        #         if nei not in seen:
        #             queue.append(nei)
        #             seen.add(nei)

        
        return True if len(seen) == n else False
        
        
        
