import pytest
import newton


def test_successful_optimization():
    f = lambda x: (x - 2) ** 2
    result = newton.optimize(f, 0)
    assert abs(result - 2) < 1e-4


def test_unsuccessful_optimization():
    f = lambda x: x**4 / 4 - x**3 - x

    with pytest.raises(RuntimeError):
        newton.optimize(f, 0)


def test_invalid_input():
    with pytest.raises(TypeError):
        newton.optimize("not a function", 0)