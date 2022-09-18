def solution(n, times):
    ans, left, right = 0, len(times), max(times)*n
    
    while left <= right:
        mid = (left + right) // 2
        check = 0
        
        for t in times:
            check += mid // t
            
            if check >= n:
                break
                
        if check >= n:
            ans = mid
            right = mid - 1
            
        elif check < n:
            left = mid + 1
            
    return ans
