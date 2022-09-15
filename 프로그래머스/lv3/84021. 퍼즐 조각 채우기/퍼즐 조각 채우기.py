def dfs(matrix, i, j, find):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0 ,1]
    stack = [[i,j]]
    result = [(i,j)]

    while stack:
        a, b = stack.pop()
        matrix[a][b] = -1
        for i in range(4):
            x, y = a + dx[i], b + dy[i]
            if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix) and matrix[x][y] == find:
                matrix[x][y] = -1
                stack.append([x,y])
                result.append((x,y))
    return result

def move(piece):
    min_x = min([x[1] for x in piece])
    min_y = min([x[0] for x in piece])
    piece = [(p[0]-min_y, p[1]-min_x) for p in piece]
    return sorted(piece)

def rotate(piece):
    if len(piece) == 1:
        return piece
    result = [piece]
    width = max(x[1] for x in piece) - min(x[1] for x in piece)
    height = max(x[0] for x in piece) - min(x[0] for x in piece)
    moves = [height, width, height]

    for i in range(3):
        lst = []
        
        for j in result[-1]:
            lst.append((j[1],j[0]))
            
        lst = [(x[0], moves[i] - x[1]) for x in lst]
        result.append(sorted(lst))

    return min(result)

def solution(game_board, table):
    answer = 0
    spaces, pieces = [], []
    for i in range(len(table[0])):
        for j in range(len(table)):
            if table[i][j] == 1:
                piece = dfs(table, i, j, 1)
                piece = move(piece)
                piece = rotate(piece)
                pieces.append(piece)

            if game_board[i][j] == 0:
                space = dfs(game_board, i, j, 0)
                space = move(space)
                space = rotate(space)
                spaces.append(space)

    for space in spaces:
            for piece in pieces:
                if space == piece:
                    answer += len(piece)
                    pieces.remove(piece)
                    break
                
    return answer