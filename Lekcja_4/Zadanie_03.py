def factorial(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum

def test_factorial():
    assert factorial(0) == 1, "Błąd dla factorial(0)"
    assert factorial(3) == 6, "Błąd dla factorial(3)"
    assert factorial(6) == 720, "Błąd dla factorial(6)"
    print("Testy ok")

test_factorial()

print(factorial(52))

