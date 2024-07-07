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

# r = range(10,20,2)
# print(list(r))
lr = list_range(10,100,2)
print(lr)