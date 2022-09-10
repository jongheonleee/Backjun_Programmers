import heapq
def solution(scoville, K):    
    answer = 0
    
    # 최소힙 구현
    heapq.heapify(scoville)
        
    while K > scoville[0]:
        answer += 1
        new_s = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new_s)
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer