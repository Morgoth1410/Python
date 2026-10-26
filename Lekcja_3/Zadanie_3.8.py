list1 = [3, 7, 12]
list2 = [1, 2, 3, 4]

# set nie zawiera potwórzeń. Zamiana na set automatycznie je usuwa
zbior1 = set(list1)
zbior2 = set(list2)

print(zbior1 & zbior2) #Iloczyn mnogościowy zbiorów
print(zbior1 | zbior2) #Suma mnogościowa zbiorów
