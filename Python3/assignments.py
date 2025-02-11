import numpy as np
import matplotlib.pyplot as plt
import math

# 1.
def check_true_statements():
    a = 4
    b = 17
    c = 13

    first = (a > c) or (c < b)
    second = (b == 9) or (a < 13)
    third = a < b
    fourth = a == c
    fifth = c == b-a
    sixth = (a < b) and (c == b)
    seventh = (b > a) and (b != c)
    eighth = not(a <= b)

    statements = [first, second, third, fourth, fifth, sixth, seventh, eighth]
    true_statements_numbers = []

    for i, statement in enumerate(statements):
        if statement:
            true_statements_numbers.append(i + 1)
    return true_statements_numbers

# 2.
def vector_battle(v_main, v_against):
    amount_of_wins_v4 = 0
    i = 0
    for val in v_main:
        if val > v_against[i]:
            amount_of_wins_v4 += 1
        i += 1
    return amount_of_wins_v4

def repetitions_of_number(searched_number, vector):
    same_number_in_vector = 0
    for val in vector:
        if val == searched_number:
            same_number_in_vector += 1 
    return same_number_in_vector

def first_index(v1, v2, v3, v4):
    n = 0
    for val in v2:
        if val < v4[n] < v1[n] < v3[n]:
            return n
        n += 1
        
def sum_of_numbers_bigger_than_seven(vector):
    # Hemmasnickrade koden i multi-line kommentaren
    """     sum = 0
    for val in vector:
        if val > 7: 
            sum += val
            print(sum) """
    return np.sum(vector[vector > 7])

def q_two():
    vector1 = np.array([5, 1, 5, 5, 6, 6, 2, 2, 7, 8, 4, 7, 7, 1, 9, 1, 7, 1, 5, 5, 8, 2, 6, 5, 9, 9, 6, 8, 1, 7, 9, 4, 7, 9, 7, 1, 1, 2, 2, 2, 1, 7, 1, 6, 5, 7, 4, 7, 1, 5, 4, 7, 8, 8, 6, 2, 6, 1, 8, 2, 6, 8, 2, 5, 4, 4, 9, 4, 6, 3, 5, 5, 4, 7, 3, 4, 1, 3, 5, 9, 3, 3, 8, 1, 9, 2, 3, 8, 2, 3, 6, 7, 9, 9, 3, 5, 5, 1, 5, 8, 8, 8, 6, 9, 8, 4, 9, 8, 1, 4, 5, 9, 6, 5, 7, 3, 6, 3, 4, 7, 9, 9, 9, 5, 1, 2, 8, 6, 7, 6, 8, 8, 9, 9, 8, 7, 3, 7, 7, 5, 1, 5, 6, 3, 2, 3, 4, 8, 8, 1])
    vector2 = np.array([6, 8, 7, 3, 3, 1, 7, 8, 8, 4, 7, 8, 5, 6, 4, 4, 9, 9, 5, 6, 9, 3, 6, 2, 2, 1, 5, 7, 6, 6, 2, 6, 6, 5, 5, 2, 6, 1, 7, 6, 9, 3, 4, 5, 5, 6, 4, 1, 3, 2, 7, 4, 7, 9, 7, 2, 1, 3, 2, 7, 9, 2, 8, 1, 9, 2, 8, 9, 6, 8, 5, 6, 6, 1, 1, 6, 8, 2, 6, 6, 6, 3, 9, 6, 6, 9, 6, 9, 3, 7, 8, 6, 6, 2, 6, 7, 6, 9, 8, 6, 1, 3, 7, 9, 6, 4, 9, 9, 7, 5, 4, 4, 4, 2, 9, 3, 1, 1, 4, 2, 8, 2, 7, 8, 8, 8, 1, 1, 4, 8, 8, 9, 1, 1, 8, 5, 2, 7, 7, 8, 3, 4, 5, 6, 6, 3, 5, 5, 2, 7])
    vector3 = np.array([9, 2, 6, 4, 9, 4, 2, 9, 2, 5, 3, 4, 8, 2, 8, 1, 3, 6, 7, 6, 3, 9, 1, 6, 1, 8, 3, 2, 3, 3, 8, 2, 6, 6, 7, 5, 9, 7, 6, 8, 3, 7, 9, 8, 8, 2, 7, 6, 1, 1, 6, 9, 2, 1, 6, 8, 7, 2, 2, 2, 5, 9, 4, 2, 2, 5, 3, 8, 8, 6, 6, 2, 5, 2, 3, 1, 4, 8, 6, 3, 5, 2, 1, 3, 2, 4, 3, 2, 2, 5, 6, 4, 2, 1, 6, 2, 7, 6, 8, 5, 5, 4, 4, 1, 2, 7, 4, 3, 4, 2, 3, 3, 8, 1, 3, 5, 1, 4, 2, 9, 3, 1, 4, 2, 2, 5, 4, 1, 4, 6, 8, 8, 1, 4, 8, 9, 2, 3, 8, 6, 4, 2, 1, 8, 4, 7, 3, 7, 3, 7])
    vector4 = np.array(	[9, 1, 2, 8, 9, 2, 5, 6, 5, 4, 7, 2, 4, 8, 6, 4, 9, 7, 4, 8, 3, 3, 3, 3, 2, 2, 8, 8, 4, 1, 8, 1, 7, 4, 7, 3, 5, 9, 8, 1, 1, 6, 6, 8, 3, 1, 9, 7, 6, 2, 3, 8, 2, 3, 9, 2, 9, 1, 4, 2, 8, 3, 2, 5, 1, 4, 2, 6, 7, 8, 1, 6, 9, 8, 4, 2, 3, 8, 5, 1, 8, 1, 6, 5, 8, 4, 9, 8, 3, 2, 7, 7, 7, 3, 5, 6, 1, 5, 1, 8, 6, 8, 7, 1, 5, 1, 8, 8, 4, 4, 4, 2, 4, 7, 8, 8, 9, 8, 3, 2, 9, 9, 6, 9, 4, 8, 1, 9, 7, 4, 8, 5, 3, 7, 5, 2, 1, 6, 4, 3, 2, 9, 5, 8, 5, 9, 6, 1, 2, 7])
    
    fives_in_v2 = repetitions_of_number(5, vector2)      
    wins_v4 = vector_battle(vector4, vector1)
    the_index = first_index(vector1, vector2, vector3, vector4)
    sum_v3 = sum_of_numbers_bigger_than_seven(vector3)
    
    return fives_in_v2, wins_v4, the_index, sum_v3


