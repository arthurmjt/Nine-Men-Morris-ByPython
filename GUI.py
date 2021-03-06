# -*- coding: utf-8 -*-
"""
GUI
@author: Jingtang Ma(Arthur)
"""
import tkinter as tk
import tkinter.messagebox
import random
from Board import *


board = Board()
PIECE_SIZE = 10
piece_color = "black"

'''Global var '''
pieceLeft = 18
movefromIndex = -1
flyfromIndex = -1

'''Each available cell'''
point_x = [35, 280, 525, 35, 525, 35, 280, 525, 133, 280, 427, 133, 427, 133, 280, 427, 231, 280, 329, 231, 329, 231, 280, 329]
point_y = [30, 30, 30, 275, 275, 520, 520, 520, 128, 128, 128, 275, 275, 422, 422, 422, 226, 226, 226, 275, 275, 324, 324, 324]


def boardOutput():
    print(board.boardPoints[0], "(00)----------------------" , board.boardPoints[1] , "(01)----------------------" , board.boardPoints[2] , "(02)");
    print("|                           |                           |");
    print("|       " , board.boardPoints[8] , "(08)--------------" , board.boardPoints[9] , "(09)--------------" , board.boardPoints[10] , "(10)     |");
    print("|       |                   |                    |      |");
    print("|       |                   |                    |      |");
    print("|       |        " , board.boardPoints[16] , "(16)-----" , board.boardPoints[17] , "(17)-----" , board.boardPoints[18] , "(18)       |      |");
    print("|       |         |                   |          |      |");
    print("|       |         |                   |          |      |");
    print(board.boardPoints[3] , "(03)---" , board.boardPoints[11] , "(11)----" , board.boardPoints[19] , "(19)               " , board.boardPoints[20] , "(20)----" ,
          board.boardPoints[12] , "(12)---" , board.boardPoints[4] , "(04)");
    print("|       |         |                   |          |      |");
    print("|       |         |                   |          |      |");
    print("|       |        " , board.boardPoints[21] , "(21)-----" , board.boardPoints[22] , "(22)-----" , board.boardPoints[23] , "(23)       |      |");
    print("|       |                   |                    |      |");
    print("|       |                   |                    |      |");
    print("|       " , board.boardPoints[13] , "(13)--------------" , board.boardPoints[14] , "(14)--------------" , board.boardPoints[15] , "(15)     |");
    print("|                           |                           |");
    print("|                           |                           |");
    print(board.boardPoints[5] , "(05)----------------------" , board.boardPoints[6] , "(06)----------------------" , board.boardPoints[7] , "(07)");







def GUIplacing(event):
    global pieceLeft
    click_x = event.x
    click_y = event.y
    index = board.indexTransfer(click_x, click_y)
    print("Whose turn: ", board.player)
    print("index now: ", index)

    if (board.getMan(index) == 0):
        board.placingMan(index)
        pieceLeft -= 1
        boardOutput()
        if (board.getPlayer() == 1 and board.getMan(index) == 1):
            canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                               point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="black")

        elif (board.getPlayer() == -1 and board.getMan(index) == -1):
            canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                               point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="white")

        if (board.isMill(index, board.getPlayer())):
            print("Mill now, remove one man. Now is turn: ", board.getPlayer())
            varState.set("Remove a Man")
            canvas.bind("<Button-1>", GUIremove)
            print("Why????????")
        else:
            menuChangeColor(board.getPlayer())
            board.changeTurn()

        if (pieceLeft <= 0):
            if (board.isMill(index, board.getPlayer())):
                print("Mill now, remove one man. Now is turn: ", board.getPlayer())
                varState.set("Remove a Man")
                canvas.bind("<Button-1>", GUIremove)
                print("Why????????")

            else:
                print("All men are gone!!!!!!!!!!!!!!!!!!!!!!!!!!")
                varState.set("Moving Man")
                canvas.bind("<Button-1>", GUImovefrom)



