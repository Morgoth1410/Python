def flatten(sequence):
    result = []
    for item in sequence: # Przechodzi przez przekazany element
        if isinstance(item, (list, tuple)): # Sprawdza czy to lista lub krotka
            result.extend(flatten(item))  # Jak tak to schodzi głębiej i dodaje rozplecione
        else:
            result.append(item) # Jak nie to dodaje liczbe po prostu

    return result

def test_flatten():
    assert flatten([1, 2, 3]) == [1, 2, 3], "Błąd dla płaskiej listy"
    assert flatten([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9], "Błąd dla zagnieżdżonej sekwencji"
    assert flatten([]) == [], "Błąd dla pustej sekwencji"
    print("Testy ok")

test_flatten()

sequence = [1, (2, 3), [4, [5, 6]], 7]
print(flatten(sequence))
