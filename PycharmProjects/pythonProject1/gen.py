def func():
    for i in range(1000):
        yield i ** 2


g = func()
while True:
    value = next(g)
    if value == 100:
        break
    print(value)