def GUIremove(event):
    click_x = event.x
    click_y = event.y
    index = board.indexTransfer(click_x, click_y)
    print("remove index ", index)
    if ((board.getMan(index) == -board.getPlayer())):
        print("!!!!!!!!!!!!")
        if (not board.isMill(index, -board.getPlayer()) or (board.isMill(index, -board.getPlayer()) and board.isAllmill(-board.getPlayer()))):
            board.removeMan(index, board.player)
            boardOutput()
            canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                               point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="saddlebrown")


            print("succful")
            print("now in that pos: ", board.getMan(index))
            menuChangeColor(board.getPlayer())
            board.changeTurn()

            if (pieceLeft <= 0):
                print("All men are gone in remove")
                varState.set("Moving Man")
                canvas.bind("<Button-1>", GUImovefrom)
            else:
                varState.set("Placing Man")
                canvas.bind("<Button-1>", GUIplacing)
        else:
            print("It is in a mill, please reselect one to remove")
    else:
        print("It is your man, cannot be removed, please reselect one to remove")


def GUImovefrom(event):
    global movefromIndex
    click_x = event.x
    click_y = event.y
    movefromIndex = board.indexTransfer(click_x, click_y)
    print("Turn: ", board.getPlayer(), " index ", movefromIndex, " who ", board.getMan(movefromIndex))
    if (board.getMan(movefromIndex) == board.getPlayer()):
        print("USER STORY 3 Move Star")
        varState.set("Moving Man")
        canvas.bind("<Button-1>", GUImoveto)
    else:
        print("It is NOT your man, cannot be moved, please reselect one to move")
        varState.set("Moving Man")
        canvas.bind("<Button-1>", GUImovefrom)

def GUImoveto(event):
    click_x = event.x
    click_y = event.y
    index = board.indexTransfer(click_x, click_y)
    print("move index to: ", index)
    if ((board.getMan(index) == 0)):
        adjacent = board.adjacentPos(movefromIndex)
        if index in adjacent:
            board.moveMan(movefromIndex, index)
            print("move finished")

            if (board.getPlayer() != 0 and board.getMan(movefromIndex) == 0):
                canvas.create_oval(point_x[movefromIndex] - PIECE_SIZE, point_y[movefromIndex] - PIECE_SIZE,
                                   point_x[movefromIndex] + PIECE_SIZE, point_y[movefromIndex] + PIECE_SIZE, fill="saddlebrown")

            if (board.getPlayer() == 1 and board.getMan(index) == 1):
                canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                                   point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="black")
            elif (board.getPlayer() == -1 and board.getMan(index) == -1):
                canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                                   point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="white")

            if (board.isMill(index, board.getPlayer())):
                print("Mill now, remove one man")
                varState.set("Remove Man")
                canvas.bind("<Button-1>", GUIremove2)
            else:
                menuChangeColor(board.getPlayer())
                board.changeTurn()
                varState.set("Moving Man")
                canvas.bind("<Button-1>", GUImovefrom)


        else:
            print(" move not finished, reselect a man to move ")
            varState.set("Moving Man")
            canvas.bind("<Button-1>", GUImovefrom)

    else:
        print("Cannot move to here, reselect a man to move")
        varState.set("Moving Man")
        canvas.bind("<Button-1>", GUImovefrom)


def GUIremove2(event):
    click_x = event.x
    click_y = event.y
    index = board.indexTransfer(click_x, click_y)
    print("remove index ", index)
    if ((board.getMan(index) == -board.getPlayer())):
        print("!!!!!!!!!!!!")
        if (not board.isMill(index, -board.getPlayer()) or (board.isMill(index, -board.getPlayer()) and board.isAllmill(-board.getPlayer()))):
            board.removeMan(index, board.player)
            boardOutput()
            canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                               point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="saddlebrown")
            print("succful")
            print("now in that pos: ", board.getMan(index))
            menuChangeColor(board.getPlayer())
            board.changeTurn()

            if (board.countMan(1) <= 3 or board.countMan(-1) <=3):
                varState.set("Flying Man")
                canvas.bind("<Button-1>", GUIflyfrom)

            else:
                varState.set("Moving Man")
                canvas.bind("<Button-1>", GUImovefrom)

        else:
            print("It is in a mill, please reselect one to remove")
    else:
        print("It is your man, cannot be removed, please reselect one to remove")

