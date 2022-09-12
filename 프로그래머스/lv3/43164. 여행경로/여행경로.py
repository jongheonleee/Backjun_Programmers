def solution(tickets):
    graph = {t[0]:[] for t in tickets}
    for t in tickets:
        graph[t[0]].append(t[1])
        
    for k in graph.keys():
        graph[k].sort(reverse=True)
        
    res, st = [], ['ICN']
    while st:
        peek = st[-1]
        
        if peek not in graph or len(graph[peek]) == 0:
            res.append(st.pop())
            
        else:
            st.append(graph[peek].pop())
            
    res.reverse()
    return res