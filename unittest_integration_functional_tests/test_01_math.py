import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        result = addition(3, 2)
        assert result == 5

    def test_threeargs(self):
        result = addition(3, 2, 1)
        assert result == 6

    def test_noargs(self):
        result = addition()
        assert result == 0

# def addition(x, y):
#     return x + y

def addition (*args):
    total = 0
    for a in args:
        total += a
    return total
