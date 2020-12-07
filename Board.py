# -*- coding: utf-8 -*-
"""
Board
@author: Jingtang Ma(Arthur)
"""
class Board():
    def __init__(self):
        self.boardPoints = []
        self.player = 1 # Black player first

    '''initial the board, make each point = 0'''
    def initBoard(self):
        for i in range(24):
            self.boardPoints.append(0)

    '''
    Return 0 means the point is available at that pos
    Return 1 means the point is black at that pos
    Return -1 means the point is white at that pos
    @param pos: the index of the position we're checking
    '''
    def getMan(self, pos): return self.boardPoints[pos]

    def getPlayer(self): return self.player

    '''
    Change the turn
    '''
    def changeTurn(self): self.player *= -1

    '''
    Count number of men for a player
    '''
    def countMan(self, player):
        count = 0
        if (player == 1):
            for i in range(24):
                if (self.boardPoints[i] == 1):
                    count += 1
            return count

        elif (player == -1):
            for i in range(24):
                if (self.boardPoints[i] == -1):
                    count += 1
            return count

        else:
            return 0

    '''
    Placing a man to the position by the player
    @param pos: the index of the position we're checking
    '''
    '''ONE BUG NEED TO BE FIXED: CANNOT REMOVE A MAN FROM A MILL WHEN THERE IS NOT A MAN WHICH IS NOT FROM A MILL'''
    def placingMan(self, pos):
        try:
            # the point is empty
            if self.boardPoints[pos] == 0:

                # if it is black player turn
                if self.player == 1:
                    self.boardPoints[pos] = 1
                    #self.player *= -1 # change the turn

                # if it is white player turn
                else:
                    self.boardPoints[pos] = -1
                    #self.player *= -1 # change the turn

            else:
                print("There is already a piece there")

        except Exception:
            print("Couldn't get the input value")


    '''
    Move a man to a new position bu the player
    @param pos: the index of the position we select
    @param topos: the index of the position we want a man to be 
    '''
    def moveMan(self, pos, topos):
        try:
            # the point is not empty
            if self.boardPoints[pos] != 0:

                try:
                    if self.boardPoints[topos] == 0:

                        # check if the point is adjacent point
                        adjacent = self.adjacentPos(pos)
                        if topos in adjacent:

                            # if it is black player turn
                            if self.player == 1:
                                self.boardPoints[pos] = 0
                                self.boardPoints[topos] = 1

                            # if it is white player turn
                            else:
                                self.boardPoints[pos] = 0
                                self.boardPoints[topos] = -1

                        else:
                            print("You can ONLY move the man to adjacent points")
                    else:
                        print("You cannot move there")

                except Exception:
                    print("You cannot move there")

            else:
                print("You cannot move this man")

        except Exception:
            print("You cannot move this man")


    '''
    fly a man to a new position bu the player
    @param pos: the index of the position we select
    @param topos: the index of the position we want a man to be 
    '''
    def flyMan(self, pos, topos):
        try:
            # the point is not empty
            if self.boardPoints[pos] != 0:

                try:
                    if self.boardPoints[topos] == 0:

                        # if it is black player turn
                        if self.player == 1:
                            self.boardPoints[pos] = 0
                            self.boardPoints[topos] = 1

                        # if it is white player turn
                        else:
                            self.boardPoints[pos] = 0
                            self.boardPoints[topos] = -1

                    else:
                        print("You cannot fly there")

                except Exception:
                    print("You cannot fly there")

            else:
                print("You cannot fly this man")

        except Exception:
            print("You cannot fly this man")


    '''
    Return true if someone win the game
    Return false if nobody win th game
    '''
    def isWin(self):
        if (self.countMan(1) <= 2):
            return True
        elif (self.countMan(-1) <= 2):
            return True
        else:
            return False


    '''
    Check if it is a mill or not when the player placed a man here
    Return true if any player has a mill on position
    @param pos: the index of the position we're checking
    '''
    def isMill(self, pos, player):
        def check(p, pos1, pos2):
            '''
            Return True if pos1 and pos2 on board both belong to player
            @param player: string representation of the board piece color
            @param board: current list
            @param pos1: first position index
            @param pos2: second position index
            '''

            if (self.boardPoints[pos1] == p and self.boardPoints[pos2] == p and self.boardPoints[pos] == p):
                return True
            else:
                return False

        if (player != 0):
            if (player == 1):
                mill = [
                    (check(1, 1, 2) or check(1, 3, 5)), # 0
                    (check(1, 0, 2) or check(1, 9, 17)), # 1
                    (check(1, 0, 1) or check(1, 4, 7)),
                    (check(1, 0, 5) or check(1, 11, 19)),
                    (check(1, 2, 7) or check(1, 12, 20)),
                    (check(1, 0, 3) or check(1, 6, 7)),
                    (check(1, 5, 7) or check(1, 14, 22)),
                    (check(1, 2, 4) or check(1, 5, 6)),
                    (check(1, 9, 10) or check(1, 11, 13)),
                    (check(1, 8, 10) or check(1, 1, 17)),
                    (check(1, 8, 9) or check(1, 12, 15)),
                    (check(1, 3, 19) or check(1, 8, 13)),
                    (check(1, 20, 4) or check(1, 10, 15)),
                    (check(1, 8, 11) or check(1, 14, 15)),
                    (check(1, 13, 15) or check(1, 6, 22)),
                    (check(1, 13, 14) or check(1, 10, 12)),
                    (check(1, 17, 18) or check(1, 19, 21)),
                    (check(1, 1, 9) or check(1, 16, 18)),
                    (check(1, 16, 17) or check(1, 20, 23)),
                    (check(1, 16, 21) or check(1, 3, 11)),
                    (check(1, 12, 4) or check(1, 18, 23)),
                    (check(1, 16, 19) or check(1, 22, 23)),
                    (check(1, 6, 14) or check(1, 21, 23)),
                    (check(1, 18, 20) or check(1, 21, 22)), # 23
                ]
                #print("ismill: ", pos, mill[pos])
                return mill[pos]

            elif (player == -1):
                mill = [
                    (check(-1, 1, 2) or check(-1, 3, 5)),
                    (check(-1, 0, 2) or check(-1, 9, 17)),
                    (check(-1, 0, 1) or check(-1, 4, 7)),
                    (check(-1, 0, 5) or check(-1, 11, 19)),
                    (check(-1, 2, 7) or check(-1, 12, 20)),
                    (check(-1, 0, 3) or check(-1, 6, 7)),
                    (check(-1, 5, 7) or check(-1, 14, 22)),
                    (check(-1, 2, 4) or check(-1, 5, 6)),
                    (check(-1, 9, 10) or check(-1, 11, 13)),
                    (check(-1, 8, 10) or check(-1, 1, 17)),
                    (check(-1, 8, 9) or check(-1, 12, 15)),
                    (check(-1, 3, 19) or check(-1, 8, 13)),
                    (check(-1, 20, 4) or check(-1, 10, 15)),
                    (check(-1, 8, 11) or check(-1, 14, 15)),
                    (check(-1, 13, 15) or check(-1, 6, 22)),
                    (check(-1, 13, 14) or check(-1, 10, 12)),
                    (check(-1, 17, 18) or check(-1, 19, 21)),
                    (check(-1, 1, 9) or check(-1, 16, 18)),
                    (check(-1, 16, 17) or check(-1, 20, 23)),
                    (check(-1, 16, 21) or check(-1, 3, 11)),
                    (check(-1, 12, 4) or check(-1, 18, 23)),
                    (check(-1, 16, 19) or check(-1, 22, 23)),
                    (check(-1, 6, 14) or check(-1, 21, 23)),
                    (check(-1, 18, 20) or check(-1, 21, 22)),
                ]
                #print("ismill: ", mill[pos])
                return mill[pos]
            else:
                return False

        return False

    '''
    Return true if the player has all mills
    Return false if the player has least one of men that is not in a mill
    '''
    def isAllmill(self, player):
        count = 0
        num = self.countMan(player)
        # count number of mills
        for i in range(24):
            print("ismill: ", i, self.isMill(i, player))
            if (self.isMill(i, player)):
                count += 1
        print("count: ", count)
        # Check here
        if (num == 3 and count == 3):
            print("All mill, can remove one with: ", num, count)
            return True

        elif(num == 5 and count == 5):
            print("All mill, can remove one with: ", num, count)
            return True

        elif(num == 6 and count == 6):
            print("All mill, can remove one with: ", num, count)
            return True

        elif(num == 7 and count == 7):
            print("All mill, can remove one with: ", num, count)
            return True

        elif(num == 8 and count == 8):
            print("All mill, can remove one with: ", num, count)
            return True

        elif(num == 9 and count == 9):
            print("All mill, can remove one with: ", num, count)
            return True

        else:
            print("Nor All mill with: ", num, count)
            return False




    '''
    Given a pos and a player who you want to remove a man from, remove it
    '''
    def removeMan(self, pos, player):
        try:
            if self.boardPoints[pos] == -player:
                self.boardPoints[pos] = 0

            else: print("Invalid position at: ", pos)

        except Exception:
            print("Input was either out of bounds or wasn't an integer")

    # Transfer indexes
    def indexTransfer(self, x, y):
        if (x >= 25 and x <= 45) and (y >=20 and y <= 40): # (35,30)
            return 0
        elif (x >= 25 and x <=45) and (y >= 265 and y <= 285): # (35,275)
            return 3
        elif (x >= 25 and x <= 45) and (y >= 510 and y <= 530): # (35,520)
            return 5
        elif (x >= 123 and x <= 143) and (y >= 118 and y <= 138): # (133,128)
            return 8
        elif (x >= 123 and x <= 143) and (y >= 265 and y <= 285): # (133,275)
            return 11
        elif (x >= 123 and x <= 143) and (y >= 412 and y <= 432): # (133,422)
            return 13
        elif (x >= 221 and x <= 241) and (y >= 216 and y <= 236): # (231, 226)
            return 16
        elif (x >= 221 and x <= 241) and (y >= 265 and y <= 285): # (231, 275)
            return 19
        elif (x >= 221 and x <= 241) and (y >= 314 and y <= 334): # (231, 324)
            return 21
        elif (x >= 270 and x <= 290) and (y >=20 and y <= 40): # (280,30)
            return 1
        elif (x >= 270 and x <= 290) and (y >= 118 and y <= 138): # (280,128)
            return 9
        elif (x >= 270 and x <= 290) and (y >= 216 and y <= 236): # (280,226)
            return 17
        elif (x >= 270 and x <= 290) and (y >= 314 and y <= 334): # (280,324)
            return 22
        elif (x >= 270 and x <= 290) and (y >= 412 and y <= 432): # (280,422)
            return 14
        elif (x >= 270 and x <= 290) and (y >= 510 and y <= 530): # (280,520)
            return 6
        elif (x >= 319 and x <= 339) and (y >= 216 and y <= 236): # (329,226)
            return 18
        elif (x >= 319 and x <= 339) and (y >= 265 and y <= 285): # (329,275)
            return 20
        elif (x >= 319 and x <= 339) and (y >= 314 and y <= 334): # (329,324)
            return 23
        elif (x >= 417 and x <= 437) and (y >= 118 and y <= 138): # (427,128)
            return 10
        elif (x >= 417 and x <= 437) and (y >= 265 and y <= 285): # (427,275)
            return 12
        elif (x >= 417 and x <= 437) and (y >= 412 and y <= 432): # (427,422)
            return 15
        elif (x >= 515 and x <= 535) and (y >=20 and y <= 40): # (525,30)
            return 2
        elif (x >= 515 and x <= 535) and (y >= 265 and y <= 285): # (525,275)
            return 4
        elif (x >= 515 and x <= 535) and (y >= 510 and y <= 530): # (525,520)
            return 7
        else:
            return



    '''
    Return pieces adjacent to the piece at position
    @param position: index of the piece
    '''
    def adjacentPos(self, pos):

        adjacent = [
            [1, 3],
            [0, 2, 9],
            [1, 4],
            [0, 5, 11],
            [2, 7, 12],
            [3, 6],
            [5, 7, 14],
            [4, 6],
            [9, 11],
            [1, 8, 10, 17],
            [9, 12],
            [3, 8, 13, 19],
            [4, 10, 15, 20],
            [11, 14],
            [6, 13, 15, 22],
            [12, 14],
            [17, 19],
            [9, 16, 18],
            [17, 20],
            [11, 16, 21],
            [12, 18, 23],
            [19, 22],
            [21, 23, 14],
            [20, 22]
        ]
        return adjacent[pos]