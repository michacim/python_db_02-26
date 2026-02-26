import pytest
from functions import sum, max1, max2, div1

class TestMax1:
    def test_max1_a_greater(self):
        assert max1(5,3) == 5
        assert max1(7,2) == 7
    def test_max1_b_greater(self):
    #     assert max1(3,5) == 5
    # def test_max1_equals(self):
    #     assert max1(5,5) == 5
    # def test_max1_negative(self):
        assert max1(-1,-5) == -1


class TestDiv1:
    def test_div1_basic(self):
        assert div1(10,2) == 5

    def test_div1_float_result(self):
        assert div1(1,2) == pytest.approx(0.5)

    def test_div_by_zero_raises(self):
        with pytest.raises(ZeroDivisionError):
            div1(10,0)
