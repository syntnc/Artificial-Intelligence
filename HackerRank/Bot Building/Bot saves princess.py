#!/usr/bin/python
def displayPathtoPrincess(n, grid):
    '''PRINTS ALL MOVES'''
    princess = None
    corners = [[0, 0], [0, n-1], [n-1, 0], [n-1, n-1]]
    for corner in corners:
        princess = corner if grid[corner[0]][corner[1]] == 'p' else princess
    vertical = 'UP' if princess[0] == 0 else 'DOWN'
    horizontal = 'LEFT' if princess[1] == 0 else 'RIGHT'
    for _ in range(abs(princess[0] - (n // 2))):
        print(vertical)
    for _ in range(abs(princess[1] - (n // 2))):
        print(horizontal)

def main():
    '''MAIN METHOD'''
    m = int(input())
    grid = []
    for i in range(0, m):
        grid.append(input().strip())

    displayPathtoPrincess(m, grid)

if __name__ == '__main__':
    main()
