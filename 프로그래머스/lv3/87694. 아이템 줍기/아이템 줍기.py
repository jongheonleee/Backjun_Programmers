import collections
def solution(rectangle, characterX, characterY, itemX, itemY):
    ans, MAX = 0, 102
    coordinate = [[-1] * MAX for _ in range(MAX)]
    
    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, rect)
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    coordinate[i][j] = 0
                    
                elif coordinate[i][j] != 0:
                    coordinate[i][j] = 1
                    
    queue = collections.deque()
    queue.append((characterX * 2, characterY * 2))
    vis = [[0] * MAX for _ in range(MAX)]
    vis[characterX*2][characterY*2] = 1
    d_xy = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while queue:
        crnt_x, crnt_y = queue.popleft()
        
        if crnt_x == itemX * 2 and crnt_y == itemY * 2:
            ans = (vis[crnt_x][crnt_y] - 1)//2
            break
        
        for dx, dy in d_xy:
            nx, ny = crnt_x+dx, crnt_y+dy
            
            if vis[nx][ny] == 0 and coordinate[nx][ny] == 1:
                queue.append((nx, ny))
                vis[nx][ny] = vis[crnt_x][crnt_y] + 1
                
    return ans
                