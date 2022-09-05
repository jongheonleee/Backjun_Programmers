def solution(participant, completion):
    # using hash_table based on completion
    from collections import Counter
    dic_com = Counter(completion)
    
    
    for p in participant:
        if p in dic_com and dic_com[p] >= 1:
            dic_com[p] -= 1
            
        else:
            return p
            

        
    