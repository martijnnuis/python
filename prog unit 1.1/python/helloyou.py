print("Hello you? Ik ben henk")
print("wie ben jij")
username = input()
print("hello" " " + username) 
print("nu is het")

import datetime


x = datetime.datetime.now()

print(x)

print("Wat is jou geboorte datum?")

from datetime import date, datetime

year = int(input('jaar geboorte: '))
month = int(input('maand van geboorte als cijfer: '))
day = int(input('de dag van geboorte: '))

d = datetime(year, month, day)

print("dus dit is de datum dat jij geboren bent?")
print(d)

uitkomst = (x-d)
print(uitkomst.days/365.25)