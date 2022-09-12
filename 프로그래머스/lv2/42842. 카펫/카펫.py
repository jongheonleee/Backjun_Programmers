def solution(brown, yellow):
    # 중앙에는 노란색
    # 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫
    measure = []
    for i in range(1, int(yellow ** 0.5)+1):
        if i == 1:
            measure.append((1, yellow))
            
        elif yellow % i == 0:
            a, b = i, yellow / i
            measure.append((a, b))
            
            
    for a, b in measure:
        if brown == 2*a + 2*b + 4:
            return [b+2, a+2]
        