from highest_peak import HighestPeak

def test_it_initializes():
    highest_peak = HighestPeak()
    assert highest_peak

def test_case_1():
    highest_peak = HighestPeak()
    grid = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    assert highest_peak.get_elevation(grid) == 0

def test_case_2():
    highest_peak = HighestPeak()
    grid = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    assert highest_peak.get_elevation(grid) == 1

def test_case_3():
    highest_peak = HighestPeak()
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]

    assert highest_peak.get_elevation(grid) == 1

def test_case_4():
    highest_peak = HighestPeak()
    grid = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    assert highest_peak.get_elevation(grid) == 2

def test_case_5():
    highest_peak = HighestPeak()
    grid = [
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    assert highest_peak.get_elevation(grid) == 2

def test_case_6():
    highest_peak = HighestPeak()
    grid = [
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]

    assert highest_peak.get_elevation(grid) == 2

def test_case_7():
    highest_peak = HighestPeak()
    grid = [
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 1, 1]
    ]

    assert highest_peak.get_elevation(grid) == 3

def test_case_8():
    highest_peak = HighestPeak()
    grid = [
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    assert highest_peak.get_elevation(grid) == 1

def test_case_9():
    highest_peak = HighestPeak()
    grid = [
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ]

    assert highest_peak.get_elevation(grid) == 1