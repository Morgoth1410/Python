
def make_ruler(x, miarka):

    gora = "|"
    dol = "0"

    for i in range(1, x + 1):
        gora += "." * miarka + "|"
        dol += f"{i:>{miarka + 1}}"

    wynik = gora + "\n" + dol
    return wynik

def make_square(x, y):

    poziom = "+---" * x + "+\n"
    pion = "|   " * x + "|\n"

    square_math = (poziom + pion) * y + "+---" * x + "+"

    return square_math


# Testy
def test_make_ruler():
    assert make_ruler(1, 1) == "|.|\n0 1", "Błąd dla make_ruler(1, 1)"
    assert make_ruler(2, 2) == "|..|..|\n0  1  2", "Błąd dla make_ruler(2, 2)"
    assert make_ruler(3, 1) == "|.|.|.|\n0 1 2 3", "Błąd dla make_ruler(3, 1)"

    print("Testy ok")


def test_make_square():
    oczekiwany_1x1 = "+---+\n" "|   |\n" "+---+"
    assert make_square(1, 1) == oczekiwany_1x1, "Błąd dla make_square(1, 1)"
    oczekiwany_2x1 = "+---+---+\n" "|   |   |\n" "+---+---+"
    assert make_square(2, 1) == oczekiwany_2x1, "Błąd dla make_square(2, 1)"
    oczekiwany_2x2 = (
        "+---+---+\n"
        "|   |   |\n"
        "+---+---+\n"
        "|   |   |\n"
        "+---+---+"
    )
    assert make_square(2, 2) == oczekiwany_2x2, "Błąd dla make_square(2, 2)"

    print("Testy ok")

test_make_ruler()
test_make_square()

print(make_ruler(12, 6))
print()
print(make_square(4, 2))

