x = 4
y = 2


# Tu bardziej jak w c++ czyli w pętlach dodajemy elementy
square_loop = ""
for i in range(y):
    for n in range(x):
        square_loop += "+---"
    square_loop += "+\n"

    for n in range(x):
        square_loop += "|   "
    square_loop += "|\n"

for n in range(x):
    square_loop += "+---"
square_loop += "+"

print(square_loop)

print()

#Tu bardziej jak w python czyli dodawanie i mnożenie stringów
poziom = "+---" * x + "+\n"
pion = "|   " * x + "|\n"

square_math = (poziom + pion) * y + "+---" * x + "+"

print(square_math)
