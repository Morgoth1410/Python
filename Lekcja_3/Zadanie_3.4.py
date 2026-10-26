while True:
    dane = input("Podaj liczbę rzeczywistą (lub wpisz 'stop' aby zakończyć): ")

    if dane == "stop":
        break

    try:
        x = float(dane)
        print(f"Podana liczba: {x}, Trzecia potęga: {x**3}")
    except ValueError:
        print("Błąd: podana wartość nie jest liczbą. Spróbuj ponownie.")
