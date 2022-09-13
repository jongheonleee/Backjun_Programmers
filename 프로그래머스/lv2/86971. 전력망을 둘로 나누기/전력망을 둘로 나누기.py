import math, collections
def solution(n, wires):
    ans = math.inf
    
    def bfs(w) -> int:
        cnt, vis = 1, [False] * (n+1)
        vis[w[0]] = True
        queue = collections.deque([w[0]])
        
        while queue:
            crnt_v = queue.popleft()
            
            for next_v in graph[crnt_v]:
                if next_v == w[1] or vis[next_v]:
                    continue
                    
                queue.append(next_v)
                vis[next_v] = True
                cnt += 1
                
        return cnt
    
    graph = collections.defaultdict(set)
    for w1, w2 in wires:
        graph[w1].add(w2)
        graph[w2].add(w1)
        
    for w in wires:
        cnt = bfs(w)
        ans = min(ans, abs(n - 2*cnt))
        
    return ans
        
    
    