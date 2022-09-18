def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[1])
    cctv = routes[0][1]
    
    for start, end in routes[1:]:
        if cctv < start:
            answer += 1
            cctv = end
            
    
    return answer