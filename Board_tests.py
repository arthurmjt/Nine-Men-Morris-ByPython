import unittest
from Board import *


class BoardTests(unittest.TestCase):

    # Should place piece
    def testPlacingMan():
        excepText = "Couldn't get the input value"

        secondTest = placingMan(self, 1)

        self.assertEqual(firstTest, excepText, "Should output " + excepText)

    def testMoveMan():
        moveMan(self, 1, 3)
        moveMan(self, 2, 5)

    def testFlyMan():
        flyMan(self, 0, 1)
        flyMan(self, 1, 1)  # Should bypass try block, print "You cannot fly this man")

    # def testIsWin():
    # firstTest = isWin(2)
    # secondTest = isWin(1)
    # thirdTest = isWin(4)

    # self.assertTrue(firstTest, "Should return true")
    # self.assertFalse(secondTest, "Should return true")
    # self.assertFalse(thirdTest, "Should return false")

    def testIsMill():
        # Player == 0, so this statement should return false
        firstTest = isMill(self, 1, 0)
        self.assertFalse(firstTest, "Should return false")

    def testRemoveMan():
        firstTest = removeMan(1, 10)
        excepText = "Input was either out of bounds or wasn't an integer"

        secondTest = removeMan(1, -1)
        invalText = "Invalid position at: "

        self.assertEqual(firstTest, excepText, "Should output " + excepText)
        self.assertEqual(secondTest, invalText, "Should output " + invalText)

    def testIndexTransfer():
        firstTest = IndexTransfer(self, 35, 30)
        secondTest = IndexTransfer(self, 231, 226)
        thirdTest = IndexTransfer(self, 427, 128)

        self.assertEqual(firstTest, 0, "Should return 0")
        self.assertEqual(secondTest, 16, "Should return 16")
        self.assertEqual(thirdTest, 10, "Should dreturn 10")

    def testAdjacentPos():
        firstTest = adjacentPos(self, 1)
        secondTest = adjacentPos(self, 4)
        thirdTest = adjacentPos(self, 7)

        self.assertEqual(firstTest, [0, 2, 9], "Should return list containing 0, 2, and 9")
        self.assertEqual(secondTest, [2, 7, 12], "Should return list containing 2, 7, and 12")
        self.assertEqual(thirdTest, [4, 6], "Should return list containing 4 and 6")


unittest.main()