def solution(triangle):
    dp1 = [triangle[0][0]]

    for i in range(1, len(triangle)):
        dp2 = [0 for _ in range(len(triangle[i]))]
        dp2[0] = dp1[0] + triangle[i][0]
        dp2[-1] = dp1[-1] + triangle[i][-1]

        for j in range(1, len(triangle[i])-1):
            dp2[j] = triangle[i][j] + max(dp1[j-1], dp1[j])

        dp1 = dp2


    return max(dp1)  

