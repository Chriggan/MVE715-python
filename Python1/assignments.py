import math 

# 1.
def calculate_fn_value(input):
    # "ln" är "log" i engelsk litteratur
    return math.log(input)


# 2.
def q_two(constant, log_ten, first_angle, arccos_ratio, sqrt_expression):

    log_value = math.log10(log_ten)
    tan_value = math.tan(first_angle)
    arccos_value = math.acos(arccos_ratio)
    squareroot_value = math.sqrt(sqrt_expression)

    return (
        constant*
        log_value-
        tan_value
            )/(
        arccos_value+
        squareroot_value
        )

# 3.
# Testa att assigna alla "namn" till något slumpmässigt 
# i en funktion och se till att inga errors sker, 
# alternativt använd en linter/code editor som pekar ut fel 


# 4a.
# sin(x) = 0.5
# => SyntaxError: cannot assign to function call

# 4b. 

def trig_value(x):
    cos_output = x
    v = math.sqrt(1-cos_output**2)

    return v

# 5.
def q_five():
    x = 1+0.51
    return x

# 6.
def q_six():
    x = 40

    for i in range(10):
        x=(x+2/x) / 2
        print(f"loop number${i}")

    return x

# 7.
def print_help():
    return help(math)

def biggest_denominator(num1, num2):
    return math.gcd(num1, num2)

# 8. 
# Konvertera talet till scientific notation och kontrollera med förstoringsglaset i möbius

# 9. 
def cylinder_cape_area(base_radius, height):
    circumference = 2*math.pi*base_radius
    cape_area = circumference*height
    return cape_area

# 10. 
def q_ten():
    t = math.pi + math.log(7)
    u = math.sin(t - 3)
    v = math.exp(t - u)
    t = t + math.sin(v)
    return t


# Manual test cases
""" 
print("Q1:", calculate_fn_value(3))
print ("Q2:", q_two(13, 9, (math.pi/6)+6, 9/13, 32**2+math.e**4))

print("Q4:", trig_value(0.5))
print("Q5:", q_five())
print("Q6:", q_six())
print("Q7:", biggest_denominator(393, 28))

print("Q9:", cylinder_cape_area(7,8))
print("Q10:", q_ten()) 
"""