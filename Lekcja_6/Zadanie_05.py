class Frac:
    """Klasa reprezentująca ułamek."""

    # Algorytm Euklidesa do znalezienia NWD
    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    # Szukamy największego wspólnego dzielnika korzystając z
    # algorytmu euklidesa i potem dzielimy obie liczby
    # przez niego
    def _simplify(self):
        if self.y == 0:
            raise ZeroDivisionError("Mianownik nie może być zerem.")

        if self.x == 0:
            self.y = 1
            return

        if self.y < 0:
            self.x = -self.x
            self.y = -self.y

        nwd = self._gcd(self.x, self.y)
        self.x //= nwd
        self.y //= nwd

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y
        self._simplify()

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.x)
        return f"{self.x}/{self.y}"

    def __repr__(self):  # zwraca "Frac(x, y)"
        return f"Frac({self.x}, {self.y})"

    def __eq__(self, other):
        return (
            isinstance(other, Frac)
            and self.x == other.x
            and self.y == other.y
        )

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.x * other.y < self.y * other.x

    def __le__(self, other):
        return self.x * other.y <= self.y * other.x

    def __gt__(self, other):
        return self.x * other.y > self.y * other.x

    def __ge__(self, other):
        return self.x * other.y >= self.y * other.x

    # frac1 + frac2
    # Mnożenie na krzyż: (a*d + c*b) / (b*d)
    # Można też szukać NWW ale jest to
    # szybsze dopiero dla dużych liczb
    def __add__(self, other):
        new_x = self.x * other.y + other.x * self.y
        new_y = self.y * other.y
        return Frac(new_x, new_y)

    # frac1 - frac2
    # Mnożenie na krzyż: (a*d - c*b) / (b*d)
    def __sub__(self, other):
        new_x = self.x * other.y - other.x * self.y
        new_y = self.y * other.y
        return Frac(new_x, new_y)

    def __mul__(self, other):  # frac1 * frac2
        new_x = self.x * other.x
        new_y = self.y * other.y
        return Frac(new_x, new_y)

    def __truediv__(self, other):  # frac1 / frac2
        new_x = self.x * other.y
        new_y = self.y * other.x
        return Frac(new_x, new_y)

    def __floordiv__(self, other):  # frac1 // frac2
        return (self.x * other.y) // (self.y * other.x)

    def __mod__(self, other):  # frac1 % frac2
        q = self // other
        return self - Frac(q) * other

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):  # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))  # immutable fracs


# Kod testujący moduł.

import unittest


class TestFrac(unittest.TestCase):

    def test_init_and_simplify(self):
        f1 = Frac(2, 4)
        self.assertEqual((f1.x, f1.y), (1, 2))

        f2 = Frac(1, -2)
        self.assertEqual((f2.x, f2.y), (-1, 2))

        f3 = Frac(-3, -6)
        self.assertEqual((f3.x, f3.y), (1, 2))

        f4 = Frac(0, 5)
        self.assertEqual((f4.x, f4.y), (0, 1))

        with self.assertRaises(ZeroDivisionError):
            Frac(1, 0)

    def test_str_and_repr(self):
        self.assertEqual(str(Frac(3, 4)), "3/4")
        self.assertEqual(str(Frac(5, 1)), "5")
        self.assertEqual(repr(Frac(3, 4)), "Frac(3, 4)")

    def test_cmp(self):
        f1 = Frac(1, 2)
        f2 = Frac(2, 4)
        f3 = Frac(3, 4)

        self.assertTrue(f1 == f2)
        self.assertFalse(f1 == f3)
        self.assertTrue(f1 != f3)
        self.assertTrue(f1 < f3)
        self.assertTrue(f1 <= f2)
        self.assertTrue(f3 > f1)
        self.assertTrue(f2 >= f1)
        self.assertFalse(f1 == "1/2")

    def test_add_and_sub(self):
        f1 = Frac(1, 3)
        f2 = Frac(1, 6)
        self.assertEqual(f1 + f2, Frac(1, 2))
        self.assertEqual(f1 - f2, Frac(1, 6))

    def test_mul_and_div(self):
        f1 = Frac(2, 3)
        f2 = Frac(3, 4)
        self.assertEqual(f1 * f2, Frac(1, 2))
        self.assertEqual(f1 / f2, Frac(8, 9))

        with self.assertRaises(ZeroDivisionError):
            _ = f1 / Frac(0, 1)

    def test_floordiv_and_mod(self):
        f1 = Frac(7, 2)
        f2 = Frac(4, 3)
        self.assertEqual(f1 // f2, 2)
        self.assertEqual(f1 % f2, Frac(5, 6))

    def test_unary(self):
        f1 = Frac(2, 3)
        self.assertEqual(+f1, Frac(2, 3))
        self.assertEqual(-f1, Frac(-2, 3))
        self.assertEqual(~f1, Frac(3, 2))

    def test_float_and_hash(self):
        f1 = Frac(1, 2)
        self.assertEqual(float(f1), 0.5)
        self.assertEqual(hash(f1), hash(0.5))
        self.assertIn(f1, {Frac(1, 2)})


if __name__ == "__main__":
    unittest.main()
