# function definition
def celsius_to_fahr(temp):
    """Converts celsius temperature to Fahrenheit"""
    return 9 / 5 * temp + 32


# calling function
freezing_point = celsius_to_fahr(0)
print(freezing_point)
print()
print("The boiling point of water is", celsius_to_fahr(100))


# function definition kelvins to Celsius
def kelv_to_cels(temp=0):  # not necessary this defines it to make zero when not input
    """Converts kelvin temperature to celsius"""
    return temp - 273.15


# calling function absolute zero
absolute_zero = kelv_to_cels(0)
print(absolute_zero)


def name_age(name, age):
    return "Hello my name is " + name + " I am" + str(age) + " years old"


output = name_age(name="Brian", age=23)
print(output)


# function within a function
def kelv_to_fahr(temp):
    """Converts kelvin temperature to Fahrenheit"""
    temp_celsius = kelv_to_cels(temp)
    temp_fahr = celsius_to_fahr(temp)
    return temp_fahr


absolute_zero_fahr = kelv_to_fahr(0)
print(absolute_zero_fahr)
print()
# import from script file
from temp_converter import celsius_to_fahr

print("The freezing point of water is", celsius_to_fahr(0))
import temp_converter as tc

print("The boiling point of water is", tc.celsius_to_fahr(100))
print()
# import modules
import math

print(math.sqrt(144))
# binary to appear as integer value
a = bin(14)
print(a)
b = format(14, 'b')
print(b)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.plot([1, 2, 3], [3, 1, 2], '-ko')
plt.show()
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N)) ** 2  # 0 to 15 point radii
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot()
print()