def GUIflyfrom(event):
    global flyfromIndex
    click_x = event.x
    click_y = event.y
    flyfromIndex = board.indexTransfer(click_x, click_y)
    if (board.getMan(flyfromIndex) == board.getPlayer()):
        print("USER STORY 4 fly Star")
        varState.set("Flying Man")
        canvas.bind("<Button-1>", GUIflyto)
    else:
        print("It is NOT your man, cannot fly, please reselect one to fly")
        varState.set("Flying Man")
        canvas.bind("<Button-1>", GUIflyfrom)


def GUIflyto(event):
    click_x = event.x
    click_y = event.y
    index = board.indexTransfer(click_x, click_y)
    print("fly index to: ", index)
    if ((board.getMan(index) == 0)):
        if (board.countMan(board.getPlayer()) <= 3):
            # can fly
            board.flyMan(flyfromIndex, index)
            print("fly finished")

            if (board.getPlayer() != 0 and board.getMan(flyfromIndex) == 0):
                canvas.create_oval(point_x[flyfromIndex] - PIECE_SIZE, point_y[flyfromIndex] - PIECE_SIZE,
                                   point_x[flyfromIndex] + PIECE_SIZE, point_y[flyfromIndex] + PIECE_SIZE,
                                   fill="saddlebrown")

            if (board.getPlayer() == 1 and board.getMan(index) == 1):
                canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                                   point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="black")
            elif (board.getPlayer() == -1 and board.getMan(index) == -1):
                canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                                   point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="white")

            if (board.isMill(index, board.getPlayer())):
                print("Mill now, remove one man")
                varState.set("Remove Man")
                canvas.bind("<Button-1>", GUIremove3)
            else:
                menuChangeColor(board.getPlayer())
                board.changeTurn()
                varState.set("Flying Man")
                canvas.bind("<Button-1>", GUIflyfrom)

        else:
            # cannot fly, just move
            adjacent = board.adjacentPos(flyfromIndex)
            if index in adjacent:
                board.moveMan(flyfromIndex, index)
                print("move finished")

                if (board.getPlayer() != 0 and board.getMan(flyfromIndex) == 0):
                    canvas.create_oval(point_x[flyfromIndex] - PIECE_SIZE, point_y[flyfromIndex] - PIECE_SIZE,
                                       point_x[flyfromIndex] + PIECE_SIZE, point_y[flyfromIndex] + PIECE_SIZE,
                                       fill="saddlebrown")

                if (board.getPlayer() == 1 and board.getMan(index) == 1):
                    canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                                       point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="black")
                elif (board.getPlayer() == -1 and board.getMan(index) == -1):
                    canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                                       point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="white")

                if (board.isMill(index, board.getPlayer())):
                    print("Mill now, remove one man")
                    varState.set("Remove Man")
                    canvas.bind("<Button-1>", GUIremove3)
                else:
                    menuChangeColor(board.getPlayer())
                    board.changeTurn()
                    varState.set("Flying Man")
                    canvas.bind("<Button-1>", GUIflyfrom)


            else:
                print(" move not finished, reselect a man to move ")
                varState.set("Flying Man")
                canvas.bind("<Button-1>", GUIflyfrom)

    else:
        print("Cannot fly to here, reselect a man to move")
        varState.set("Flying Man")
        canvas.bind("<Button-1>", GUIflyfrom)


