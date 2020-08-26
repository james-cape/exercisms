# https://leetcode.com/problems/generate-parentheses/

from parantheses import Parantheses

def test_it_initializes():
    parantheses = Parantheses()

    assert isinstance(parantheses, Parantheses)

def test_generateParanthesis():
    parantheses = Parantheses()

    result = parantheses.generateParanthesis(3)

    assert len(result) == 5
    assert "((()))" in result
    assert "(()())" in result
    assert "(())()" in result
    assert "()(())" in result
    assert "()()()" in result