def searchWord(grid, key):
    rows = len(grid)
    columns = len(grid[0])

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == key[0]:
                if(backTrackSearchWord(grid, i, j, '', key)):
                    return True

    return False

def backTrackSearchWord(grid, x, y, current, key):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    if ( x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '' ):
        return False
    

    current = current + grid[x][y]

    if(len(current) > len(key)):
        return False
    
    if(current[len(current)-1] != key[len(current)-1]):
        return False
    
    if current == key:
        return True

    temp = grid[x][y]
    grid[x][y] = ''

    

    for i in range(len(dx)):
        if (backTrackSearchWord(grid, x+dx[i], y+dy[i], current, key)):
            return True
    
    grid[x][y] = temp
    return False
    


grid = [
    ['A','B','C', 'E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]

print(searchWord(grid, 'ASF'))