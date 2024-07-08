from functools import wraps


def coroutine(func):
    @wraps(func)
    def start(*args, **kwargs):
        gn = func()
        print(next(gn))
        return gn

    return start


@coroutine
def my_gen():
    print("Start!!")
    for i in range(10):
        name = yield i
        print("My name is", name)


g = my_gen()
print(g.send("Nasir"))
print(g.send("Khani"))
