# 1. L = [3, 5, 4] ; L = L.sort()
# L.sort() zortuje liste w miejscu i zwraca None więc L będzie miało none

# 2. x, y = 1, 2, 3
# ValueError. Próbujemy rozpakować 3 wartości do 2 zmiennych. Zmienne po lewej
# stronie muszą odpowiadać liczbie wartości po prawej stronie.

# 3. X = 1, 2, 3 ; X[1] = 4
# TypeError. Zmienna X staje się krotką. Krotki w Pythonie są niemutowalne, więc nie można zmienić ich elementów.

# 4. X = [1, 2, 3] ; X[3] = 4
# IndexError. Lista ma 3 elementy. Próba odwołania się do nieistniejącego indeksu wyrzuca błąd.

# 5. X = "abc" ; X.append("d")
# AttributeError. String nie posiada metody append().

# 6. L = list(map(pow, range(8)))
# TypeError. Funkcja wbudowana pow() wymaga podania przynajmniej dwóch argumentów
# Funkcja map() dostarcza jej tylko po jednym argumencie z range(8).
