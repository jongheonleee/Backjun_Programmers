import collections
def solution(maps):
    if (len(maps) == 1 or len(maps[0]) == 1) and 0 in maps:
        return -1

    row, col = len(maps), len(maps[0])
    queue = collections.deque([(0, 0)])
    d = [(1,0), (0,1), (-1,0), (0, -1)]

    
    while queue:
        y, x = queue.popleft()
        
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            
            if 0<= ny<=row-1 and 0<= nx<=col-1 and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                queue.append((ny, nx))
                
    return maps[row-1][col-1] if maps[row-1][col-1] > 1 else -1
                        