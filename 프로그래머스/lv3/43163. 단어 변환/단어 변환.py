import math
import collections
def solution(begin, target, words):
    answer = math.inf 
    similar_map = collections.defaultdict(list)
            
    for w1 in [begin] + words:
        for w2 in words:
            if w1 == w2:
                continue
                
            match_cnt = 0
            for i in range(len(w1)):
                if w1[i] == w2[i]:
                    match_cnt += 1
                    
            if match_cnt == len(w1)-1:
                similar_map[w1] += [w2]
                
                
    def dfs(word, cnt, seen):
        if word == target:
            nonlocal answer
            answer = min(cnt, answer)
            return
        
        if word != target and cnt >= len(words):
            return 
        
        seen.add(word)
        for nw in similar_map[word]:
            if nw not in seen:
                dfs(nw, cnt+1, seen)
                 
        
    dfs(begin, 0, set())  
    return answer if answer != math.inf else 0