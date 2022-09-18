import collections
def solution(n, edge):
    graph = collections.defaultdict(list)
    vis = [0] * (n+1)
    
    for u, v in edge:
        graph[u] += [v]
        graph[v] += [u]
        
    queue = collections.deque([1])
    vis[1] = 1
    
    while queue:
        u = queue.popleft()
        
        for v in graph[u]:
            if not vis[v]:
                vis[v] = vis[u] + 1
                queue.append(v)
                
    max_dist = max(vis)
    cnt = vis.count(max_dist)
    
    return cnt if cnt > 0 else 1
                    
