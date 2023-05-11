class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        cost = lambda x, y : abs(x[0] - y[0]) + abs(x[1] - y[1]) 
        
        specialRoads = [start + start + [0]] + specialRoads 
        dist = [float('inf') for _ in specialRoads] 
        dist[0] = 0 
        vis = [False for _ in specialRoads]
          
        res = cost(start, target)  
        pq = [(0, 0)] 
        while pq: 
            d, v = heappop(pq)
            if vis[v]:
                continue
            vis[v] = True
            res = min(res, d + cost(specialRoads[v][2:4], target))
            for w in range(len(dist)):
                if vis[w]:
                    continue   
                alt = d + cost(specialRoads[v][2:4], specialRoads[w][:2]) + specialRoads[w][4]
                if alt < dist[w]:
                    dist[w] = alt 
                    heappush(pq, (alt, w))
        return res 
            
        
