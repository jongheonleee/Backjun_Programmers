import collections 
import math
def solution(progresses, speeds):
    answer = []
    queue = collections.deque()
    
    for i, (p, s) in enumerate(zip(progresses, speeds)):
        day = math.ceil((100 - p) / s)
        queue.append(day)
        
    while queue:
        
        first = queue.popleft()
        cnt = 1
        
        while queue and first >= queue[0] :
            queue.popleft()
            cnt += 1
            
        answer.append(cnt)
    
    
    
    
    return answer