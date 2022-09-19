def solution(distance, rocks, n):
    ans = 0
    rocks.sort()
    rocks.append(distance)
    
    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        mid_dis = float('inf')
        
        crnt, cnt_del = 0, 0
        
        for r in rocks:
            diff = r - crnt
            
            if diff < mid:
                cnt_del += 1
                
            else:
                crnt = r
                mid_dis = min(mid_dis, diff)
                
        if cnt_del > n:
            right = mid - 1
            
        else:
            ans = mid_dis
            left = mid + 1
            
    return ans