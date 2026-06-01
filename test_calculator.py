import pytest
from calculator import add, subtract, multiply, divide


class TestAdd:
    def test_positive_numbers(self):
        assert add(10, 5) == 15

    def test_negative_numbers(self):
        assert add(-3, -7) == -10

    def test_mixed_sign(self):
        assert add(-4, 9) == 5

    def test_floats(self):
        assert add(1.5, 2.5) == pytest.approx(4.0)

    def test_zero(self):
        assert add(0, 0) == 0
        assert add(5, 0) == 5


class TestSubtract:
    def test_positive_numbers(self):
        assert subtract(10, 5) == 5

    def test_result_is_negative(self):
        assert subtract(3, 7) == -4

    def test_negative_numbers(self):
        assert subtract(-4, -6) == 2

    def test_floats(self):
        assert subtract(5.5, 2.5) == pytest.approx(3.0)

    def test_zero(self):
        assert subtract(5, 0) == 5
        assert subtract(0, 0) == 0


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(10, 5) == 50

    def test_negative_numbers(self):
        assert multiply(-3, -4) == 12

    def test_mixed_sign(self):
        assert multiply(-3, 4) == -12

    def test_floats(self):
        assert multiply(2.5, 4.0) == pytest.approx(10.0)

    def test_zero(self):
        assert multiply(0, 999) == 0
        assert multiply(0, 0) == 0

    def test_identity(self):
        assert multiply(7, 1) == 7


class TestDivide:
    def test_positive_numbers(self):
        assert divide(10, 5) == 2.0

    def test_negative_numbers(self):
        assert divide(-10, -5) == 2.0

    def test_mixed_sign(self):
        assert divide(-10, 5) == -2.0

    def test_floats(self):
        assert divide(7.5, 2.5) == pytest.approx(3.0)

    def test_non_integer_result(self):
        assert divide(1, 3) == pytest.approx(0.3333, rel=1e-3)

    def test_divide_by_zero(self):
        assert divide(10, 0) == "Error: Cannot divide by zero"

    def test_zero_numerator(self):
        assert divide(0, 5) == 0.0