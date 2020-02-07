x = 34
if x == 34:
  print("Ok")
  print("34")
print("Good")
print()

x=4
if x == 34:
  print("Ok")
  print("34")
print("Good")
print()

today_is_friday = True
if today_is_friday:
  print("Noooooo")
else:
  print("yay")
print("Good")
print()

today_is_friday = True
if not today_is_friday:
  print("Noooooo")
else:
  print("yay")
print("Good")
print()

BMI = 26
if BMI > 25:
  print("Overweight")
elif BMI>18:
  print("Normal")
else:
  print("Underweight")
print("Good Morning")
print()

a=36
print(a)
print(type(a))
c = 3 + 1j
print(type(c))
a+c
print()

x = input("Enter year ")
x = int(x)
if (((x % 4 == 0) and (x % 100 != 0)) or
             (x % 400 == 0)):
  print("Leap year")
else:
  print("Not leap year")
print()

i = 0
while i<10:
  print(i)
  i+=1
print()

i = 0
while i<10:
  print(i,end=" ")
  i+=1
print()

# for loop range(inclusive,exlusive,increment range)
for i in range(0,10):
  print(i)
print("Done")
for i in range(0,10,2):
  print(i)
print("Done")
print()


for i in range(97,123):
  print(chr(i))

for i in range(0,26):
  print(chr(i+65), end=" ")
print()
print("Thanks")
print()

#function
def bdtConvert(taka):
  dollar = taka / 85.02
  return dollar

bdtConvert(80000)
print()

#swap
a = 67
b = 36
print(a)
print(b)
a,b=b,a
print(a)
print(b)
print()

#list and function
a=[10,20,30,40,50,60,70]
print(type(a))
print(sum(a))
print(max(a))
print(min(a))
b=[80,90]
a.append(b)
print(a)
print(a[7][0])
for i in a:
  print(i,end=" ")
print()
a.pop()
print(a)
print(a[::2])
print(a[:3])
#enumerate(a) returns two value first is index and second is value
for idx, val in enumerate(a):
  print("index:", idx,"\nvalue ", val)
print()
#formatting
for idx, val in enumerate(a):
  print(f"index {idx} \nvalue {val}")
print()