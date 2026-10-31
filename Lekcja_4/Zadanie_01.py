X = "qwerty"

def func():
    print(X)

func()

X = "qwerty"

def func():
    X = "abc"

func()
print(X)

X = "qwerty"

def func():
    global X
    X = "abc"

func()
print(X)
