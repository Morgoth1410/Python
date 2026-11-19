import random
# yield zatrzymuje pętlę więc
# kiedy 
def zero_one():
    while True: 
        yield 0
        yield 1

def random_direction():
    direction = ("N", "E", "S", "W")
    while True:
        yield random.choice(direction)

def days_of_the_week():
    while True:
        yield from range(7)

gen1 = zero_one()
for i in range(10):
    print(next(gen1), end = " ")
print()

gen2 = random_direction()
for i in range(10):
    print(next(gen2), end = " ")
print()

gen3 = days_of_the_week()
for i in range(10):
    print(next(gen3), end = " ")
print()