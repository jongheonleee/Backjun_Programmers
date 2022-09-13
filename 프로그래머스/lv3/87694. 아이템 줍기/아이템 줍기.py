import collections 
def solution(rectangle, characterX, characterY, itemX, itemY):
    ans, MAX = 0, 102
    
    field = [[5] * MAX for _ in range(MAX)]
    
    # 테두리 그리기
    # 두배해주는 이유
    # 입출력 예1에서, 현재 좌표가 (3,5)일때 위로 이동하면 (3,6)도 성립
    # 하지만 실제로는 테두리가 이어져 있지않아서 이동 불가함
    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, rect)
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                    
                elif field[i][j] != 0:
                    field[i][j] = 1
                    
    queue = collections.deque()
    queue.append([characterX * 2, characterY * 2])
    vis = [[0] * MAX for _ in range(MAX)]
    vis[characterX * 2][characterY * 2] = 1
    d_xy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        
        if x == itemX * 2 and y == itemY * 2:
            ans = (vis[x][y] - 1) // 2
            break
            
        for dx, dy in d_xy:
            nx, ny = x+dx, y+dy
            
            if vis[nx][ny] == 0 and field[nx][ny] == 1:
                queue.append([nx, ny])
                vis[nx][ny] = vis[x][y] + 1
                
    return ans
    