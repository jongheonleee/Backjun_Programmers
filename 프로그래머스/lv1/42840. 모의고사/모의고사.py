def solution(answers):
    answer = []
    A, B, C = '12345', '21232425', '3311224455'
    ansA, ansB, ansC = 0, 0, 0
    
    for i, a in enumerate(answers):
        Ai, Bi, Ci = i % 5, i % 8, i % 10
        
        if A[Ai] == str(a):
            ansA += 1
            
        if B[Bi] == str(a):
            ansB += 1
            
        if C[Ci] == str(a):
            ansC += 1
            
    ansM = max([ansA, ansB, ansC]) 
    for i, ans in enumerate([ansA, ansB, ansC]):
        if ans == ansM:
            answer.append(i+1)
            
    return answer