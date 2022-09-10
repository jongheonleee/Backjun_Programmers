import collections
def solution(n, computers):
    answer = 0
    networks = collections.defaultdict(list)
    
    for i, cs in enumerate(computers):
        networks[i] = []
        for j, c in enumerate(cs):
            if i == j:
                continue
                
            if c == 1:
                networks[i] += [j]
                

    queue = collections.deque()
    seen = set()

    for crnt_c in range(len(computers)):
        if crnt_c not in seen:
            queue.append(crnt_c)
            
            while queue:
                c = queue.popleft()
                seen.add(c)
                
                for connected_c in networks[c]:
                    if connected_c not in seen:
                        queue.append(connected_c)
                        
            answer += 1
            

        
        
    
    return answer