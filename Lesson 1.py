print("Hello world")
# arithmetic operators num
print(10**2)
print(9/3)
print(5 * 7)
print(5 + 5)
print(20 - 10)
# remainder modulus
print(10%3)
import math
print(math.sin(3))
print(math.pi)
print(math.sin(math.pi))
print(math.sin(math.sqrt(4)))
# variables
x = 4
y = 6
z = x + y
print(z)
# relational operator
p = x>y
z = x<=y
# not equal to
t = x !=y
k = (complex(x,y))
print(p)
print(z)
print(t)
print(k)
# logical operators
x = 2
y = 4
e = 3
z = 10
# and(both true) or(at least one) operator
print(x<y and y>z)
print(e>x and z>y)
print(e>x or x<y)
temp_celsius = 10.0
print( "Temperature in Fahreinheit is", temp_celsius * 9/5 + 32)
# updating variables
name = "Brian Otieno "
# \n to form a new line
print(name, "\new laptop")
# to ignore formation of new line using r
print(name,r"\new laptop")
print(10 * name)
cars = 1
temp_celsius = 15.0
temp_fahreinheit = 9/5 * temp_celsius + 32
print("Temperature in celsius is now", temp_celsius)
print("Temperature in celsius is", temp_celsius," and temperature in fahreinheit is", temp_fahreinheit)
# data type
# none is null
print(type(name))
print(type(temp_celsius))
print(type(cars))
print(type(k))
print(type(p))
# character input string
surname = input("What is your name")
age = input("how old are you")
print(surname +' is a nice name and from your age of', age ,"you are  still young!")
station_name = "CK1"
station_lat = 258506.417
station_lon =9855083.229
station_id = 1
station_type = "control"
# converting to another data type
station_id_str = str(station_id)
print(type(station_id_str))
print("Station name is", station_name + ": ," +station_id_str)
# sequence
# creating a list lst
station_names = ['CK1','TMH01', 'TR2', 'TR3', 'TR4', 'TR5', 'TMHO2', 'TMHO3']
print(station_names)
print(len(station_names))
print(station_names[1])
print(station_names[-8])
# printing first three only
print(station_names[0:3])
# printing last three only
print(station_names[5:])
# modifying list value
station_names[0] ="CK2"
print(station_names)
print(type(station_names))
# removing a station to list
del station_names[0]
print(station_names)
del station_names[3:]
# adding a station at the end
station_names.append("TMH04")
print(station_names)
# adding a station at an index value
station_names.insert(2, "CK2")
print(station_names)
# counting no of stations appears
print(station_names.count('TMH04'))
# reverse list of stations
station_names.reverse()
print(station_names)
# sorting alphabetically
station_names.sort()
print(station_names)
# tuple values
t = (2,3,4,5,7,9,8,77,66,55,34)
print(t)
# set values dont follow sequence in plotting
s = {2, 1, 4, 5, 6}
s.pop()
print(s)
# range
print(range(0,10))
print(list(range(10)))
print(set(range(10)))
# printing range at an interval
print(range(2,20,2))
print(list(range(2,20,2)))
# dictionary stores data in set format to prevent editing
d = {"Brian": "Samsung", "John": "Apple", "Mark": "infinix", "Mathew": "Tecno","Peter": "Siemens"}
print(d)
# keys are names
print(d.keys())
# values the things owned use get or square brackets
print(d.get("Brian"))
print(d["Brian"])
# block comments
'''this is an example of a block comment\n i am having fun\n hire me now world'''
print()