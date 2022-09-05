def solution(nums):
    # 당신은 최대한 다양한 종류의 폰켓몬을 가지길 원하기 때문에,
    # 최대한 많은 종류의 폰켓몬을 포함해서 N/2마리를 선택하려 합니다.
    from collections import Counter
    
    p_cnt = Counter(nums)
    seen = set()
    m = len(nums) // 2
    cnt = 0
    
    for num in nums:
        if p_cnt[num] >= 1 and num not in seen and m >= 1:
            cnt += 1
            m -= 1
            seen.add(num)
            
    return cnt
        
    
    
