def solution(money):
    dp1, dp2 = [0] * len(money), [0] * len(money)
    
    # 1번 집을 터는 경우
    dp1[0] = money[0]
    for i in range(1, len(money) -1):
        # 마지막 집은 못 텀
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
        
    # 1번 집을 안터는 경우    
    dp2[0] = 0
    for j in range(1, len(money)):
        dp2[j] = max(dp2[j-1], dp2[j-2] + money[j])
        
    return max(dp1[-2], dp2[-1])