from uselessmath import uadd, udiv, umult, usub


def test_uadd():
    assert uadd(1, 2) == 3


def test_usub():
    assert usub(3, 2) == 1


def test_umult():
    assert umult(2, 2) == 4


def test_udiv():
    assert udiv(6, 2) == 3
