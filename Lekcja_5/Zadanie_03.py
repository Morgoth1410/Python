def add_poly(poly1, poly2):         # poly1(x) + poly2(x)                                               # Działa tak że znajduje krótszy wielomian i potem wykonuje
    disambiguate_poly(poly1) ; disambiguate_poly(poly2)                                                 # Tylko tyle operacji ile ma ten krótszy i tworzy liste
    poly_short, poly_long = (poly1, poly2) if len(poly1) < len(poly2) else (poly2, poly1)               # długości tego dłuższego.
    result = list(long_poly)                                                                            # Złożoność czasowa O(min(N,M)) pamięciowa O(max(N,M))
    for i in range(len(poly_short):
        result[i] += poly_short[i]
    return result

def sub_poly(poly1, poly2):         # poly1(x) - poly2(x)
    disambiguate_poly(poly1) ; disambiguate_poly(poly2)                                                 # Algorytmicznie tak samo jak dodawnie
    poly_short, poly_long = (poly1, poly2) if len(poly1) < len(poly2) else (poly2, poly1)
    result = list(long_poly)
    for i in range(len(poly_short):
        result[i] += poly_short[i]
    return result

def mul_poly(poly1, poly2):         # poly1(x) * poly2(x)                                               # Mnoży każdy z każdym i dodaje do odpowieniego elementu wyniku.
    disambiguate_poly(poly1) ; disambiguate_poly(poly2)                                                 # Złożoność czasowa to O(N^2) pamięciowa O(N+M-1)
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1)):                                                                         # Jest algortym o złożoności czasowej O(Nlog(N))
        for j in range(len(poly2)):                                                                     # ale jest szybszy działa dopiero dla dużych wielomianów
            result[i+j] = result[i+j] + poly1[i] * poly2[j]                                             # np pareset współczynników
    return result

def is_zero(poly):                 # bool, [0], [0,0], itp.                                             # Przechodzi przez wszystkie elemetny i sprawdza czy któryś to nie zero
    for i in range(len(poly)):                                                                          # Czasowo O(N) pamięciowo O(1)
        if (poly[i] != 0): return False
    return True

def eq_poly(poly1, poly2):         # bool, porównywanie poly1(x) == poly2(x)                            # Przechodzi przez całą liste i sprawdza czy coś jest inne
    disambiguate_poly(poly1) ; disambiguate_poly(poly2)
    if (len(poly1) != len(poly2)): return False
    for i in range(len(poly1):
        if (poly1[i] != poly2[i]): return False
    return True


def eval_poly(poly, x0):            # poly(x0), algorytm Hornera
    disambiguate_poly(poly)
    result = 0
    for i in range(len(poly) - 1, -1, -1)):
        result = (result * x0) + poly[i]
    return result

def combine_poly(poly1, poly2): pass    # poly1(poly2(x)), trudne!

def pow_poly(poly, n):              # poly(x) ** n                                                      # Potęgowanie binarne. Działa tak że jeśli dostaje liczbe parzystą to
    disambiguate_poly(poly)                                                                             # rekurencyjnie potęguje połowy tych liczb parzystych i mnoży je.
    if (n == 0): return [1]                                                                             # Jeśli dostaje nieparzystą to odejmuje jeden i wykonuje to samo co
    if (n == 1 or poly == [0]): return list(poly)                                                       # dla parzystych.
    if (n % 2 == 0):
        half = pow_poly(poly, n // 2)
        result = mul_poly(half, half)
    else:
        result = mul_poly(poly, pow_poly(poly, n - 1))

    return disambiguate_poly(result)


def diff_poly(poly):                # pochodna wielomianu
    disambiguate_poly(poly)
    if (poly == [0]) return [0];
    poly1 = list(poly)
    for i in range(1, len(poly1)):
        poly1[i-1] = poly1[i]*i
    del poly1[-1]
    return poly1


def disambiguate_poly(poly): # dodatkowa funkcja do usuwania niejednoznaczności
    if not poly:             # przyjmuje poly i usuwa końcowe zera np:
        poly.append(0)       # poly = [2, 0, 1, 0] to zwróci [2, 0, 1]
        return poly          # dla [0,0,0] i [] zwróci [0]

    n_zero = 0
    for i in range(len(poly) - 1, 0, -1):
        if poly[i] != 0:
            n_zero = i
            break;
    del poly[n_zero + 1:]
    return poly


# p1 = [2, 1]                   # W(x) = 2 + x
# p2 = [2, 1, 0]                # jw  (niejednoznaczność)
# p3 = [-3, 0, 1]               # W(x) = -3 + x^2
# p4 = [3]                      # W(x) = 3, wielomian zerowego stopnia
# p5 = [0]                      # zero
# p6 = [0, 0, 0]                # zero (niejednoznaczność)

import unittest

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x^2

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])

    def test_sub_poly(self): pass

    def test_mul_poly(self): pass

    def test_is_zero(self): pass

    def test_eq_poly(self): pass

    def test_eval_poly(self): pass

    def test_combine_poly(self): pass

    def test_pow_poly(self): pass

    def test_diff_poly(self): pass

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
