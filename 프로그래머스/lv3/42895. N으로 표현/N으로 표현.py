def solution(N, number):
    dp = []
    
    for i in range(1, 9):
        set_nums = set()
        set_nums.add(int(str(N) * i))
        
        for j in range(0, i-1):
            for x in dp[j]:
                for y in dp[-j-1]:
                    set_nums.add(x+y)
                    set_nums.add(x-y)
                    set_nums.add(x*y)
                    
                    if y != 0:
                        set_nums.add(x/y)
                        
        if number in set_nums:
            return i
        
        dp.append(set_nums)
    
    return -1