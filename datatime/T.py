from khayyam import JalaliDatetime, JalaliDate

print(JalaliDatetime.now())
print(JalaliDate.today())
print(JalaliDate.today().strftime('%A %d %B %Y'))
print(JalaliDate(1403, 4, 26).todate())


