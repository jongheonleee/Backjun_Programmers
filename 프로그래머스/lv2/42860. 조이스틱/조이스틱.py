def solution(name):
    ans, min_move = 0, len(name)-1
    
    for i, char in enumerate(name):
        ans += min(ord(char)-ord('A'), ord('Z')-ord(char)+1)
        
        j = i+1
        while j < len(name) and name[j] == 'A':
            j += 1
            
        min_move = min([min_move, 2*i+(len(name)-j), i+2*(len(name)-j)])
        
    ans += min_move
    return ans
    
    return ans