def cen_gen(words):
    print("Start!")
    w = None
    while True:
        word = yield w
        if word not in words:
            w = word
        else:
            w = "*" * len(word)


g = cen_gen(["khar", "gav", "meymoon"])
next(g)
print(g.send("Reza"))
print(g.send("khar"))
print(g.send("Khani"))
print(g.send("gav"))
print(g.send("sahel"))
print(g.send("meymoon"))
