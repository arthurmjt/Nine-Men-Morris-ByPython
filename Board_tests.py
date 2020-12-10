# -*- coding: utf-8 -*-
"""
Unittest
@author: Brennan Campbell
"""
import unittest
from unittest.mock import Mock
from Board import *


class BoardTests(unittest.TestCase):

    def testPlacingMan(self):
        boardPoints = Mock()
        Board.placingMan(self, 0)
        Board.placingMan(self, 2)

    def testMoveMan(self):
        boardPoints = Mock()
        Board.moveMan(self, 0, 1)
        Board.moveMan(self, 1, 2)

    def testFlyMan(self):
        boardPoints = Mock()
        Board.flyMan(self, 0, 1)
        Board.flyMan(self, 1, 3)

    # ERROR
    def testIsWin(self):
        firstTest = Board.isWin(self)
        secondTest = Board.isWin(self)
        thirdTest = Board.isWin(self)

        self.assertTrue(firstTest, "Should return true")
        self.assertFalse(secondTest, "Should return false")
        self.assertFalse(thirdTest, "Should return false")

    def testIsMill(self):
        firstTest = Board.isMill(self, 1, 1)
        self.assertFalse(firstTest, "Should return false")

        secondTest = Board.isMill(self, 14, 1)
        self.assertTrue(secondTest, "Should return true")

    def testRemoveMan(self):
        boardPoints = Mock()
        Board.placingMan(self, 0)
        Board.removeMan(self, 0, 1)
        Board.removeMan(self, 25, 1)

    def testIndexTransfer(self):
        firstTest = Board.indexTransfer(self, 35, 30)
        secondTest = Board.indexTransfer(self, 231, 226)
        thirdTest = Board.indexTransfer(self, 427, 128)

        self.assertEqual(firstTest, 0, "Should return 0")
        self.assertEqual(secondTest, 16, "Should return 16")
        self.assertEqual(thirdTest, 10, "Should dreturn 10")

    def testAdjacentPos(self):
        firstTest = Board.adjacentPos(self, 1)
        secondTest = Board.adjacentPos(self, 4)
        thirdTest = Board.adjacentPos(self, 7)

        self.assertEqual(firstTest, [0, 2, 9], "Should return list containing 0, 2, and 9")
        self.assertEqual(secondTest, [2, 7, 12], "Should return list containing 2, 7, and 12")
        self.assertEqual(thirdTest, [4, 6], "Should return list containing 4 and 6")