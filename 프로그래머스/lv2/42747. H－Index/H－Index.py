def solution(citations):
#     max_c = 0
#     citations.sort()
    
#     for i, c in enumerate(citations):
#         cnt_cite = len(citations)-i
        
#         if i+1 <= c <= cnt_cite:
#             max_c = max(max_c, c)
        
#     return max_c
    citations.sort()
    for i, c in enumerate(citations):
        if c >= len(citations) - i:
            return len(citations) - i
        
    return 0