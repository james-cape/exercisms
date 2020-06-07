from evaluate_reverse_polish_notation import Solution

def test_it_initializes():
    solution = Solution()
    assert solution

def test_case_1():
    solution = Solution()
    tokens = ["2", "1", "+", "3", "*"]
    answer = 9
    # Explanation: ((2 + 1) * 3) = 9

    assert solution.get_answer(tokens) == answer

def test_case_2():
    solution = Solution()
    tokens = ["4", "13", "5", "/", "+"]
    answer = 6
    # Explanation: (4 + (13 / 5)) = 6

    assert solution.get_answer(tokens) == answer

def test_case_3():
    solution = Solution()
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    answer = 22
    # Explanation: 
    #   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    # = ((10 * (6 / (12 * -11))) + 17) + 5
    # = ((10 * (6 / -132)) + 17) + 5
    # = ((10 * 0) + 17) + 5
    # = (0 + 17) + 5
    # = 17 + 5
    # = 22

    assert solution.get_answer(tokens) == answer