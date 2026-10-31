# Iteracyjnie działa tak że ma wskaźniki na lewą i prawą stronę listy
# i zamienia liczbe pod L[left] na L[right] następnie zmniejsza zakres
# czyli left++ i right-- i robi tak dopóki left <= right

def odwracanie_iter(L, left, right):
    while left <= right:
        helper = L[right]
        L[right] = L[left]
        L[left] = helper
        left += 1
        right -= 1

    return L

# Robi to samo tylko zamiast pętli zwraca funkcje ze zmniejszonym
# zakresem.

def odwracanie_rekur(L, left, right):
    if left >= right: return L

    L[left], L[right] = L[right], L[left]

    return odwracanie_rekur(L, left + 1, right - 1)


def test_odwracanie():
    assert odwracanie_iter([1, 2, 3, 4, 5], 1, 3) == [1, 4, 3, 2, 5], "Błąd dla iter(1, 3)"
    assert odwracanie_iter([1, 2, 3, 4, 5], 2, 2) == [1, 2, 3, 4, 5], "Błąd dla iter(2, 2)"
    assert odwracanie_iter([1, 2, 3, 4, 5], 0, 4) == [5, 4, 3, 2, 1], "Błąd dla iter(0, 4)"

    assert odwracanie_rekur([1, 2, 3, 4, 5], 1, 3) == [1, 4, 3, 2, 5], "Błąd dla rekur(1, 3)"
    assert odwracanie_rekur([1, 2, 3, 4, 5], 2, 2) == [1, 2, 3, 4, 5], "Błąd dla rekur(2, 2)"
    assert odwracanie_rekur([1, 2, 3, 4, 5], 0, 4) == [5, 4, 3, 2, 1], "Błąd dla rekur(0, 4)"
    print("Testy ok")

test_odwracanie()

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(odwracanie_iter(L, 2, 6)) # To najpierw odwraca iteracyjnie
#L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #Można zresetować liste
print(odwracanie_rekur(L, 2, 6)) # To potem odwraca do poczatkowej postaci rekurencyjnie


