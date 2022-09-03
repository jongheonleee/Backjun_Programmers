from collections import deque
def solution(arr):
    deq = deque()
    ans = []
    
    for num in arr:
        deq.append(num)
        
    for cand in deq:
        if len(ans) == 0:
            ans.append(cand)
            
        if cand == ans[-1]:
            continue
            
        else:
            ans.append(cand)
            
    return ans