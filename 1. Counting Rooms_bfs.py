import sys
from collections import deque

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def count_rooms(grid: list[str]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = [[cell == '#' for cell in row] for row in grid]

    count = 0
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                bfs(visited, r, c)
                count += 1
    return count


def bfs(visited, start_r, start_c):
    rows, cols = len(visited), len(visited[0])
    q = deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = True
    while q:
        r, c = q.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if is_inside(nr, nc, rows, cols) and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True


def is_inside(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols


def main():
    n, _ = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().rstrip() for _ in range(n)]
    print(count_rooms(grid))


if __name__ == "__main__":
    main()
