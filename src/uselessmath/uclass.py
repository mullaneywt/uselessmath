from uselessmath import ucube, usquare


class umath:
    def add(self, x: int, y: int) -> int:
        return x + y

    def sub(self, x: int, y: int) -> int:
        return x - y

    def mult(self, x: int, y: int) -> int:
        return x * y

    def div(self, x: int, y: int) -> int:
        return x / y

    def square(self, x: int) -> int:
        return usquare(x)

    def cube(self, x: int) -> int:
        return ucube(x)
