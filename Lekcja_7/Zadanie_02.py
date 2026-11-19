# Większość metod w klasie jest przepisana z poprzedniego
# zestawu lub lekko pozmieniana.

class Poly:
    """Klasa reprezentująca wielomiany."""

    # Idzie od tyłu i usuwa niepotrzebne 0
    # nie w konstruktorze bo używana w 
    # __setitem__
    def _disambiguate(self):
        if not self.a:
            self.a = [0]
        while len(self.a) > 1 and self.a[-1] == 0:
            self.a.pop()
        self.size = len(self.a)

    # wg Sedgewicka - tworzymy wielomian c*x^n
    # Konstruktor
    # Dodatkowo obsługuje wywołanie
    # np Poly([1,2,3]) i Poly((1,2,3))
    # 1x^0 + 2x^1 + 3x^2
    def __init__(self, c=0, n=0):
        if n < 0:
            raise ValueError("Poly nie obsługuje ujemnych potęg")
        if isinstance(c, (list, tuple)):
            self.a = list(c)
            self.size = len(self.a)
        else:
            self.size = n + 1
            self.a = self.size * [0]
            self.a[self.size - 1] = c
        self._disambiguate()

    # poly1 + poly2
    # Sprawdza który dłuższy i potem dodaje do niego ten krótszy
    def __add__(self, other):
        if not isinstance(other, (int, float, Poly)):
            return NotImplemented
        if isinstance(other, (int, float)):
            other = Poly(other)
        poly1 = self.a
        poly2 = other.a
        if len(poly1) < len(poly2):
            poly_short, poly_long = poly1, poly2
        else:
            poly_short, poly_long = poly2, poly1

        result = list(poly_long)
        for i in range(len(poly_short)):
            result[i] += poly_short[i]
        return Poly(result)

    __radd__ = __add__              # liczba+poly

    # poly1 - poly2
    # Tworzy liste result sprawdza czy poly2
    # dłuższe i jak tak do ją poszerza
    # i potem odejmuje
    def __sub__(self, other):
        if not isinstance(other, (int, float, Poly)):
            return NotImplemented
        if isinstance(other, (int, float)):
            other = Poly(other)
        poly1 = self.a
        poly2 = other.a
        result = list(poly1)
        if len(poly2) > len(poly1):
            result += [0] * (len(poly2) - len(poly1))
        for i in range(len(poly2)):
            result[i] -= poly2[i]
        return Poly(result)

    # liczba-poly
    # Tworzy obiekt Poly z liczby i używa
    # odejmowania wielomianów
    def __rsub__(self, other): 
        if not isinstance(other, (int, float, Poly)):
            return NotImplemented
        result = Poly(other, 0) - self
        return result

    # poly1 * poly2
    # Robi liste długości N+M-1 i potem mnoży każdy z każdym
    def __mul__(self, other):
        if not isinstance(other, (int, float, Poly)):
            return NotImplemented
        if isinstance(other, (int, float)):
            other = Poly(other)
        poly1 = self.a
        poly2 = other.a
        if poly1 == [0] or poly2 == [0]:
            return Poly()
        result = [0] * (len(poly1) + len(poly2) - 1)
        for i in range(len(poly1)):
            for j in range(len(poly2)):
                result[i + j] = result[i + j] + poly1[i] * poly2[j]
        return Poly(result)

    __rmul__ = __mul__              # liczba*poly

    # +poly1 = (+1)*poly1
    # przekazuje listę jako argument. Konstruktor sam robi kopie
    def __pos__(self):
        return Poly(self.a)

    # -poly1 = (-1)*poly1
    # Neguje każdy element
    def __neg__(self):
        result = list(self.a)
        for i in range(len(result)):
            result[i] = -result[i]
        return Poly(result)

    # Przez to że dane są w postaci kanonicznej to trzeba tylko
    # sprawdzić czy listy są takie same
    # obsługa poly1 == poly2
    def __eq__(self, other):
        return isinstance(other, Poly) and self.a == other.a

    # obsługa poly1 != poly2
    def __ne__(self, other):
        return not self == other

    # Schemat Hornera. Idziemy od najwyższej potęgi i mnożymy
    # dotychczasowy wynik przez x, dodając kolejny współczynnik.
    def eval(self, x):
        poly = self.a
        result = 0
        for i in range(len(poly) - 1, -1, -1):
            result = (result * x) + poly[i]
        return result

    # Złożenie wielomianów wg schematu Hornera. Idziemy od tyłu,
    # mnożymy obiektowo przez other i dodajemy Poly(a[i]).
    def combine(self, other):
        result = Poly()
        for i in range(len(self.a) - 1, -1, -1):
            result = (result * other) + Poly(self.a[i])
        return result

    # poly(x)**n lub pow(poly(x),n)
    # Potęgowanie binarne czyli mnożenie połów
    def __pow__(self, n):
        if n < 0:
            raise ValueError("Poly nie obsługuje ujemnych potęg")
        if n == 0:
            return Poly(1)
        if n == 1 or self.a == [0]:
            return Poly(self.a)
        if n % 2 == 0:
            half = pow(self, n // 2)
            result = half * half
        else:
            result = self * pow(self, n - 1)
        return result

    # różniczkowanie
    # Przesuwamy elementy o jeden do tyłu i mnożymy
    def diff(self):
        if len(self.a) <= 1:
            return Poly()
        poly1 = list(self.a)
        for i in range(1, len(poly1)):
            poly1[i - 1] = poly1[i] * i
        del poly1[-1]
        return Poly(poly1)

    # całkowanie
    # Przesuwamy elementy o jeden do przodu i dzielimy
    def integrate(self):
        result = [0] * (len(self.a) + 1)
        for i in range(len(self.a)):
            result[i + 1] = self.a[i] / (i + 1)
        return Poly(result)

    # bool, True dla [0], [0, 0],...
    # Dane są w postaci kanonicznej więc
    # tylko sprawdzamy czy lista jest zerowa
    def is_zero(self):
        return self.a == [0]

    def __len__(self):        # len(poly), rozmiar self.a
        return len(self.a)

    def __getitem__(self, i):           # poly[i], współczynnik przy x^i
        return self.a[i]

    def __setitem__(self, i, value):     # poly[i] = value
        self.a[i] = value
        self._disambiguate()    # Gdyby ostatni element wielomianu
                                # był ustawiony na 0

    # dla isinstance(x, (int,float)) odpowiada eval(),
    # dla isinstance(x, Poly) odpowiada combine()
    def __call__(self, x):     # poly(x)
        if isinstance(x, (int,float)):
            return self.eval(x)
        if isinstance(x, Poly):
            return self.combine(x)
        else:
            raise TypeError("Argument musi być liczbą lub wielomianem.")

    def __iter__(self):
        return iter(self.a)

    def __bool__(self): # Ponieważ wielomiany są w postaciach kanonicznych 
        return not self.is_zero() # to nie są nigdy []

    def __contains__(self, x):
        return x in self.a # Wykonuje wbudowaną funkcje contains dla list

    
# Kod testujący moduł.

import unittest


class TestPoly(unittest.TestCase):

    def test_init_and_disambiguate(self):
        p1 = Poly(4, 2)  # 4x^2 -> [0, 0, 4]
        self.assertEqual(p1.a, [0, 0, 4])
        self.assertEqual(p1.size, 3)

        p2 = Poly([1, 2, 0, 0])  # 1 + 2x -> [1, 2]
        self.assertEqual(p2.a, [1, 2])
        self.assertEqual(p2.size, 2)

        p3 = Poly()  # [0]
        self.assertEqual(p3.a, [0])
        self.assertEqual(p3.size, 1)

    def test_add(self):
        p1 = Poly([1, 2])  # 1 + 2x
        p2 = Poly([3, 4, 5])  # 3 + 4x + 5x^2
        self.assertEqual((p1 + p2).a, [4, 6, 5])

        p3 = Poly([2, -3])
        p4 = Poly([-2, 3])
        self.assertEqual((p3 + p4).a, [0])  # Redukcja do [0]

    def test_sub(self):
        p1 = Poly([5, 3, 2])
        p2 = Poly([1, 3])
        self.assertEqual((p1 - p2).a, [4, 0, 2])

        p3 = Poly([1])
        p4 = Poly([1, 1])
        self.assertEqual((p3 - p4).a, [0, -1])
        self.assertEqual((p3 - p3).a, [0])

    def test_mul(self):
        p1 = Poly([1, 1])  # 1 + x
        p2 = Poly([1, -1])  # 1 - x
        self.assertEqual((p1 * p2).a, [1, 0, -1])  # 1 - x^2

        p3 = Poly([3, 4])
        p_zero = Poly()
        self.assertEqual((p3 * p_zero).a, [0])

    def test_pos_and_neg(self):
        p1 = Poly([2, -3, 4])
        self.assertEqual((+p1).a, [2, -3, 4])
        self.assertEqual((-p1).a, [-2, 3, -4])
        self.assertIsNot(+p1, p1)  # Sprawdzenie czy to nowa instancja
        self.assertIsNot(-p1, p1)

    def test_eq_and_ne(self):
        p1 = Poly([1, 2, 0])
        p2 = Poly([1, 2])
        p3 = Poly([1, 3])
        self.assertTrue(p1 == p2)
        self.assertTrue(p1 != p3)
        self.assertFalse(p1 == [1, 2])  # Różne typy

    def test_eval(self):
        p1 = Poly([2, 3, 1])  # 2 + 3x + x^2
        self.assertEqual(p1.eval(2), 12)  # 2 + 6 + 4 = 12
        self.assertEqual(p1.eval(0), 2)

    def test_combine(self):
        p1 = Poly([1, 2])  # 1 + 2x
        p2 = Poly([0, 1])  # x
        self.assertEqual(p1.combine(p2).a, [1, 2])  # 1 + 2(x)

        p3 = Poly([0, 0, 1])  # x^2
        p4 = Poly([1, 1])  # 1 + x
        # (1 + x)^2 = 1 + 2x + x^2
        self.assertEqual(p3.combine(p4).a, [1, 2, 1])

    def test_pow(self):
        p1 = Poly([1, 1])  # 1 + x
        self.assertEqual((p1 ** 0).a, [1])
        self.assertEqual((p1 ** 1).a, [1, 1])
        self.assertEqual((p1 ** 2).a, [1, 2, 1])
        self.assertEqual((p1 ** 3).a, [1, 3, 3, 1])

    def test_diff(self):
        p1 = Poly([5, 3, 2])  # 5 + 3x + 2x^2
        self.assertEqual(p1.diff().a, [3, 4])  # 3 + 4x

        p2 = Poly([7])
        self.assertEqual(p2.diff().a, [0])

    def test_integrate(self):
        p1 = Poly([3, 4])  # 3 + 4x
        self.assertEqual(p1.integrate().a, [0, 3, 2])  # 3x + 2x^2

        p_zero = Poly()  # [0]
        self.assertEqual(p_zero.integrate().a, [0])

    def test_is_zero(self):
        p1 = Poly()
        p2 = Poly([0, 0, 0])
        p3 = Poly([1, 0])
        self.assertTrue(p1.is_zero())
        self.assertTrue(p2.is_zero())
        self.assertFalse(p3.is_zero())

    def test_scalar_operations(self):
        p = Poly([2, 4])  # 2 + 4x

        # Dodawanie liczb (int i float) z obu stron
        self.assertEqual((p + 3).a, [5, 4])
        self.assertEqual((3 + p).a, [5, 4])
        self.assertEqual((p + 1.5).a, [3.5, 4])
        self.assertEqual((1.5 + p).a, [3.5, 4])
        self.assertEqual((Poly([5]) + (-5)).a, [0])

        # Odejmowanie liczb (int i float) z obu stron
        self.assertEqual((p - 2).a, [0, 4])
        self.assertEqual((10 - p).a, [8, -4])
        self.assertEqual((p - 0.5).a, [1.5, 4])
        self.assertEqual((0.5 - p).a, [-1.5, -4])

        # Mnożenie przez liczby (int i float) z obu stron
        self.assertEqual((p * 3).a, [6, 12])
        self.assertEqual((3 * p).a, [6, 12])
        self.assertEqual((p * 0.5).a, [1.0, 2.0])
        self.assertEqual((0 * p).a, [0])
        self.assertEqual((p * 0).a, [0])

    def test_container_methods(self):
        p = Poly([10, 20, 30])

        # __len__ i __getitem__
        self.assertEqual(len(p), 3)
        self.assertEqual(p[0], 10)
        self.assertEqual(p[2], 30)
        self.assertEqual(p[-1], 30)

        # __setitem__ oraz automatyczne skracanie zer (disambiguate)
        p[1] = 25
        self.assertEqual(p.a, [10, 25, 30])
        p[2] = 0
        self.assertEqual(p.a, [10, 25])
        self.assertEqual(len(p), 2)
        self.assertEqual(p.size, 2)

        # __bool__
        self.assertTrue(bool(p))
        self.assertFalse(bool(Poly()))
        self.assertFalse(bool(Poly([0, 0])))

        # __contains__ (in / not in)
        p_with_zero = Poly([5, 0, 8])
        self.assertTrue(5 in p_with_zero)
        self.assertTrue(0 in p_with_zero)
        self.assertTrue(8 in p_with_zero)
        self.assertFalse(99 in p_with_zero)
        self.assertTrue(99 not in p_with_zero)

    def test_iteration(self):
        p = Poly([3, 6, 9])
        self.assertEqual(list(p), [3, 6, 9])

        coeffs = []
        for coeff in p:
            coeffs.append(coeff)
        self.assertEqual(coeffs, [3, 6, 9])

    def test_call(self):
        g = Poly([1, 0, 1])  # x^2 + 1
        f = Poly([3, 1])     # x + 3

        # Wywołanie dla liczby -> eval()
        self.assertEqual(g(2), 5)
        self.assertEqual(g(0.5), 1.25)

        # Wywołanie dla wielomianu -> combine()
        composed = g(f)
        self.assertIsInstance(composed, Poly)
        self.assertEqual(composed.a, [10, 6, 1])  # (x + 3)^2 + 1

    def test_exceptions(self):
        p = Poly([1, 2])

        # ValueError dla ujemnych wykładników
        with self.assertRaises(ValueError):
            Poly(1, -1)
        with self.assertRaises(ValueError):
            _ = p ** -2

        # TypeError dla nieobsługiwanych typów
        with self.assertRaises(TypeError):
            _ = p + "abc"
        with self.assertRaises(TypeError):
            _ = "abc" - p
        with self.assertRaises(TypeError):
            _ = p * "abc"
        with self.assertRaises(TypeError):
            p("abc")


if __name__ == '__main__':
    unittest.main()
