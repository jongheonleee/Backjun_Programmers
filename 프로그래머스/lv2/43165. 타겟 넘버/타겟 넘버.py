def solution(numbers, target):
    answer = 0
    
    def dfs(idx, res):
        if idx == len(numbers)-1:
            if res == target:
                nonlocal answer
                answer += 1
        
        else:
            dfs(idx+1, res+numbers[idx+1])
            dfs(idx+1, res-numbers[idx+1])
            
    dfs(0, numbers[0])
    dfs(0, -numbers[0])
        
    return answer