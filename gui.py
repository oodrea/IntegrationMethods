"""
GUI Program

STMATH S14 | AY 22-23
Group Project | Numerical Integration Methods

Team D:
Jocson, Nicole
Martin, Elaine Riz
Tabadero, Audrea Arjaemi

"""

import sys
import tkinter as tk
from tkinter import ttk
import os

# Integration Methods
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


integration_methods = {
    "Midpoint Rule": 1,
    "Trapezoidal Rule": 2,
    "Simpson's Rule": 3,
    "Actual Riemann Sums": 4
}

def calculate_integral():
    user_func = function_entry.get()
    def user_function(x):
        return eval(user_func, {'x': x})
    method = integration_methods.get(method_var.get(), 0)

    try:
        a = float(lower_bound_entry.get())
        b = float(upper_bound_entry.get())
        n = int(subintervals_entry.get())

        if method == 1:
            result = midpoint_rule(user_func, a, b, n)
        elif method == 2:
            result = trapezoidal_rule(user_function, a, b, n)
        elif method == 3:
            result = simpsons_rule(user_function, a, b, n)
        elif method == 4:
            results = riemann_sums(user_function, a, b, n)
            result = "\n".join([f"{method}: {value}" for method, value in results.items()])
        else:
            result = "Invalid Method"

        result_label.config(text=f"Approximated Integral:\n{result}")

    except ValueError:
        tk.messagebox.showerror("Invalid Input", "Please enter valid numerical values for the interval and subintervals.")
    except Exception as e:
        tk.messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("STMATH | Numerical Integration Methods")

script_path = sys.argv[0]
script_directory = os.path.dirname(script_path)
icon_path = os.path.join(script_directory, 'icon.ico')
root.iconbitmap(icon_path)

window_width = 400
window_height = 500
root.geometry(f"{window_width}x{window_height}")
root.resizable(width=False, height=False)


# function input field
function_label = ttk.Label(root, text="Enter Function (use 'x' as the variable)")
function_label.pack(pady=10)
instructions = ttk.Label(root, text="x^n = x**n\nmn = m*n\nex.  x^2 + 3x - 5 = x**2 + 3*x - 5 ")
instructions.pack(anchor="center")
function_entry = ttk.Entry(root, width=30)
function_entry.pack()

# integration method selection dropdown
method_label = ttk.Label(root, text="Select an Integration Method:")
method_label.pack(pady=10)
method_var = tk.StringVar(value="Midpoint Rule")
method_dropdown = ttk.Combobox(root, textvariable=method_var, values=list(integration_methods.keys()), state="readonly")
method_dropdown.pack()

# interval input fields
lower_bound_label = ttk.Label(root, text="Enter the Lower Bound of the Interval:")
lower_bound_label.pack(pady=10)
lower_bound_entry = ttk.Entry(root, width=10)
lower_bound_entry.pack()

upper_bound_label = ttk.Label(root, text="Enter the Upper Bound of the Interval:")
upper_bound_label.pack(pady=10)
upper_bound_entry = ttk.Entry(root, width=10)
upper_bound_entry.pack()

subintervals_label = ttk.Label(root, text="Enter the Number of Subintervals:")
subintervals_label.pack(pady=10)
subintervals_entry = ttk.Entry(root, width=10)
subintervals_entry.pack()

# calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_integral)
calculate_button.pack(pady=10)

# results
result_label = ttk.Label(root, text="Approximated Integral:", font="bold")
result_label.pack(pady=10)

root.mainloop()