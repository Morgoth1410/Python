x = 15
miarka = 6

gora = "|"
dol = "0"

for i in range(1, x + 1):
    gora += "." * miarka + "|"
    dol += f"{i:>{miarka + 1}}"

wynik = gora + "\n" + dol
print(wynik)
