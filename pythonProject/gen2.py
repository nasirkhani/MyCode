def spl_gen(delimiter=" "):
    print("Start!")
    s = None
    while True:
        line = yield s
        s = line.split(delimiter)


g = spl_gen("-")
next(g)
print(g.send("ali-reza-hasan-sahel"))
