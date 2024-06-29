import time
import winsound

t = int(input('Please enter the time in second(s):'))

def start_beep()

while t > 0:
    mins, secs = divmod(t, 60)
    timer = str(mins) + ':' + str(secs)
    print(timer, end='\r')
    time.sleep(1)
    t = t-1
for i in range(2):
    winsound.Beep(800, (i + 1) * 500)
print('Done')