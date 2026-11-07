# W kodzie występuje wielokrotne wywoływanie disambiguate_poly przy uruchamianiu funkcji. Przy programowaniu obiektowym można usunąć te funkcje 
# bo byłoby to wywoływane przy konstruktorze obiektu. 

def add_poly(poly1, poly2):         # poly1(x) + poly2(x)                                               # Działa tak że znajduje krótszy wielomian i potem wykonuje
    disambiguate_poly(poly1) ; disambiguate_poly(poly2)                                                 # Tylko tyle operacji ile ma ten krótszy i tworzy liste
    poly_short, poly_long = (poly1, poly2) if len(poly1) < len(poly2) else (poly2, poly1)               # długości tego dłuższego.
    result = list(poly_long)                                                                            
    for i in range(len(poly_short)):
        result[i] += poly_short[i]
    return disambiguate_poly(result)

def sub_poly(poly1, poly2):         # poly1(x) - poly2(x)                                               # Najpierw ustawiamy wynik jako poly1 sprawdzamy czy poly1
    disambiguate_poly(poly1) ; disambiguate_poly(poly2)                                                 # jest dłuższe jeśli tak to dodajemy więcej miejsca do result
    result = list(poly1)                                                                                # i potem odejmujemy w pętli.
    if len(poly2) > len(poly1):                                                                         
        result += [0] * (len(poly2) - len(poly1))
    for i in range(len(poly2)):
        result[i] -= poly2[i]
    return disambiguate_poly(result)

def mul_poly(poly1, poly2):         # poly1(x) * poly2(x)                                               # Mnoży każdy z każdym i dodaje do odpowieniego elementu wyniku.
    disambiguate_poly(poly1) ; disambiguate_poly(poly2)                                           
    if ((poly1 == [0]) or (poly2 == [0])): return [0]                                           
    result = [0] * (len(poly1) + len(poly2) - 1)                                                        
    for i in range(len(poly1)):                                                                         
        for j in range(len(poly2)):                                                                     
            result[i+j] = result[i+j] + poly1[i] * poly2[j]                                             
    return result

def is_zero(poly):                 # bool, [0], [0,0], itp.                                             # Przechodzi przez wszystkie elemetny i sprawdza czy któryś to nie zero
    for i in range(len(poly)):                                                                          # Dodatkowo inną metodą implementacji może być: 
        if (poly[i] != 0): return False                                                                 # disambiguate_poly(poly) ; if poly == [0]: return True ; else: return False 
    return True                                                                                         

def eq_poly(poly1, poly2):         # bool, porównywanie poly1(x) == poly2(x)                            # Przechodzi przez całą liste i sprawdza czy coś jest inne
    disambiguate_poly(poly1) ; disambiguate_poly(poly2)                                                 
    if (len(poly1) != len(poly2)): return False
    for i in range(len(poly1)):
        if (poly1[i] != poly2[i]): return False
    return True

def eval_poly(poly, x0):            # poly(x0), algorytm Hornera                                        # Schemat Hornera. Idziemy od tyłu i mnożymy result * x0 zamiast 
    disambiguate_poly(poly)                                                                             # od przodu. Np. (((a3 x + a2) x + a1) * x) + a0 tu w pierwszej iteracji
    result = 0                                                                                          # dostajemy result = a3 i potem liczymy result = a3*x0 + a2 i tak do końca
    for i in range(len(poly) - 1, -1, -1):                                                             
        result = (result * x0) + poly[i]
    return result

def combine_poly(poly1, poly2):    # poly1(poly2(x)), trudne!                                           # Łączenie wielomianów. Podobnie jak schemat hornera. Idziemy od tyłu 
    disambiguate_poly(poly1)                                                                            # i podstawiamy po kolei. 
    disambiguate_poly(poly2)                                                                            
    poly = [0]                                                                                                                                                            
    for i in range(len(poly1) - 1, -1, -1):
        poly = (mul_poly(poly, poly2))
        poly[0] += poly1[i]
    return disambiguate_poly(poly)

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

def diff_poly(poly):                # pochodna wielomianu                                               # Przechodzi przez liste i przesuwa każdy element o jeden do tyłu      
    disambiguate_poly(poly)                                                                             # oraz mnoży go przez potęge x przy nim
    if (len(poly) <= 1): return [0];                                                                   
    poly1 = list(poly)
    for i in range(1, len(poly1)):
        poly1[i-1] = poly1[i]*i
    del poly1[-1]
    return poly1

def disambiguate_poly(poly):                                                                            # dodatkowa funkcja do usuwania niejednoznaczności
    if not poly:                                                                                        # przyjmuje poly i usuwa końcowe zera np:
        poly.append(0)                                                                                  # poly = [2, 0, 1, 0] to zwróci [2, 0, 1]
        return poly                                                                                     # dla [0,0,0] i [] zwróci [0]                                                      
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

    def test_disambiguate_poly(self):
        self.assertEqual(disambiguate_poly([2, 1, 0, 0]), [2, 1])
        self.assertEqual(disambiguate_poly([0, 0, 0]), [0])
        self.assertEqual(disambiguate_poly([]), [0])

    def test_add_poly(self):
        self.assertEqual(add_poly([0, 1], [0, 0, 1]), [0, 1, 1])
        self.assertEqual(add_poly([2, 0, 1], [3, 0, -1]), [5])

    def test_sub_poly(self):
        self.assertEqual(sub_poly([1, 3], [2, 1]), [-1, 2])
        self.assertEqual(sub_poly([1], [1, 2]), [0, -2])
        self.assertEqual(sub_poly([0, 2, 1], [0, 0, 1]), [0, 2])

    def test_mul_poly(self):
        self.assertEqual(mul_poly([2, 1], [1, -2]), [2, -3, -2])
        self.assertEqual(mul_poly([2, 1], [0]), [0])

    def test_is_zero(self):
        self.assertTrue(is_zero([0]))
        self.assertTrue(is_zero([0, 0, 0]))
        self.assertFalse(is_zero([0, 1, 0]))

    def test_eq_poly(self):
        self.assertTrue(eq_poly([2, 1], [2, 1, 0, 0]))
        self.assertFalse(eq_poly([2, 1], [2, 2]))

    def test_eval_poly(self):
        self.assertEqual(eval_poly([2, 3, 1], 2), 12)
        self.assertEqual(eval_poly([5], 10), 5)

    def test_combine_poly(self):
        self.assertEqual(combine_poly([3, 0, 1], [1, 2]), [4, 4, 4])

    def test_pow_poly(self):
        self.assertEqual(pow_poly([2, 1], 0), [1])
        self.assertEqual(pow_poly([1, -1], 2), [1, -2, 1])
        self.assertEqual(pow_poly([1, 1], 3), [1, 3, 3, 1])

    def test_diff_poly(self):
        self.assertEqual(diff_poly([5]), [0])
        self.assertEqual(diff_poly([3, 2]), [2])
        self.assertEqual(diff_poly([1, 0, 3]), [0, 6])


if __name__ == '__main__':
    unittest.main()
