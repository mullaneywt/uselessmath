from uselessmath.uclass import Umath


def test_umath_add():
    m = Umath()
    assert m.add(1, 2) == 3


def test_umath_sub():
    m = Umath()
    assert m.sub(3, 2) == 1


def test_umath_mult():
    m = Umath()
    assert m.mult(2, 2) == 4


def test_umath_div():
    m = Umath()
    assert m.div(6, 2) == 3


def test_umath_square():
    m = Umath()
    assert m.square(2) == 4


def test_umath_cube():
    m = Umath()
    assert m.cube(2) == 8