# 3.
def find_substring(sentence, substring):
    start_index = sentence.find(substring)
    if start_index == -1:
        return None 

    end_index = start_index + len(substring) 
    
    return (start_index, end_index)
""" print(find_substring('Snart är det sommar', 'd'))
print(find_substring('Snart är det sommar', 'det som'))

print(find_substring('Snart är det sommar', 'sommar'))
print(find_substring('Snart är det sommar', 'är')) """

# 4.
def fn4():
    u=np.genfromtxt('data_jamnt.txt')
    us=np.sort(u)
    m=np.size(u)
    # median=(us[m/2]+us[m//2+1])/2
    median=(us[m//2] + us[m//2 + 1]) / 2
    medel=np.sum(u)/m
    if medel < median:
        print('Medelvärdet är mindre än medianen')
    elif medel > median:
        print('Medelvärdet är större än medianen')
    else:
        print('Medelvärdet och medianen är samma')

# 6.
def sum_of_exp():
    n = 0
    k = 33
    while n <= 150:
        n += 1 / math.log(k - 3)
        k += 1
    return k - 1


# 7.
def fn7():
    summa = 0
    antal = 0
    while summa <= 50:
        tal = int(input('Ange ett heltal mellan 1 och 10\n'))
        summa = summa + tal
        antal = antal + 1
    print('Summan av de ' + str(antal) + ' talen är ' + str(summa))
    
# 8.
def guess_the_number():
    import random
    okand = random.randint(1, 9)
    gissning = 1
    tal = (int(input('Gissa siffran: ')))
    while tal != okand:
        tal = (int(input('Gissa siffran igen: ')))
        gissning = gissning + 1
    return 'Grattis! Gissning nummer ' + str(gissning) + ' blev rätt'
    
# 9.
def reorder_vector():
    v=np.genfromtxt('data.txt')
    vlen = np.size(v)
    u = np.ones(vlen)
    n = -1
    for val in v:
        u[n] = val
        n -= 1
    print('Den nya vektorn är [' + str(u) + ']')
    
# 10. 
def vector_reassemble():
    # v=np.genfromtxt('data.txt')
    v=['a', '0.1', '3+0.9j', '7', 'True'] 
    vlen = int(np.size(v))
    u = np.zeros(vlen, dtype=complex)
    for k in range(vlen):
        try:
            u[k] = complex(v[k])
        except:
            u[k] = complex(real=0, imag=-100)
    
    print('Den nya vektorn är [' + str(u) + ']')
