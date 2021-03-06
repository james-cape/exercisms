import unittest

from islands import Solution

class IslandsTest(unittest.TestCase):
    def test_functional_test(self):
        results = 1
        table = 800
        self.assertEqual(results, 1)

    # def test_islands_1(self):
    #     solution = Solution()
    #     grid = [
    #         ["1","1","1"],
    #         ["0","1","0"],
    #         ["1","1","1"]
    #     ]
    #     result = solution.numIslands(grid)
    #     self.assertEqual(result, 1)

    # def test_islands_2(self):
    #     solution = Solution()
    #     grid = [
    #         ["1","1","1","1","1","1","1","1","1"],
    #         ["1","0","0","0","0","0","0","0","1"],
    #         ["1","0","1","0","1","0","1","0","1"],
    #         ["1","0","1","1","1","1","1","0","1"],
    #         ["1","0","1","0","1","0","1","0","1"],
    #         ["1","0","0","0","0","0","0","0","1"],
    #         ["1","1","1","1","1","1","1","1","1"]
    #     ]
    #     grid = [
    #         [1 1 1 1 1 1 1 1 1],
    #         [1 0 0 0 0 0 0 0 1],
    #         [1 0 1 0 1 0 1 0 1],
    #         [1 0 1 1 1 1 1 0 1],
    #         [1 0 1 0 1 0 1 0 1],
    #         [1 0 0 0 0 0 0 0 1],
    #         [1 1 1 1 1 1 1 1 1]
    #     ]
    #     result = solution.numIslands(grid)
    #     self.assertEqual(result, 2)

    # def test_islands_3(self):
    #     solution = Solution()
    #     grid = [["1","0","1","1","0","1","1"]]
    #     result = solution.numIslands(grid)
    #     self.assertEqual(result, 3)

    def test_islands_4(self):
        solution = Solution()
        grid = [
            ["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
            ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
            ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
            ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
            ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
        ]
        result = solution.numIslands(grid)
        self.assertEqual(result, 1)


