import unittest
from Board import *


class BoardTests:

    # Should initialize board
    def testInitBoard():
        initBoard(self)

    def testGetMan():
        getMan(0)  # Point should be available
        getMan(1)  # Point should be black
        getMan(-1)  # Point should be white
        getMan(2)  # Invalid input

    # Should return player
    def testGetPlayer():
        getPlayer(self)

    # Should change whose turn it is
    def testChangeTurn():
        changeTurn(self)

    def testCountMan():
        countMan(1);  # Should increment count for player 1
        countMan(-1);  # Should increment count for player -1
        countMan(2);  # Invalid input

    # Should place piece
    def testPlacingMan():
        placingMan(self, 0)
        placingMan(self, 1)
        placingMan(self, -1)
        placingMan(self, 3)  # Invalid input

    def testMoveMan():
        moveMan(self, 1, 3)  # Should move black piece
        moveMan(self, 2, 5)  # Should movve white piece
        moveMan(self, 3)  # Invalid input

    def testFlyMan():
        flyMan(self, 0, 1)
        flyMan(self, 1, 1)  # Should bypass try block, print "You cannot fly this man")

    def testIsWin():
        isWin(1)  # Should return true
        isWin(2)  # Should return false

    def testIsMill():
        isMill(self, 1, 1)
        isMill(self, 2, 1)
        isMill(self, -1, 1)

    def testRemoveMan():
        removeMan(0, 1)
        removeMan(1, 1)
        removeMan(3, 1)
        removeMan(-1, 1)  # Invalid input

    def testIndexTransfer():
        indexTransfer(self, 30, 30)  # Should return 0
        indexTransfer(self, 133, 128)  # Should return 8
        indexTransfer(self, 231, 226)  # Should return 16
        indexTransfer(self, 280, 128)  # Should return 9
        indexTransfer(self, 427, 128)  # Should return 10
        indexTransfer(self, 525, 520)  # Should return 7