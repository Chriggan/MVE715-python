import numpy as np
import matplotlib.pyplot as plt
import math

# 1. 
def random_vector(input):
    d = np.array(input)
    return d


# 2.
def second_to_last_element():
    za = np.arange(6, 34, 0.1)
    zb = np.linspace(6, 34, 57)
    return f"a) {za[-3]} \n\n\n b) {zb[-3]}"

# 3. 
def average_from_file(file_path):
    file_data = np.genfromtxt(file_path)
    return np.average(file_data)

# 4.
def analyze_output(input_vector):
    return f"\nshape: {np.shape(input_vector)}\n\nsize: {np.size(input_vector)}"

# 5. 
""" def find_index(searched, input_list):
    i = 0
    for element in input_list:
        if element == searched:
            print("index no.", i)
            return i
        i += 1 

    return "Did not find element" """

def find_index(searched, input_list):
    for i, element in enumerate(input_list):
        if np.isclose(element, searched): 
            print("index no.", i)
            return i
    return None

def alter_elements():
    P=np.array([36.3293536208005, 39.6913349011629, 35.3864172438561, 36.6868414628116, 38.3396900973137, 36.9363176184042, 37.1591481768142, 38.4234574444593, 38.8431905657525, 38.429599328591, 37.8882647832225, 38.1917397157122, 37.2308560921739, 39.2598713529186, 37.0473631360391, 36.3218714102335, 38.1310581802105, 38.2691224428924, 37.0219392928869, 37.4573081614346, 39.0320214470633, 39.119171701376, 39.6587164610054, 38.6947188298058, 36.8953886669057])
    indexFrom = find_index(36.9363176184042, P)
    indexEnd = find_index(37.2308560921739, P) + 1
    P[indexFrom:indexEnd] = 7
    
    return P

# 6.
def vector_addition(n):
    vector = np.array()
    for i in range(n):
        vector += n

    return vector

""" def my_func(n):
    value = 0
    for i in range(1, n+1):
        value += 1/i
        print('iteration number', i-1)
        print(value)
    return value """

# 7.

def velocity(t):
    if t > 0:
        return 4/3*math.cos(math.cos(math.log(t)))
    else:
        raise NotImplementedError("t must be bigger than 0")

def velocity_calc():
    timestamps = np.genfromtxt('./data/q7.txt')
    highest_vel = 0
    time_at_highest_vel = 0

    for time in timestamps:
        vel = velocity(time)
        if vel > highest_vel:
            highest_vel = vel
            time_at_highest_vel = time

    return f"Hastighet: {highest_vel}\n\nTid: {time_at_highest_vel}"

# 8. Använd Jupyter notebook, vet inte hur man gör i terminalen
""" 
import matplotlib.pyplot as plt

a = 5
b = 6
c = 5
d = 5
e = 6
f = 6

plt.plot([5,a,6,b,c],[6,5,d,e,f])
plt.show() """

""" 
y1 = 3
y2 = 0
"""


# 9. 
""" import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2 * np.sin(x - 6) / np.log(2 + x**2)

x = np.linspace(0, 10, 100) 

y = f(x)
y2 = f(f(x))
y3 = f(f(f(x)))

plt.plot(x,y)
#plt.plot(x,y2)
plt.plot(x,y3) """

# 10. 
""" import matplotlib.pyplot as plt
import numpy as np
def h(x):
    return np.cos(x)**2
I = [1, 5]
x = np.linspace(I[0], I[1])
y=h(x)
plt.plot(x, y)
 """