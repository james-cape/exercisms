from unique_binary_trees import UniqueBinaryTrees

solver = UniqueBinaryTrees()

def test_it_initializes():
    assert isinstance(solver, UniqueBinaryTrees)
    assert hasattr(solver, 'numTrees')

def test_it_counts_unique_for_2():
    assert solver.numTrees(2) == 2

def test_it_counts_unique_for_3():
    assert solver.numTrees(3) == 5