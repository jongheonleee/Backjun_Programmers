def solution(prices):
    answer, st = [0 for _ in range(len(prices))], []
    
    for i1, p1 in enumerate(prices):
        while st and st[-1][1] > p1:
            i2, p2 = st.pop()
            answer[i2] = i1 - i2
            
        st.append((i1, p1))
        
    i1, p1 = st.pop()
    
    while st:
        i2, p2 = st.pop()
        answer[i2] = i1 - i2
            
    return answer