def GUIremove3(event):
    click_x = event.x
    click_y = event.y
    index = board.indexTransfer(click_x, click_y)
    print("remove index ", index)
    if ((board.getMan(index) == -board.getPlayer())):
        print("???????????")
        if (not board.isMill(index, -board.getPlayer()) or (board.isMill(index, -board.getPlayer()) and board.isAllmill(-board.getPlayer()))):
            board.removeMan(index, board.player)
            boardOutput()
            canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                               point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="saddlebrown")
            print("succful")
            print("now in that pos: ", board.getMan(index))
            if (not board.isWin()):
                menuChangeColor(board.getPlayer())
                board.changeTurn()
                varState.set("Flying Man")
                canvas.bind("<Button-1>", GUIflyfrom)
            else:
                GUIwin()

        else:
            print("It is in a mill, please reselect one to remove")
    else:
        print("It is your man, cannot be removed, please reselect one to remove")


def GUIwin():
    if (board.getPlayer() == 1):
        print("Black Win")
        varState.set("Black player Win$$$")
    elif (board.getPlayer() == -1):
        print("White player Win$$$")
        varState.set("White Win")
    else:
        print("Nobody Win***")
        varState.set("Nobody Win***")

    print("Game over")







''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
AI VS Human
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def GUIHumplacing(event):
    global pieceLeft
    click_x = event.x
    click_y = event.y
    index = board.indexTransfer(click_x, click_y)

    if (board.getMan(index) == 0):
        board.placingMan(index)
        pieceLeft -= 1
        boardOutput()

        canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                            point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="black")

        if (board.isMill(index, board.getPlayer())):
            varState.set("Remove a Man")
            canvas.bind("<Button-1>", GUIHumremove)
        else:
            menuChangeColor(board.getPlayer())
            board.changeTurn()
            GUIAIplacing()


def GUIAIplacing():
    global pieceLeft
    index = random.randint(0,23)
    while (board.getMan(index) != 0):
        index = random.randint(0, 23)

    if (board.getMan(index) == 0):
        board.placingMan(index)
        pieceLeft -= 1
        boardOutput()

        canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                               point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="white")

        if (board.isMill(index, board.getPlayer())):
            varState.set("Remove a Man")
            GUIAIremove()
        else:
            if (pieceLeft <= 0):
                print("All men are gone!!!!!!!!!!!!!!!!!!!!!!!!!!")
                menuChangeColor(board.getPlayer())
                board.changeTurn()
                varState.set("Moving Man")
                canvas.bind("<Button-1>", GUIHummovefrom)
            else:
                menuChangeColor(board.getPlayer())
                board.changeTurn()
                print("ask Hum placing")
                canvas.bind("<Button-1>", GUIHumplacing)


def GUIHumremove(event):
    click_x = event.x
    click_y = event.y
    index = board.indexTransfer(click_x, click_y)
    if ((board.getMan(index) == -board.getPlayer())):
        if (not board.isMill(index, -board.getPlayer()) or (board.isMill(index, -board.getPlayer()) and board.isAllmill(-board.getPlayer()))):
            board.removeMan(index, board.player)
            boardOutput()
            canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                               point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="saddlebrown")


            menuChangeColor(board.getPlayer())
            board.changeTurn()
            print("hum remove")
            varState.set("Placing Man")
            GUIAIplacing()
        else:
            print("It is in a mill, please reselect one to remove")
    else:
        print("It is your man, cannot be removed, please reselect one to remove")

def GUIAIremove():
    index = random.randint(0, 23)
    while (board.getMan(index) != -board.getPlayer() or
            board.isMill(index, -board.getPlayer()) and
            not (board.isMill(index, -board.getPlayer()) and board.isAllmill(-board.getPlayer()))):
        index = random.randint(0, 23)
        print("AI remove index", index)

    board.removeMan(index, board.player)
    boardOutput()
    canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                       point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="saddlebrown")


    menuChangeColor(board.getPlayer())
    board.changeTurn()

    if (pieceLeft <= 0):
        varState.set("Moving Man")
        canvas.bind("<Button-1>", GUIHummovefrom)
    else:
        varState.set("Placing Man")
        canvas.bind("<Button-1>", GUIHumplacing)



