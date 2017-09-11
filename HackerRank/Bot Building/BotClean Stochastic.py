def nextMove(posr, posc, board):
    '''RETURNS THE NEXT MOVE'''
    nearest_x, nearest_y = min(((i, j) \
                            for i, row in enumerate(board) if 'd' in row\
                            for j, c in enumerate(row) if c == 'd'), \
                            key=lambda x: abs(posr - x[0]) + abs(posc - x[1]))
    print("LEFT" if nearest_y < posc \
          else "RIGHT" if nearest_y > posc \
          else "UP" if nearest_x < posr \
          else "DOWN" if nearest_x > posr \
          else "CLEAN")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
