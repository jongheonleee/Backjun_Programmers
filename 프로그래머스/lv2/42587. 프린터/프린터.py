import collections
def solution(priorities, location):
    # 우선순위 큐 구현 x -> 우선순위가 같으면 인덱스 작은것 부터 반환함
    ans = 0
    queue = collections.deque()
    
    for i, p in enumerate(priorities):
        queue.append((i, p))
        
    while 1:
        max_p = max(queue, key=lambda x:x[1])
        
        # 우선순위 기준으로 프린트 순서 재배열
        for _ in range(len(queue)):
            if queue[0][1] == max_p[1]:
                break
                
            else:
                idx, cand = queue.popleft()
                queue.append((idx, cand))        

        loc, p = queue.popleft()
        ans += 1
        
        if loc == location:
            return ans
