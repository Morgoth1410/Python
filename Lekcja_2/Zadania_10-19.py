# Dane przykładowe
line = """Guido van Rossum, znany jako GvR,
stworzyl jezyk Python.\tGvR pracowal
w wielu firmach i organizacjach."""

word = "Python"
L = [7, 24, 123, 5, 99, 400]
n = 1002003000405060

# ZADANIE 2.10
print("ZADANIE 2.10")
print(len(line.split())) #split tworzy ze string listę podzieloną po białych znakach.
print()

# ZADANIE 2.11
print("ZADANIE 2.11")
print("_".join(word)) #join łączy każdy string określonym znakiem
print()

# ZADANIE 2.12
print("ZADANIE 2.12")
print(''.join(w[0] for w in line.split())) #W pętli przechodzimy przez każdy pierwszy element wszystkich komórek listy i łączymy join
print(''.join(w[-1] for w in line.split())) #To samo tylko ostatni
print()

# ZADANIE 2.13
print("ZADANIE 2.13")
print(sum(len(w) for w in line.split())) #Len zwraca wartość listy w której elementami są wyrazy bez białych znaków
print()

# ZADANIE 2.14
print("ZADANIE 2.14")
print("(a)", max(line.split(), key=len)) #Zwraca największy z listy wszystkich wyrazów z line
print("(b)", len(max(line.split(), key=len))) #Zwraca długość tego wyrazu
print()

# ZADANIE 2.15
print("ZADANIE 2.15")
print(''.join(str(x) for x in L)) #Zamienia liczby na string i potem je łączy
print()

# ZADANIE 2.16
print("ZADANIE 2.16")
print(line.replace("GvR", "Guido van Rossum")) #Podmienia GvR na Guido van Rossum
print()

# ZADANIE 2.17
print("ZADANIE 2.17")
print(sorted(line.split())) #Sortuje alfabetycznie po ASCII
print(sorted(line.split(), key=len)) #Sortuje po długości
print()

# ZADANIE 2.18
print("ZADANIE 2.18")
print(str(n).count('0')) #Zamienia na string i liczy ile jest 0
print()

# ZADANIE 2.19
print("ZADANIE 2.19")
print(''.join(str(x).zfill(3) for x in L)) #Każdy element L po kolei zamieniamy na string i potem zfill wypełnia zerami do długości 3 a następnie join dodaje do wyniku
