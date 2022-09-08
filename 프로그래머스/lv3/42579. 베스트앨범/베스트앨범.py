def solution(genres, plays):
    ans = []
    
    # dic1; k> 장르, v> 인덱스, 각 노래(인덱스)마다 플레이횟수
    # dic2; k> 장르, v> 해당 장르의 총 플레이횟수
    dic1, dic2 = {}, {}
    
    for i, (g, ps) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, ps)]
            
        else:
            dic1[g].append((i, ps))
            
        if g not in dic2:
            dic2[g] = ps
            
        else:
            dic2[g] += ps
            
    # 내림차순
    # 가장 많이 플레이한 장르부터 접근
    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        # 내림차순
        # 해당 장르에서, 가장 많이 플레이한 노래(인덱스) 접근
        # 2개만 확보
        for (i, ps) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            # 여기서 "장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다."
            # [:2]하면 오류 발생하지 않음?
            ans.append(i)
            
    return ans
    