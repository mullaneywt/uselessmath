from uselessmath.uclass import umath


def test_umath_add():
    m = umath()
    assert m.add(1, 2) == 3


def test_umath_sub():
    m = umath()
    assert m.sub(3, 2) == 1


def test_umath_mult():
    m = umath()
    assert m.mult(2, 2) == 4


def test_umath_div():
    m = umath()
    assert m.div(6, 2) == 3


def test_umath_square():
    m = umath()
    assert m.square(2) == 4


def test_umath_cube():
    m = umath()
    assert m.cube(2) == 8