def GUIHummovefrom(event):
    global movefromIndex
    click_x = event.x
    click_y = event.y
    movefromIndex = board.indexTransfer(click_x, click_y)
    print("Turn: ", board.getPlayer(), " index ", movefromIndex, " who ", board.getMan(movefromIndex))
    if (board.getMan(movefromIndex) == board.getPlayer()):
        print("USER STORY 3 Move Star in hum move from")
        varState.set("Moving Man")
        canvas.bind("<Button-1>", GUIHummoveto)
    else:
        print("It is NOT your man, cannot be moved, please reselect one to move")
        varState.set("Moving Man")
        canvas.bind("<Button-1>", GUIHummovefrom)


def GUIAImovefrom():
    global movefromIndex
    movefromIndex = random.randint(0,23)
    while (board.getMan(movefromIndex) != board.getPlayer()):
        movefromIndex = random.randint(0, 23)

    print("USER STORY 3 Move Star in AI move from")
    varState.set("Moving Man")
    GUIAImoveto()

def GUIHummoveto(event):
    click_x = event.x
    click_y = event.y
    index = board.indexTransfer(click_x, click_y)
    print("move index to: ", index)
    if ((board.getMan(index) == 0)):
        adjacent = board.adjacentPos(movefromIndex)
        if index in adjacent:
            board.moveMan(movefromIndex, index)
            print("move finished")

            canvas.create_oval(point_x[movefromIndex] - PIECE_SIZE, point_y[movefromIndex] - PIECE_SIZE,
                               point_x[movefromIndex] + PIECE_SIZE, point_y[movefromIndex] + PIECE_SIZE, fill="saddlebrown")
            canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                               point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="black")

            if (board.isMill(index, board.getPlayer())):
                print("Mill now, remove one man")
                varState.set("Remove Man")
                canvas.bind("<Button-1>", GUIHumremove2)
            else:
                menuChangeColor(board.getPlayer()) # !!!
                board.changeTurn()
                varState.set("Moving Man")
                print("Hum move end")
                GUIAImovefrom()

        else:
            print(" move not finished, reselect a man to move ")
            varState.set("Moving Man")
            canvas.bind("<Button-1>", GUIHummovefrom)

    else:
        print("Cannot move to here, reselect a man to move")
        varState.set("Moving Man")
        canvas.bind("<Button-1>", GUIHummovefrom)

def GUIAImoveto():
    index = -1
    TF = True
    adjacent = board.adjacentPos(movefromIndex)
    for i in adjacent:
        if (board.getMan(i) == 0):
            index = i
            board.moveMan(movefromIndex, index)
            TF = False
            break

    if (TF):
        varState.set("Moving Man")
        GUIAImovefrom()

    else:
        canvas.create_oval(point_x[movefromIndex] - PIECE_SIZE, point_y[movefromIndex] - PIECE_SIZE,
                           point_x[movefromIndex] + PIECE_SIZE, point_y[movefromIndex] + PIECE_SIZE, fill="saddlebrown")
        canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                               point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="white")

        if (board.isMill(index, board.getPlayer())):
            print("Mill now, remove one man")
            varState.set("Remove Man")
            GUIAIremove2()
        else:
            menuChangeColor(board.getPlayer())
            board.changeTurn()
            varState.set("Moving Man")
            print("AI move end")
            canvas.bind("<Button-1>", GUIHummovefrom)



def GUIHumremove2(event):
    click_x = event.x
    click_y = event.y
    index = board.indexTransfer(click_x, click_y)
    print("remove index ", index)
    if ((board.getMan(index) == -board.getPlayer())):
        print("!!!!!!!!!!!!")
        if (not board.isMill(index, -board.getPlayer()) or (board.isMill(index, -board.getPlayer()) and board.isAllmill(-board.getPlayer()))):
            board.removeMan(index, board.player)
            boardOutput()
            canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                               point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="saddlebrown")
            print("succful")
            print("now in that pos: ", board.getMan(index))
            menuChangeColor(board.getPlayer())
            board.changeTurn()
            print("Hum remove end")
            if (board.countMan(-1) <=3):
                varState.set("Flying Man")
                GUIAIflyfrom()
            else:
                varState.set("Moving Man")
                GUIAImovefrom()

        else:
            print("It is in a mill, please reselect one to remove")
    else:
        print("It is your man, cannot be removed, please reselect one to remove")


