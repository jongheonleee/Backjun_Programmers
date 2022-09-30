def solution(n):
    answer = 1
    s = 0
    
    i = 1
    
    for i in range(1, n-1):
        s = i
        for j in range(i+1, n):
            s += j
            
            if s == n:
                answer += 1
                break
                
            elif s > n:
                break
                
            
    
    return answer