from time import perf_counter


def list_range(start, stop, step=1):
    new_range = []
    while start < stop:
        new_range.append(start)
        start += step
    return new_range


def gen_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step


start = perf_counter()
lr = list_range(1, 10000000)
s = 0
for i in lr:
    if i == 3:
        break
    s += i ** 2
end = perf_counter()
print("ln: ", end - start)
# ***********************************
start2 = perf_counter()
gr = gen_range(1, 10000000000000000000)
s = 0
for j in gr:
    if j == 3:
        break
    s += j ** 2
end2 = perf_counter()
print("gn: ", end2 - start2)
