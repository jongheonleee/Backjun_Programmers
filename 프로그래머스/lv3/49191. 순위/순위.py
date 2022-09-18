from collections import defaultdict
def solution(n, results):
    ans = 0
    win_graph, lose_graph = defaultdict(set), defaultdict(set)
    
    for winner, loser in results:
        win_graph[loser].add(winner)
        lose_graph[winner].add(loser)
    
    # 딕셔너리에서 update()의 기능
    #   dict_example = {'림코딩': 30, '김갑환': 33, '장고환': 23} 
    #   dict_example.update({'림코딩':33,'최번개':26})
    #   -> {'림코딩': 33, '김갑환': 33, '장고환': 23, '최번개': 26} 
    # 기존의 데이터를 수정할 수도 있고, 추가할 수도 있음
    for i in range(1, n+1):
        for winner in win_graph[i]:
            lose_graph[winner].update(lose_graph[i])
            
        for loser in lose_graph[i]:
            win_graph[loser].update(win_graph[i])
            
    for i in range(1, n+1):
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:
            ans += 1
            
            
    
    return ans