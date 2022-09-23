def solution(dp):
    # 삼각형의 정보가 담긴 배열 triangle이 매개변수
    # 거쳐간 숫자의 최댓값을 return
    
    for i in range(1, len(dp)):
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] += dp[i-1][j]
                
            elif j == len(dp[i])-1:
                dp[i][j] += dp[i-1][j-1]
                
            else:
                dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
                
    return max(dp[-1])
                
                
            
    
    return 