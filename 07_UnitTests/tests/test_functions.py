
import pytest
from functions import sum,div1,max1,max2


def test_max1():
    assert max1(1,2) == 2
def test_sum():
    assert sum(1,2) == 3


def test_div():
    assert div1(1,2) == 0.5

def test_divException():
    with pytest.raises(ZeroDivisionError):
        div1(1,0)

def test_max2():
    assert max2([1,2,3]) == 3
def test_max2_empty_list_raises():
    with pytest.raises(ValueError, match="List must not be empty"):
        max2([])