def GUIAIremove2():
    index = random.randint(0, 23)
    while (board.getMan(index) != -board.getPlayer() or
            board.isMill(index, -board.getPlayer()) and
            not (board.isMill(index, -board.getPlayer()) and board.isAllmill(-board.getPlayer()))):
        index = random.randint(0, 23)
        print("AI remove index", index)

    board.removeMan(index, board.player)
    boardOutput()
    canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                       point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="saddlebrown")

    menuChangeColor(board.getPlayer())
    board.changeTurn()
    print("AI remove end")
    if (board.countMan(1) <=3):
        varState.set("Flying Man")
        canvas.bind("<Button-1>", GUIHumflyfrom)
    else:
        varState.set("Moving Man")
        canvas.bind("<Button-1>", GUIHummovefrom)


def GUIHumflyfrom(event):
    global flyfromIndex
    click_x = event.x
    click_y = event.y
    flyfromIndex = board.indexTransfer(click_x, click_y)
    if (board.getMan(flyfromIndex) == board.getPlayer()):
        print("USER STORY 4 fly Star")
        varState.set("Flying Man")
        canvas.bind("<Button-1>", GUIHumflyto)
    else:
        print("It is NOT your man, cannot fly, please reselect one to fly")
        varState.set("Flying Man")
        canvas.bind("<Button-1>", GUIHumflyfrom)

def GUIAIflyfrom():
    global flyfromIndex
    flyfromIndex = random.randint(0,23)
    while (board.getMan(flyfromIndex) != board.getPlayer()):
        flyfromIndex = random.randint(0, 23)

    print("USER STORY 4 fly Star")
    varState.set("Flying Man")
    GUIAIflyto()


def GUIHumflyto(event):
    click_x = event.x
    click_y = event.y
    index = board.indexTransfer(click_x, click_y)
    print("fly index to: ", index)
    if ((board.getMan(index) == 0)):
        if (board.countMan(board.getPlayer()) <= 3):
            # can fly
            board.flyMan(flyfromIndex, index)
            print("fly finished")

            canvas.create_oval(point_x[flyfromIndex] - PIECE_SIZE, point_y[flyfromIndex] - PIECE_SIZE,
                               point_x[flyfromIndex] + PIECE_SIZE, point_y[flyfromIndex] + PIECE_SIZE,
                               fill="saddlebrown")
            canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                               point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="black")


            if (board.isMill(index, board.getPlayer())):
                print("Mill now, remove one man")
                varState.set("Remove Man")
                canvas.bind("<Button-1>", GUIHumremove3)
            else:
                menuChangeColor(board.getPlayer())
                board.changeTurn()
                varState.set("Flying Man")
                GUIAIflyfrom()

        else:
            # cannot fly, just move
            adjacent = board.adjacentPos(flyfromIndex)
            if index in adjacent:
                board.moveMan(flyfromIndex, index)
                print("move finished")


                canvas.create_oval(point_x[flyfromIndex] - PIECE_SIZE, point_y[flyfromIndex] - PIECE_SIZE,
                                   point_x[flyfromIndex] + PIECE_SIZE, point_y[flyfromIndex] + PIECE_SIZE,
                                   fill="saddlebrown")
                canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                                   point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="black")

                if (board.isMill(index, board.getPlayer())):
                    print("Mill now, remove one man")
                    varState.set("Remove Man")
                    canvas.bind("<Button-1>", GUIHumremove3)
                else:
                    menuChangeColor(board.getPlayer())
                    board.changeTurn()
                    varState.set("Flying Man")
                    GUIAIflyfrom()


            else:
                print(" move not finished, reselect a man to move ")
                varState.set("Flying Man")
                canvas.bind("<Button-1>", GUIHumflyfrom)

    else:
        print("Cannot fly to here, reselect a man to move")
        varState.set("Flying Man")
        canvas.bind("<Button-1>", GUIHumflyfrom)


