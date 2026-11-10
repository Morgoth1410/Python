# Większość metod w klasie jest przepisana z poprzedniego
# zestawu lub lekko pozmieniana. 

class Poly:
    """Klasa reprezentująca wielomiany."""

    # Przepisany disambiguate.
    # operujemy na elemencie obiektu
    # Tak jak wcześniej idzie od tyłu
    # i usuwa element jeśli to 0
    # ale zamiast pojedynczego usunięcia
    # del w każdej iteracji wywołuje
    # funkcje pop()
    def _disambiguate(self):
        if not self.a:
            self.a = [0]
        while len(self.a) > 1 and self.a[-1] == 0:
            self.a.pop()
        self.size = len(self.a)

    # wg Sedgewicka - tworzymy wielomian c*x^n
    # Konstruktor
    # Dopisałem że jeśli przekazywany argument to
    # lista to od razu tworzymy całą liste
    # zamiast jednego elementu wielomianu
    # dzięki temu można definiować wielomian
    # np. Poly([1, 2])
    def __init__(self, c=0, n=0):
        if isinstance(c, (list, tuple)):
            self.a = list(c)
            self.size = len(self.a)
        else:
            self.size = n + 1
            self.a = self.size * [0]
            self.a[self.size - 1] = c
        self._disambiguate()

    def __str__(self):
        return str(self.a)

    # poly1 + poly2
    # Sprawdza który dłuższy i potem dodaje do niego ten krótszy
    def __add__(self, other):
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

    # poly1 - poly2
    # Tworzy liste result sprawdza czy poly2
    # dłuższe i jak tak do ją poszerza
    # i potem odejmuje
    def __sub__(self, other):
        poly1 = self.a
        poly2 = other.a
        result = list(poly1)
        if len(poly2) > len(poly1):
            result += [0] * (len(poly2) - len(poly1))
        for i in range(len(poly2)):
            result[i] -= poly2[i]
        return Poly(result)

    # poly1 * poly2
    # Robi liste długości N+M-1 i potem mnoży każdy z każdym
    def __mul__(self, other):
        poly1 = self.a
        poly2 = other.a
        if poly1 == [0] or poly2 == [0]:
            return Poly()
        result = [0] * (len(poly1) + len(poly2) - 1)
        for i in range(len(poly1)):
            for j in range(len(poly2)):
                result[i + j] = result[i + j] + poly1[i] * poly2[j]
        return Poly(result)

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


if __name__ == '__main__':
    unittest.main()