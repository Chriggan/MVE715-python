import numpy as np
import random

# 1.
def sok(x, Int):
    p=np.logical_and( (Int[0] < x),( x < Int[1] ) )
    v=np.where(p)
    return v

# My test case
""" v = np.array([5,14])
Int = np.array([2, 7, 6, 4, 6, 9, 6, 1, 2])
print(sok(Int, v)) """


# 2. 
def funk(x):
    if x < 3: 
        y = np.cos(x) 
    elif x < 8: 
        y = x * np.sqrt(x)
    else: 
        y = np.sin(x) ** 2
    return y

# 3.
""" from helpers.addition import *
from helpers.addition import addition
print(addition(1,20)) """

# 4.
def max(x):
    return min(x)

# 5.
def omvandla():
    sek = float(input("Ange pris i SEK: "))
    kurs = 0.09
    print(str(sek*kurs) + 'EUR.')
    
# 6.
def number_of_vocals():
    text = input('Skriv in en text: ')
    vokaler = 'aeiouyAEIOUY'
    antal = 0
    for letter in text:
        if letter in vokaler:
            antal += 1 
    print('Din text har ' + str(antal) + ' vokaler')
    
# 7.
def create_unsafe_password():
    lösenord = ''
    bokstäver = ['a' ,'b' ,'c' ,'d' ,'e' ,'f' ,'g' ,'h' ,'i' ,'j' ,'k' ,'l' ,'m' ,'n' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u' ,'v' ,'w' ,'x' ,'y' ,'z']
    längd = int(input("Antal tecken i lösenordet: "))
    tecken = np.arange(1, längd+1)
    for k in tecken:
        slumptal = random.randint(0, len(bokstäver)-1)
        bokstav = bokstäver[slumptal]
        lösenord += bokstav
    print(lösenord)
        
# 8. 
def fix_point_iteration(x):
    return x - (np.cos(x) / 2)

# 9.
def findel(u, v):
    u_indexes = []
    for i, u_item in enumerate(u):
        for v_item in v:
            if u_item == v_item and i not in u_indexes:
                u_indexes.append(i)
    P = np.array(u_indexes)
    return P

# 10.
def faktorisera(n):
    v = n
    for k in range(2,int(np.floor(np.sqrt(n)))):
        if np.mod(n, k) == 0:
            v = [k, int(n/k)]
            break
    return v
