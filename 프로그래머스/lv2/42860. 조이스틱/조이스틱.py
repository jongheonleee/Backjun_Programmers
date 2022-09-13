def solution(name):
    # 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 
    ans = 0
    min_move = len(name)-1
    
    for i, char in enumerate(name):
        ans += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        nt = i+1
        while nt < len(name) and name[nt] == 'A':
            nt += 1
            
        min_move = min(min_move, 2 * i + len(name) - nt, i + 2 * (len(name) - nt))
        
    ans += min_move
    return ans
