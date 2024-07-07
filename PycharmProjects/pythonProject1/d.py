x = 2
y = 8.123456789

print("x is: %i\ny is: %i\nz is: %i" % (x, y, 5 + 2))
# [(key)] [flag + - 0] [m] [.p] type
print("%i" % (2))  # Integer
print("%c" % ('r'))  # unicode
print("%c" % (56))  # character
print("%s" % ('nasir'))  # String
print("Nasir: %s" % ("Khani"))  # String
print("Nasir: %s" % ("Khani"))
print("%d" % (55.66))  # Integer
print("%o" % (356))  # Octal mabnaye 8
print("%x" % (356))  # Mabnaye 16
print("%X" % (356))  # Mabnaye 16
print("%e" % (356))  # Namade Elmi
print("%E" % (356))
print("%f" % (1.123456))  # Adade Ashari ta 6 ragham neshan midahad
print("%F" % (1.123456789))
print("%g" % (1.123456))
print("%r" % ("nasir"))

print("%.4f" % (y))
print("%9.4f" % (y))
print("%+9.8f" % (y))
print("%-4.5f" % y,"*",sep="")