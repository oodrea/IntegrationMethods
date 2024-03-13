"""
Commandline Program

STMATH S14 | AY 22-23
Group Project | Numerical Integration Methods

Team D:
Jocson, Nicole
Martin, Elaine Riz
Tabadero, Audrea Arjaemi

"""

def midpoint_rule(func, a, b, n):
    # a: Lower bound of the interval
    # b: Upper bound of the interval
    # n: Number of subintervals
    
    h = (b - a) / n
    integral_sum = 0
    
    for i in range(n):
        x_mid = a + (i + 0.5) * h
        fx_mid = eval(func, {'x': x_mid})
        integral_sum += fx_mid * h
        
    return integral_sum

# Trapezoidal Rule
def trapezoidal_rule(func, a, b, n):
    # a: Lower bound of the interval
    # b: Upper bound of the interval
    # n: Number of subintervals
    
    h = (b - a) / n
    integral_sum = 0
    
    integral_sum += (func(a) + func(b)) / 2
    
    # sum of points
    for i in range(1, n):
        x = a + i * h
        integral_sum += func(x)
        
    # final integral approximation
    integral_sum *= h
    
    return integral_sum

# Simpson's Rule
def simpsons_rule(func, a, b, n):
    # a: Lower bound of the interval
    # b: Upper bound of the interval
    # n: Number of subintervals (even number)
    
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be an even number.")
    
    h = (b - a) / n
    integral_sum = func(a) + func(b)
    
    # sum of points
    for i in range(1, n):
        x = a + i * h
        factor = 2 if i % 2 == 0 else 4
        integral_sum += factor * func(x)
        
    # final integral approximation
    integral_sum *= h / 3
    
    return integral_sum

# Actual Riemann Sums
def riemann_sums(func, a, b, n):
    def riemann_sum_left(a, b, n):
        dx = (b - a) / n
        return sum(func(a + i * dx) * dx for i in range(n))

    def riemann_sum_right(a, b, n):
        dx = (b - a) / n
        return sum(func(a + (i + 1) * dx) * dx for i in range(n))

    left_sum = riemann_sum_left(a, b, n) 
    right_sum = riemann_sum_right(a, b, n)

    results = {
        "Left Riemann Sum": left_sum,
        "Right Riemann Sum": right_sum,
    }

    return results


result = 0
user_func = input("Enter the function to integrate (use 'x' as the variable | e.g., 'x**2 + 3*x - 5'): ")
def user_function(x):
    return eval(user_func, {'x': x})

method = 0

# Actual Program; getting input, calculation
while(method==0):
    method = int(input("1. Midpoint Rule \n2. Trapezoidal Rule \n3. Simpson's Rule \n4. Actual Riemann Sums\nSelect an Integration Method: "))
    print()
    
    match method:
        case 1: # midpoint rule
            a = float(input("Enter the Lower Bound of the Interval: "))
            b = float(input("Enter the Upper Bound of the Interval: ")) 
            n = int(input("Enter the Number of Subintervals: "))
            result = midpoint_rule(user_func, a, b, n)
            print("Midpoint Rule | Approximated Integral:", result)
            
        case 2: # trapezoidal rule
            a = float(input("Enter the Lower Bound of the Interval: "))
            b = float(input("Enter the Upper Bound of the Interval: ")) 
            n = int(input("Enter the Number of Subintervals: "))
            result = trapezoidal_rule(user_function, a, b, n)
            print("Trapezoidal Rule | Approximated Integral:", result)

        case 3: # simpson's rule
            a = float(input("Enter the Lower Bound of the Interval: "))
            b = float(input("Enter the Upper Bound of the Interval: ")) 
            n = int(input("Enter the Number of Subintervals: "))
            result = simpsons_rule(user_function, a, b, n)
            print("Simpson's Rule | Approximated Integral:", result)

        case 4: # actual riemann sums
            a = float(input("Enter the Lower Bound of the Interval: "))
            b = float(input("Enter the Upper Bound of the Interval: ")) 
            n = int(input("Enter the Number of Subintervals: "))
            print("Actual Riemann Sums | Approximated Integral:")
            results = riemann_sums(user_function, a, b, n)
            for method, result in results.items():
                print(f"{method}: {result}")

        case _: # invalid input
            method=0
            print("Invalid Input. Please Try Again.")



