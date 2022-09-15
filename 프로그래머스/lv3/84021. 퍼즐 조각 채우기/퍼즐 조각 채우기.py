def dfs(table, i, j, shape, find = 1):
        # 우 좌 하 상
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0] 
    stack = [[i, j]] # 현재 위치 스택에 저장
    shape.append((i, j))
    
    while stack:
        a, b = stack.pop()
        table[a][b] = -1 # 방문 처리
        for i in range(4): # 우 좌 하 상 순으로 스택에 저장 -> 상 하 좌 우 순으로 꺼내져 수행된다.
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < len(table) and 0 <= y < len(table[0]) and table[x][y] == find:
                table[x][y] = -1
                stack.append([x, y])
                shape.append((x, y))
                
# 블록이나 빈 칸을 (0, 0)을 시작점으로 옮김
def rearrange(shape):
    minX = min([x[1] for x in shape])
    minY = min([x[0] for x in shape])
    shape = [(s[0]-minY, s[1]-minX) for s in shape]
    return sorted(shape) # 블록이 여러 칸으로 이루어진 경우 같은 모양에서 같은 결과를 위해 정렬해서 반환

# 여러 방향으로 회전 후 하나의 값 반환
def rotate(shape):
    if len(shape) == 1: return shape
    shapes = []
    shape = list(shape)
    shape.sort()
    width = max([x[1] for x in shape]) - min([x[1] for x in shape])
    height = max([x[0] for x in shape]) - min([x[0] for x in shape])
    # 시계 방향으로 4회 회전
    for _ in range(4):
        tmp = []
        # 시계 방향으로 회전하는 방법
        # 1. (x, y) 값을 (y, x)로 x, y를 맞바꾸는 '전치'
        for pos in shape:
            tmp.append((pos[1], pos[0])) # 전치
        # 2. 전치된 결과에서 x 좌표를 가로 길이에서 뺀다.
        tmp = [(x[0], width - x[1]) for x in tmp]
        tmp = rearrange(tmp) # 재정렬
        shape = tmp # 시계 방향으로 회전 한 블록을 shape에 다시 저장
        shapes.append(shape)
        width, height = height, width # 2x3 크기의 블록이 회전하면 3x2가 되므로 width, height를 맞바꾼다.
    
    # 4번 회전한 결과가 담긴 shapes의 최소값을 반환하면 
    # 같은 구성의 순서가 다른 리스트에서도 항상 동일한 결과 반환
    return min(shapes) 
                
def solution(game_board, table):
    # table에서 추출된 블록들과 game_board에서 추출된 빈 칸들을 저장하는 리스트
    shapes, spaces = list(), list() 
    # game_board와 table의 크기가 같다고 주어졌기 때문에 한 번에 돌릴 수 있음
    for i in range(len(table[0])):
        for j in range(len(table)):
            # table에서 블록 추출하는 dfs
            if table[i][j] == 1: # 1이면 블록
                shape = list()
                dfs(table, i, j, shape) # table에서 블록(1) 추출
                shape = rearrange(shape) # 추출한 블록 (0, 0) 부터 시작하도록 위치 값 조정
                shape = rotate(shape) # 회전 후 항상 동일한 결과 반환
                shapes.append(shape) # shapes 에서 블록들 관리
            # game_board에서 빈 칸 추출하는 dfs
            if game_board[i][j] == 0: # 0이면 빈 칸
                space = list()
                dfs(game_board, i, j, space, find = 0) # game_board에서 빈 칸(0) 추출
                space = rearrange(space) # 추출한 공백 (0, 0) 부터 시작하도록 위치 값 조정
                space = rotate(space) # 회전 후 항상 동일한 결과 반환
                spaces.append(space) # spaces 에서 공백들 관리
                
    answer = 0
    for space in spaces:
        for shape in shapes:
            if space == shape: # 같은 모양이 있다면
                answer += len(shape) # 블록의 개수만큼 더한다
                shapes.remove(shape) # 사용된 블록은 제거
                break
    return answer