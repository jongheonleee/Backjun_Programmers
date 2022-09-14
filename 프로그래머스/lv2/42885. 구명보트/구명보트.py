def solution(people, limit):
    people.sort()
    cnt, i, j = 0, 0, len(people)-1
    
    # 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.
    while i <= j:
        cnt += 1
        
        if people[i] + people[j] <= limit:
            i+=1
        j-= 1
        
    return cnt
        
    
                