from src.math_operations import add, sub

def test_add():
    assert add(3,5)==8
    assert add(-2,2)==0

def test_sub():
    assert(5,3)==2
    assert(-2,-2)==0