def GUIAIflyto():
    if (board.countMan(board.getPlayer()) <= 3):
        # can fly
        index = random.randint(0, 23)
        while ((board.getMan(index) != 0)):
            index = random.randint(0, 23)

        board.flyMan(flyfromIndex, index)
        print("fly finished")


        canvas.create_oval(point_x[flyfromIndex] - PIECE_SIZE, point_y[flyfromIndex] - PIECE_SIZE,
                           point_x[flyfromIndex] + PIECE_SIZE, point_y[flyfromIndex] + PIECE_SIZE,
                           fill="saddlebrown")

        canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                           point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="white")

        if (board.isMill(index, board.getPlayer())):
            print("Mill now, remove one man")
            varState.set("Remove Man")
            GUIAIremove3()
        else:
            menuChangeColor(board.getPlayer())
            board.changeTurn()
            varState.set("Flying Man")
            canvas.bind("<Button-1>", GUIHumflyfrom)

    else:
        # cannot fly, just move
        TF = True
        adjacent = board.adjacentPos(flyfromIndex)
        for i in adjacent:
            if (board.getMan(i) == 0):
                index = i
                board.moveMan(flyfromIndex, index)
                TF = False
                break

        if (TF):
            varState.set("Moving Man")
            GUIAIflyfrom()

        else:

            canvas.create_oval(point_x[flyfromIndex] - PIECE_SIZE, point_y[flyfromIndex] - PIECE_SIZE,
                               point_x[flyfromIndex] + PIECE_SIZE, point_y[flyfromIndex] + PIECE_SIZE,
                               fill="saddlebrown")

            canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                               point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="white")

            if (board.isMill(index, board.getPlayer())):
                print("Mill now, remove one man")
                varState.set("Remove Man")
                canvas.bind("<Button-1>", GUIAIremove3)
            else:
                menuChangeColor(board.getPlayer())
                board.changeTurn()
                varState.set("Flying Man")
                canvas.bind("<Button-1>", GUIHumflyfrom)

def GUIHumremove3(event):
    click_x = event.x
    click_y = event.y
    index = board.indexTransfer(click_x, click_y)
    print("remove index ", index)
    if ((board.getMan(index) == -board.getPlayer())):
        print("???????????")
        if (not board.isMill(index, -board.getPlayer()) or (board.isMill(index, -board.getPlayer()) and board.isAllmill(-board.getPlayer()))):
            board.removeMan(index, board.player)
            boardOutput()
            canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                               point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="saddlebrown")
            print("succful")
            print("now in that pos: ", board.getMan(index))
            if (not board.isWin()):
                menuChangeColor(board.getPlayer())
                board.changeTurn()
                varState.set("Flying Man")
                GUIAIflyfrom()
            else:
                GUIwin()

        else:
            print("It is in a mill, please reselect one to remove")
    else:
        print("It is your man, cannot be removed, please reselect one to remove")

def GUIAIremove3():
    index = random.randint(0, 23)
    while (board.getMan(index) != -board.getPlayer() or
            board.isMill(index, -board.getPlayer()) and
            not (board.isMill(index, -board.getPlayer()) and board.isAllmill(-board.getPlayer()))):
        index = random.randint(0, 23)
        print("AI remove index", index)


    board.removeMan(index, board.player)
    boardOutput()
    canvas.create_oval(point_x[index] - PIECE_SIZE, point_y[index] - PIECE_SIZE,
                       point_x[index] + PIECE_SIZE, point_y[index] + PIECE_SIZE, fill="saddlebrown")
    print("succful")
    print("now in that pos: ", board.getMan(index))
    if (not board.isWin()):
        menuChangeColor(board.getPlayer())
        board.changeTurn()
        varState.set("Flying Man")
        canvas.bind("<Button-1>", GUIHumflyfrom)
    else:
        GUIwin()



