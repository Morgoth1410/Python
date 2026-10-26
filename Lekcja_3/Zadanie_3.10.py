roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
napis = "MDCCCLXXXVIII"

suma = 0
max_wartosc = 0

# Przechodzimy od końca. Zależność między rzymskimi liczbami jest taka
# że jeśli liczba wcześniej jest mniejsza to odejmujemy tą wartość od
# następnej typu IX = 9. Kiedy przechodzimy od końca to idziemy od najmniejszej
# do największej więc zapisujemy największą obecną liczbe w zmiennej i
# sprawdzamy idąc do tyłu czy któraś jest mniejsza od obecnej i jeśli jest
# to odejmujemy ją.

for znak in reversed(napis):
    wartosc = roman_map[znak]

    if wartosc < max_wartosc:
        suma -= wartosc
    else:
        suma += wartosc
        max_wartosc = wartosc

print(suma)

# Tu od lewej. Sprawdzamy czy następna wartość po obecnej jest większa.
# Jeśli jest to odejmujemy jeśli nie to dodajemy.

suma = 0
n = len(napis)

for i in range(n):
    wartosc = roman_map[napis[i]]

    if i + 1 < n and wartosc < roman_map[napis[i + 1]]:
        suma -= wartosc
    else:
        suma += wartosc

print(suma)
