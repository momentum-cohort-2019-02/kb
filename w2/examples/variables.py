z = 10


def add(x, y):
    total = x + y  # only available inside add
    return total + z  # works, but bad idea


x = 1
y = 2

add(y, x)
