# for loop
kenyan_cities = ["Nairobi","Kisumu","Mombasa","Eldoret"]
print(kenyan_cities[0])
print(kenyan_cities[1:])
for city in kenyan_cities:
    print(city)
print()
towns_kenya =["Butere","Nakuru","kitale","thika","lamu"]
for towns in towns_kenya:
    print(towns)
# value stored in towns changes to last in loop
print("After the loop towns is", towns)
# numbers
for value in range(10):
    print(value)
for value in range(2,9,3):
    print(value)
numbers = [2,4,6,8]
for i in range(len(numbers)):
    print("Value of i:", i)
    print("Value of numbers[i] before addition:",numbers[i])
    numbers[i] = numbers[i] + i
    print("Value of numbers[i] after addition:",numbers[i])
    print()
    print()
countries = ["Kenya","Uganda","Tanzania","United states"]
capital = ["Nairobi","Kampala","Dodoma","washington"]
for i in range(len(countries)):
    print(capital[i], "is the capital of",countries[i])
# swapping variables
a = 5
b =6
a,b =b,a # works only in python
print(a)
a =a^b
b =a^b
a =a^b
print(a)
# number format binary octagon hexagon
print(bin(12))
print(oct(12))
print(hex(12))
# bitwise operators
print(~20) # compliment of numbers
print(12 & 13) # and
print(12|13) # or
print(12^13) # x or
print(10<<2) # left shift gaining bits
print(10>>2) # right shift losing bits
# round off
import math
print(math.floor(9.9))
print(math.ceil(9.9))
print(math.pow(3,3))
import math as m # shortening module
print(m.sqrt(100))
# while loops navin
i = 1
while i<=5:
    print("Hello world", i)
    i = i + 1
print()
i = 5
while i>=1:
    print("Hello world",i)
    i = i-1
print()
i = 1

while i<=5:
    print("Hello world",end="")
    j= 1
    while j<=4:
        print(" Am great",end="")
        j=j+1

    i=i+1
    print()
# input for loop
x = int(input("How many candies you want"))
i = 1
while i<=x:
    print("candy")
    i+=1
print("Thank you")
# only 5 candies available
av =5
x = int(input("How many candies you want"))
i = 1
while i<=x:
    if i>av:
        print("out of stock")
        break
    print("candy")
    i+=1
print("Thank you")
print()
# for loop skipping numbers divisible by 3 or 5
for i in range(1,101):

    if i%3==0 or i%5==0  or i%7==0 or i%11==0 or i%13==0:
        continue

    print (i)

print()
# for loop divisible numbers
for i in range(1,101):
    if i%2!=0: # not diviible by 2
        pass
    else:
     print(i)
# conditional statements
temp = int(input("What is the temperature?"))
if temp > 23:
    print("It is hot")
else:
    print("It is not hot.")
weather = "rain"
if weather == "rain":
    print("Wear a raincoat")
else:
    print("Do not wear a raincoat")
# if elif else statements
temp = int(input("What is the temperature?"))
if temp > 0:
    print(temp, "is above freezing temperature")
elif temp == 0:
    print(temp, "is freezing temperature")
else:
    print(temp, "is below freezing temperature")
weather = "snow"
wind = 96
if (weather == "snow") and (wind > 96):
    print("Stay at home")
else:
    print("You can go out")
# combining loops and if ststements
temp = [3, 6, 8, 9, 5, 4, 23, 45, 6, 7, 72]
for t in temp:
    if t > 20:
        print(t)

print()