def GUIwin():
    if (board.getPlayer() == 1):
        print("Black Win")
        varState.set("Black player Win")
    elif (board.getPlayer() == -1):
        print("White player Win")
        varState.set("White Win")
    else:
        print("Nobody Win***")
        varState.set("Nobody Win")

    print("Game over")






"""Create a window for playing"""
window = tk.Tk()
window.title("Nine-Men-Morris")
window.geometry("760x560")

"""Display the board"""
# Background
canvas = tk.Canvas(window, bg="saddlebrown", width=540, height=540)
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
for i in range(24):
    canvas.create_oval(point_x[i] - PIECE_SIZE, point_y[i] - PIECE_SIZE,
                       point_x[i] + PIECE_SIZE, point_y[i] + PIECE_SIZE, fill="saddlebrown")

# Transparent chess pieces (set transparent chess pieces to facilitate the positioning of the coordinates of the subsequent move to the correct position)
for i in point_x:
    for j in point_x:
        canvas.create_oval(i - PIECE_SIZE, j - PIECE_SIZE,
                           i + PIECE_SIZE, j + PIECE_SIZE,
                           width=0, tags=(str(i), str(j)))

# Num index from 1 to 7
for i in range(7):
    label = tk.Label(canvas, text=str(7 - i), fg="black", bg="saddlebrown",
                     width=2, anchor=tk.E)
    label.place(x=2, y=85 * i + 10)

# Later index from a to g
count = 0
for i in range(65, 72):
    label = tk.Label(canvas, text=chr(i), fg="black", bg="saddlebrown")
    label.place(x=85 * count + 10, y=525)
    count += 1


'''Display the Menu'''
def menuChangeColor(player):
    global piece_color
    if (player == 1):
        varTrun.set("White Player's Turn")
        piece_color = "White"
        canvas_side.delete("show_piece")
        canvas_side.create_oval(110 - PIECE_SIZE, 25 - PIECE_SIZE,
                                110 + PIECE_SIZE, 25 + PIECE_SIZE,
                                fill=piece_color, tags=("show_piece"))
    elif (player == -1):
        varTrun.set("Black Player's Turn")
        piece_color = "Black"
        canvas_side.delete("show_piece")
        canvas_side.create_oval(110 - PIECE_SIZE, 25 - PIECE_SIZE,
                                110 + PIECE_SIZE, 25 + PIECE_SIZE,
                                fill=piece_color, tags=("show_piece"))
    else:
        return



# Display the colour of man
canvas_side = tk.Canvas(window, width=220, height=50)
canvas_side.grid(row=0, column=1)
canvas_side.create_oval(110 - PIECE_SIZE, 25 - PIECE_SIZE,
                        110 + PIECE_SIZE, 25 + PIECE_SIZE,
                        fill=piece_color , tags=("show_piece"))

# Display the turn
varTrun = tk.StringVar()
varTrun.set("Black Player's Turn")
person_label = tk.Label(window, textvariable=varTrun, width=15, anchor=tk.CENTER,
                        font=("Arial", 16))
person_label.grid(row=1, column=1)

# State
varState = tk.StringVar()
varState.set("Placing Man")
result_label = tk.Label(window, textvariable=varState, width=12, height=4,
                        anchor=tk.CENTER, fg="red", font=("Arial", 20))
result_label.grid(row=2, column=1, rowspan=2)

def hitHum():
    tk.messagebox.showinfo(title='Message', message='Start with Human VS Human')
    canvas.bind("<Button-1>", GUIplacing)  # Click

def hitAI():
    tk.messagebox.showinfo(title='Message', message='Start with AI VS Human')
    canvas.bind("<Button-1>", GUIHumplacing)  # Click



'''Main'''
board.initBoard()
buttonHum = tk.Button(window, text='Human', bg='green', font=("Arial", 20), width=8, command=hitHum)
buttonAI = tk.Button(window, text='AI', bg='red', font=("Arial", 20), width=8, command=hitAI)
buttonHum.grid(row=4, column=1)
buttonAI.grid(row=5, column=1)


window.mainloop()