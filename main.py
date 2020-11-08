from Board import *

if __name__ == "__main__":
    board = Board()
    board.initBoard()
    board.placingMan(1)
    print(board.getMan(1))

    board.placingMan(2)
    print(board.getMan(2))