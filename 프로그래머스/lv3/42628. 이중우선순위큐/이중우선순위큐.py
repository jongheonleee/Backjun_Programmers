import collections
import heapq
def solution(operations):
    max_heap, min_heap = [], []
    
    # max_heap구현
    for o in operations:
        if 'I' in o:
            heapq.heappush(max_heap, -int(o[2:]))
            heapq.heappush(min_heap, int(o[2:]))
            
        if 'D 1' in o and max_heap:
            max_num = heapq.heappop(max_heap)
            min_heap.remove(-max_num)
            
        if 'D -1' in o and min_heap:
            min_num = heapq.heappop(min_heap)
            max_heap.remove(-min_num)
            
    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)] if len(max_heap) >= 1 and len(min_heap) >= 1 else [0, 0]