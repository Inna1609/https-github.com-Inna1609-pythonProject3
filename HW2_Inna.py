import random
#1
minute = random.randint(0,59)
print(minute)

if minute <= 15:
    print("First quater")
elif minute >15 and minute <= 30:
    print("Second quater")
elif minute >30 and minute <= 45:
    print("Third quater")
elif minute > 45 and minute <= 60:
    print("Fourth quater")

#2
birth_month =int(input("print some number"))

if birth_month >= 1 and birth_month <=2 or birth_month ==12:
    print("It is snowing outside")
elif birth_month >=3 and birth_month <=5:
    print("Everything around is blooming")
elif birth_month >=6 and birth_month <=8:
    print("Kids enjoying summer vacations")
elif birth_month >=9 and birth_month <=11:
    print("Everything around lit up with bright colours")
else:
    print("Write correct number,please")

#3
x = float(input("Please enter x= "))
y = float(input("Please enter y= "))

if x > 0 and y > 0:
  print("Point is in 1 quater")
elif x < 0 and y > 0:
  print("Point is in 2 quater")
elif x < 0 and y < 0:
  print("Point is in 3 quater")
elif x > 0 and y < 0:
  print("Point is in 4 quater")
elif x == 0 and y == 0:
  print("Point is at the start of coordinates")
elif x == 0:
  print("Point is at the axis Y")
elif y == 0:
  print("Point is at the axis X")
