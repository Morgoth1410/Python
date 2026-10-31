def fib(n):
    if n == 0: return 0
    if n == 1: return 1

    a = 0
    b = 1
    for i in range(2, n + 1):
        a, b = b, a + b # Liczone jest od prawej do lewej czyli najpierw a + b potem b
    return b            # i potem dopiero przypisywane są wartości dla a i b

def test_fib():
    assert fib(0) == 0, "Błąd dla fib(0)"
    assert fib(1) == 1, "Błąd dla fib(1)"
    assert fib(5) == 5, "Błąd dla fib(5)"
    assert fib(10) == 55, "Błąd dla fib(10)"
    print("Testy ok")

test_fib()

print(fib(0))
print(fib(12))
