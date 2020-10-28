from Board import *

import tkinter as tk

PIECE_SIZE = 10

click_x = 0
click_y = 0

pieces_x = [35, 35, 35, 133, 133, 133, 231, 231, 231, 280, 280, 280, 280, 280, 280, 329, 329, 329, 427, 427, 427, 525, 525, 525]
pieces_y = [30, 275, 520, 128, 275, 422, 226, 275, 324, 30, 128, 226, 324, 422, 520, 226, 275, 324, 128, 275, 422, 30, 275, 520]


coor_black = []
coor_white = []

person_flag = 1
piece_color = "black"


board = []
# Set 24 empty intersections
for i in range(24):
    board.append("X")


# Display
def showChange(color):
    global piece_color
    piece_color = color
    side_canvas.delete("show_piece")
    side_canvas.create_oval(110 - PIECE_SIZE, 25 - PIECE_SIZE,
                            110 + PIECE_SIZE, 25 + PIECE_SIZE,
                            fill=piece_color, tags=("show_piece"))


# return coordinates of cursor
def coorBack(event):
    global click_x, click_y
    click_x = event.x
    click_y = event.y
    Player(board)


# Transfer indexes
def indexTransfer(x, y):
    if x==35 and y==30:
        return 0
    if x==35 and y==275:
        return 3
    if x==35 and y==520:
        return 5
    if x==133 and y==128:
        return 8
    if x==133 and y==275:
        return 11
    if x==133 and y==422:
        return 13
    if x==231 and y==226:
        return 16
    if x==231 and y==275:
        return 19
    if x==231 and y==324:
        return 21
    if x==280 and y==30:
        return 1
    if x==280 and y==128:
        return 9
    if x==280 and y==226:
        return 17
    if x==280 and y==324:
        return 22
    if x==280 and y==422:
        return 14
    if x==280 and y==520:
        return 6
    if x==329 and y==226:
        return 18
    if x==329 and y==275:
        return 20
    if x==329 and y==324:
        return 23
    if x==427 and y==128:
        return 10
    if x==427 and y==275:
        return 12
    if x==427 and y==422:
        return 15
    if x==525 and y==30:
        return 2
    if x==525 and y==275:
        return 4
    if x==525 and y==520:
        return 7




'''Logic'''


# Put piece to the GUI
def putPiece(piece_color):
    global coor_black, coor_white
    canvas.create_oval(click_x - PIECE_SIZE, click_y - PIECE_SIZE,
                       click_x + PIECE_SIZE, click_y + PIECE_SIZE,
                       fill=piece_color, tags=("piece"))
    if piece_color == "white":
        coor_white.append((click_x, click_y))
    elif piece_color == "black":
        coor_black.append((click_x, click_y))


# Find out the point
def coorJudge():
    global click_x, click_y
    coor = coor_black + coor_white
    global person_flag, show_piece
    # print("x = %s, y = %s" % (click_x, click_y))
    item = canvas.find_closest(click_x, click_y)
    tags_tuple = canvas.gettags(item)
    if len(tags_tuple) > 1:
        tags_list = list(tags_tuple)
        coor_list = tags_list[:2]
        try:
            for i in range(len(coor_list)):
                coor_list[i] = int(coor_list[i])
        except ValueError:
            pass
        else:
            coor_tuple = tuple(coor_list)
            (click_x, click_y) = coor_tuple
            # print("tags = ", tags_tuple, "coors = ", coor_tuple)
            if ((click_x, click_y) not in coor) and (click_x in pieces_x) and (click_y in pieces_y):
                # print("True")
                if person_flag != 0:
                    if person_flag == 1:
                        putPiece("black")
                        showChange("white")
                        var.set("White Player")
                    elif person_flag == -1:
                        putPiece("white")
                        showChange("black")
                        var.set("Black Player")
                    person_flag *= -1
            # else:
            # print("False")



'''
User story 2: Placing pieces (remove one of man from another player
 Haven't done yet


def coorBackRemove(event):
    global click_x, click_y
    click_x = event.x
    click_y = event.y
    RemoveMen(board)


def removePiece(piece_color):
    global coor_black, coor_white
    canvas.create_oval(click_x - PIECE_SIZE, click_y - PIECE_SIZE,
                       click_x + PIECE_SIZE, click_y + PIECE_SIZE,
                       fill="grey", tags=("piece"))
    if piece_color == "white":
        coor_white.append((click_x, click_y))
    elif piece_color == "black":
        coor_black.append((click_x, click_y))

def coorJudgeRemove():
    global click_x, click_y
    coor = coor_black + coor_white
    global person_flag, show_piece
    # print("x = %s, y = %s" % (click_x, click_y))
    item = canvas.find_closest(click_x, click_y)
    tags_tuple = canvas.gettags(item)
    if len(tags_tuple) > 1:
        tags_list = list(tags_tuple)
        coor_list = tags_list[:2]
        try:
            for i in range(len(coor_list)):
                coor_list[i] = int(coor_list[i])
        except ValueError:
            pass
        else:
            coor_tuple = tuple(coor_list)
            (click_x, click_y) = coor_tuple
            # print("tags = ", tags_tuple, "coors = ", coor_tuple)
            if ((click_x, click_y) not in coor) and (click_x in pieces_x) and (click_y in pieces_y):
                # print("True")
                if person_flag != 0:
                    if person_flag == -1:
                        removePiece("white")
                        showChange("white")
                        var.set("White Player")
                    elif person_flag == 1:
                        removePiece("black")
                        showChange("black")
                        var.set("Black Player")
                    person_flag *= -1
'''

