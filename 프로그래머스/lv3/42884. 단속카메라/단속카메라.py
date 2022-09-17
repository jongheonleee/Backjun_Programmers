def solution(routes):
    # routes를 나간시간 순으로 오름차순 정렬
    routes.sort(key = lambda x: x[1])
    answer = 1
    # camera = 현재 카메라가 설치된 위치
    camera = routes[0][1]
    
    # 두번째 차량부터 마지막번째 차량까지 반복문을 돌며 현재 카메라가 설치된 시간보다
    # 들어온 시간이 늦으면 camera에 현재 차량의 나간시간을 넣어주고 answer 1증가
    for i in range(1, len(routes)):
        if camera < routes[i][0]:
            camera = routes[i][1]
            answer += 1
                
    return answer