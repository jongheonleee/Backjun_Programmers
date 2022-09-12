from itertools import permutations
def solution(numbers):
    ans, nums, per = [], [n for n in numbers], []
    
    for i in range(1, len(numbers)+1):
        # nums에서 i개씩 순열 조합 만들어주기
        per += list(permutations(nums, i))
        
    # 각 순열 조합을 하나의 문자열로 만들어서 리스트에 저장
    new_nums = [int(("").join(p)) for p in per]
    
    # 모든 순열 조합의 숫자들
    for n in new_nums:
        if n < 2:
            continue
            
        check = True
        
        # 소수인지 아닌지 판별
        # n의 약수의 절반
        # 각 숫자들로 나눠보기
        for i in range(2, int(n**0.5)+1):
            # 나누어 떨어지면 소수가 아님
            if n % i == 0:
                check = False
                break
                
        # 소수일 경우 해당 숫자 ans에 담기
        if check:
            ans.append(n)
            
    # 같은 숫자가 순열에 담겨있는 경우가 있음
    return len(set(ans))