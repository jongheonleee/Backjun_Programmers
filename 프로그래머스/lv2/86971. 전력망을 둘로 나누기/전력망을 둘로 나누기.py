import collections, math
def solution(n, wires):
    # 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누
    # 개수의 차이(절대값)를 return
    ans = math.inf
    graph = collections.defaultdict(set)
    
    def bfs(w):
        cnt, vis = 1, [False] * (n+1)
        # 방문 기록을 리스트에서 각 인덱스의 True/False로 저장
        # - True: 방문
        # - False: 미방문
        vis[w[0]] = True
        queue = collections.deque([w[0]])
        
        while queue:
            crnt_v = queue.popleft()
            
            for i in graph[crnt_v]:
                if vis[i] or i == w[1]:
                    continue
                    
                cnt += 1
                queue.append(i)
                vis[i] = True
                
        return cnt
    
    # graph만들기 방향x
    for v1, v2 in wires:
        graph[v1].add(v2)
        graph[v2].add(v1)
        
    # w:[v1, v2] 끊어진 노드를 의미함. 
    for w in wires:
        cnt = bfs(w)
        # A: n-cnt, b: cnt
        ans = min(ans, abs(n-cnt*2))
    return ans