import sys
from collections import deque

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def main():
    first_line = sys.stdin.readline().split()
    r = int(first_line[0])
    c = int(first_line[1])

    grid = []
    for i in range(r):
        grid.append(sys.stdin.readline().rstrip())

    q = deque()
    visited = [[False for j in range(c)] for i in range (r)]

    for i in range(r):
        for j in range(c):
            if grid[i][j] == '#':
                visited[i][j] = True
            else:
                visited[i][j] = False
    count = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                if not visited[i][j]:
                    q.append((i, j))
                    visited[i][j] = True
                    bfs(grid, q, visited)
                    count = count + 1
    print(count)

def bfs(grid, q, visited):
    while(q):
        curr = q.popleft()
        r = curr[0]
        c = curr[1]
        for dir in DIRS:
            next_r = r + dir[0]
            next_c = c + dir[1]
            if(isValid(next_r, next_c, len(grid), len(grid[0])) and visited[next_r][next_c] == False):
                q.append((next_r, next_c))
                visited[next_r][next_c] = True

def isValid(r,c,m,n):
    return r < m and c < n and r >= 0 and c >= 0

main()




