def solution(clothes):
    answer = 1
    clothes_map = {}
    
    for c in clothes:
        if c[-1] in clothes_map:
            clothes_map[c[-1]] += 1
            
        else:
            clothes_map[c[-1]] = 1
            
    for val in clothes_map.values():
        # 1을 더한 이유는 안입는 경우를 고려하는 거임

        # 얼굴: A, B, X
        # 상의: ㄱ, ㄴ, ㄷ, X
        # 하의: 1, X
        
        # 마지막에 모두 X는 아예 안입는 경우이므로 -1를 해줘서 빼준다
        answer *= (val + 1)
            
    return answer - 1

'''
(종류 + 1) 곱하고 1 빼면 되는 이유: ex. (a + 1)(b + 1)(c + 1) - 1 = (a + b + c) + (ab + bc + ca) + abc
'''