from pacific_atlantic_water_flow import Solution

def test_it_initializes():
    solution = Solution()
    assert solution

def test_case_1():
    solution = Solution()
    grid = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]

    answer = [
        [0,4],
        [1,3],
        [1,4], #
        [2,2],
        [3,0], #
        [3,1],
        [4,0]
    ]
    for coordinate in solution.get_divide(grid):
        assert coordinate in answer
    assert len(answer) == len(solution.get_divide(grid))

def test_case_2():
    solution = Solution()
    grid = []
    answer = []
    assert solution.get_divide(grid) == []

def test_case_3():
    solution = Solution()
    grid = [
        [1,2,3],
        [8,9,4],
        [7,6,5]
    ]
    answer = [
        [0,2],
        [1,0],
        [1,1],
        [1,2],
        [2,0],
        [2,1], #
        [2,2]
    ]
    for coordinate in solution.get_divide(grid):
        assert coordinate in answer
    assert len(answer) == len(solution.get_divide(grid))

def test_case_4():
    solution = Solution()
    grid = [
        [1,1],
        [1,1],
        [1,1]
    ]
    answer = [
        [0,0],
        [1,0],
        [2,0],
        [0,1],
        [1,1],
        [2,1]
    ]
    for coordinate in solution.get_divide(grid):
        assert coordinate in answer
    assert len(answer) == len(solution.get_divide(grid))

def test_case_5():
    solution = Solution()
    grid = [
        [1]
    ]
    answer = [
        [0, 0]
    ]
    for coordinate in solution.get_divide(grid):
        assert coordinate in answer
    assert len(answer) == len(solution.get_divide(grid))

def test_case_6():
    solution = Solution()
    grid = [
        [ 1, 2, 3, 4],
        [12,13,14, 5],
        [11,16,15, 6],
        [10, 9, 8, 7]
    ]

    answer = [
        [0,3],
        [1,0],
        [1,1],
        [1,2],
        [1,3],
        [2,0],
        [2,1],
        [2,2],
        [2,3],
        [3,0],
        [3,1],
        [3,2],
        [3,3]
    ]
    for coordinate in solution.get_divide(grid):
        assert coordinate in answer
    assert len(answer) == len(solution.get_divide(grid))