def solution(phone_book):
    ans = True
    hash_map = {}
    
    for num in phone_book:
        hash_map[num] = 1
        
    for num in phone_book:
        tmp = ''
        
        for n in num:
            tmp += n
            
            if tmp in hash_map and tmp != num:
                ans = False
                
    return ans
    
    