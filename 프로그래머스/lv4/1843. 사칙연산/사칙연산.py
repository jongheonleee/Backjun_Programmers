def solution(arr):
    dp = [0, 0]
    # dp[0]:min, dp[1]:max
    cum_sum = 0
    
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == '+':
            continue
            
        elif arr[i] == '-':
            sub_min, sub_max = dp
            
            dp[0] = min(-(cum_sum+sub_max), -cum_sum +sub_min)
            
            minus_num = int(arr[i+1])
            dp[1] = max(-(cum_sum+sub_min), -minus_num+(cum_sum-minus_num) + sub_max)
            
            cum_sum = 0
            
        
        else:
            cum_sum += int(arr[i])
            
    return dp[1] + cum_sum