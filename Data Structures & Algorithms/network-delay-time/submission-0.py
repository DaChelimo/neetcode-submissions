import math
from heapq import heapify, heappop, heappush
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adj list
        # Dijkstra's starting from k to all nodes
        # Sum up all distances
        # If any is still infinity, return -1

        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        dist = {u: math.inf for u in range(1, n + 1)}
        

        dist[k] = 0
        minHeap = [(0, k)]
        heapify(minHeap)

        while minHeap:
            nodeDist, node = heappop(minHeap)

            if nodeDist > dist[node]:
                continue

            for nei, neiWeight in adj[node]:
                newDist = nodeDist + neiWeight

                if dist[nei] > newDist:
                    dist[nei] = newDist
                    heappush(minHeap, (newDist, nei))
    

        longest = 0

        for distance in dist.values():
            if distance == math.inf:
                return -1
            longest = max(distance, longest)

        return longest

        
            
