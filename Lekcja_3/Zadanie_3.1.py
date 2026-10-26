# 1.
# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;
#
# Kod się uruchomi ale średniki są zbędne i nawias po if też

# 2.
# for i in "axby": if ord(i) < 100: print (i)
#
# Nie zadziała bo w python nie można umieszczać if zaraz po dwukropku w tej samej linii co pętla. Potrzebna jest nowa linia i wcięcie

# 3.
# for i in "axby": print (ord(i) if ord(i) < 100 else i)
#
# Zadziała. Można wykonać prostą instrukcje print po dwukropku pętli
