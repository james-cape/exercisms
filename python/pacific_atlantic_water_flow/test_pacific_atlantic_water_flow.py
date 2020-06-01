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
    # grid = [
    #     [ 1,*2, 2,*3, 5],
    #     [ 3, 2, 3, 4, 4],
    #     [ 2, 4, 5, 3, 1],
    #     [ 6, 7, 1,*4,*5],
    #     [ 5, 1,*1,*2,*4]
    # ]
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
    # grid = [
    #     [1,2,7,7,2],
    #     [8,9,6,6,2],
    #     [7,6,5,2,2]
    # ]
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