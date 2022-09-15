import collections
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    MAX = 102
    field = [[-1] * MAX for _ in range(MAX)]
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    
    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2,rect)
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                    
                elif field[i][j] != 0:
                    field[i][j] = 1
    
    queue = collections.deque([])
    queue.append((characterX*2, characterY*2))
    vis = [[0]*MAX for _ in range(MAX)]
    vis[characterX*2][characterY*2] = 1
    
    
    while queue:
        crnt_x, crnt_y = queue.popleft()
        
        if crnt_x == itemX * 2 and crnt_y == itemY * 2:
            answer = (vis[crnt_x][crnt_y] - 1)//2
            break
        
        for dx, dy in d:
            nx, ny = crnt_x+dx, crnt_y+dy
            
            if vis[nx][ny] == 0 and field[nx][ny] == 1:
                queue.append((nx, ny))
                vis[nx][ny] = 1 + vis[crnt_x][crnt_y]
        
    return answer