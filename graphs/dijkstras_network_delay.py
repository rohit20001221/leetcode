from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, N, K):
        G = defaultdict(list)

        for u, v, weight in times:
            G[u].append([weight, v])
    
        min_heap = [(0,K)]

        visited = set()
        distance = {i:float('inf') for i in range(1, N+1)}

        distance[K] = 0

        while len(min_heap) > 0:
            cur_dist, cur_node = heapq.heappop(min_heap)

            if cur_node in visited:
                continue
            
            visited.add(cur_node)

            if len(visited) == N:
                return distance
            
            for direct_distance, v in G[cur_node]:
                if cur_dist + direct_distance < distance[v] and v not in visited:
                    distance[v] = cur_dist + direct_distance
                    heapq.heappush(min_heap, (distance[v], v))

        return -1

            
times = [
    [1,2,1],
    [1,3,1],
    [3,4,1]
]

N = 4
K = 1

s = Solution()

print(s.networkDelayTime(times, N, K))