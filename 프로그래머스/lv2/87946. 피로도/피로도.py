from itertools import permutations
def solution(k, dungeons):
    # 일정 피로도를 사용해서 던전을 탐험함
    # 각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"와 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"가 있음
    ans = 0
    per = []
    
    per += list(permutations(dungeons, len(dungeons)))

    for ps in per:
        cnt = 0
        crnt_k = k
        for p in ps:
            if crnt_k >= p[0]:
                crnt_k -= p[1]
                cnt += 1
                
        ans = max(ans, cnt)
        if cnt == len(dungeons):
            return ans
        
            
    return ans if ans else -1