def Player(board):
    '''
    User Story 1: Start Nine men's morris game
    '''

    '''
    User Story 2: Placing pieces
    '''
    # White/Black Player has 9 Men


    # White player #1 is playing
    try:

        # Ask user where you want to place a men
        coorJudge()
        pos = int(indexTransfer(click_x, click_y))


        # If the intersection is empty
        if board[pos] == "X":
            if person_flag == -1:
                # Set this to not empty
                board[pos] = '1' # Black
                print(board)
                boardOutput(board)

            elif person_flag == 1:
                # Set this to not empty
                board[pos] = '2' # White
                print(board)
                boardOutput(board)

            '''Haven't done yet'''
            # # Check if it is a mill
            # if isCloseMill(pos, board):
            #     global TF
            #     TF = True

        else:
            print("There is already a piece there")

    except Exception:
        print("Couldn't get the input value")

'''
User story 2: Placing pieces (remove one of man from another player
 Haven't done yet
 
 
def RemoveMen(board):
    canvas.bind("<Button-1>", coorBackRemove)
    coorJudgeRemove()
    pos = int(indexTransfer(click_x, click_y))
    print(pos)

    if person_flag == 1: # Black turn, want to remove a white man
        if board[pos] == "2" and not isCloseMill(pos, board) or (
                isCloseMill(pos, board) and getPiecesInPotentialMillFormation(board, "2") == 3):  # BUG !!!!
            board[pos] = "X"

        else:
            print("Invalid position")
            #RemoveMen(board)

    elif person_flag == -1: # Black turn, want to remove a white man
        if board[pos] == "1" and not isCloseMill(pos, board) or (
                isCloseMill(pos, board) and getPiecesInPotentialMillFormation(board, "1") == 3):  # BUG !!!!
            board[pos] = "X"

        else:
            print("Invalid position")
            #RemoveMen(board)

'''

"""Create a window for playing"""

root = tk.Tk()

root.title("Nine-Men-Morris")
root.geometry("760x560")

"""Display"""
side_canvas = tk.Canvas(root, width=220, height=50)
side_canvas.grid(row=0, column=1)
side_canvas.create_oval(110 - PIECE_SIZE, 25 - PIECE_SIZE,
                        110 + PIECE_SIZE, 25 + PIECE_SIZE,
                        fill=piece_color, tags=("show_piece"))

"""Who is going to play"""
var = tk.StringVar()
var.set("Black Player")
person_label = tk.Label(root, textvariable=var, width=12, anchor=tk.CENTER,
                        font=("Arial", 20))
person_label.grid(row=1, column=1)


"""Display the board"""
# Background
canvas = tk.Canvas(root, bg="grey", width=540, height=540)
canvas.bind("<Button-1>", coorBack)  # Click



canvas.grid(row=0, column=0, rowspan=6)
# Lines
for i in range(3):
    canvas.create_line(35 + i * 98, 30 + i * 98, 525 - i * 98, 30 + i * 98)  # out mid inner line
    canvas.create_line(35 + i * 98, 520 - i * 98, 525 - i * 98, 520 - i * 98)  # out mid inner line
    canvas.create_line(35 + i * 98, 30 + i * 98, 35 + i * 98, 520 - i * 98)  # out mid inner line
    canvas.create_line(525 - i * 98, 30 + i * 98, 525 - i * 98, 520 - i * 98)  # out mid inner line

canvas.create_line(280, 30, 280, 234)  # inter line
canvas.create_line(280, 330, 280, 528)  # inter line
canvas.create_line(35, 275, 231, 275)  # inter line
canvas.create_line(329, 275, 525, 275)  # inter line
# Points

point_x = [35, 35, 35, 133, 133, 133, 231, 231, 231, 280, 280, 280, 280, 280, 280, 329, 329, 329, 427, 427, 427,
           525, 525, 525]
point_y = [30, 275, 520, 128, 275, 422, 226, 275, 324, 30, 128, 226, 324, 422, 520, 226, 275, 324, 128, 275, 422,
           30, 275, 520]
for i in range(24):
    canvas.create_oval(point_x[i] - 4, point_y[i] - 4,
                       point_x[i] + 4, point_y[i] + 4, fill="black")

# Transparent chess pieces (set transparent chess pieces to facilitate the positioning of the coordinates of the subsequent move to the correct position)
for i in pieces_x:
    for j in pieces_y:
        canvas.create_oval(i - PIECE_SIZE, j - PIECE_SIZE,
                           i + PIECE_SIZE, j + PIECE_SIZE,
                           width=0, tags=(str(i), str(j)))

# Num index from 1 to 7
for i in range(7):
    label = tk.Label(canvas, text=str(7 - i), fg="black", bg="grey",
                     width=2, anchor=tk.E)
    label.place(x=2, y=85 * i + 10)
# Later index from a to g
count = 0
for i in range(65, 72):
    label = tk.Label(canvas, text=chr(i), fg="black", bg="grey")
    label.place(x=85 * count + 10, y=525)
    count += 1

"""Loop the window"""

root.mainloop()
