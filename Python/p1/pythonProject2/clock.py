import time
import winsound

t = int(input("Enter time in seconds: "))

while t > 0:
    mins, secs = divmod(t, 60)
    timer = str(mins) + "m " + str(secs)
    print(timer, end="\r")
    time.sleep(1)
    t = t - 1
print(t)
for i in range(3):
    winsound.Beep(850, (i + 1) * 1000)
print("Done")
