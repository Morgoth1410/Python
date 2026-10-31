def sum_seq(sequence):
    total = 0
    for item in sequence: # Przechodzi po elementach
        if isinstance(item, (list, tuple)): # Sprawdza czy lista czy krotka
            total += sum_seq(item) # jak tak to wywołuje funkcje dla wewnętrznej listy lub krotki
        else:
            total += item # Jak cyfra to sumuje

    return total

def test_sum_seq():
    assert sum_seq([1, 2, 3]) == 6, "Błąd dla [1, 2, 3]"
    assert sum_seq([1, (2, 3), [4, [5, 6]], 7]) == 28, "Błąd dla [1, (2, 3), [4, [5, 6]], 7]"
    assert sum_seq([]) == 0, "Błąd dla []"
    print("Testy ok")

test_sum_seq()

sequence = [1, (2, 3), [4, [5, 6]], 7]
print(sum_seq(sequence))
