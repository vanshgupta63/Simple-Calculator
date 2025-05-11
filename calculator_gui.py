import tkinter as tk
from tkinter import messagebox


# Function for addition
def add():
    calculate(lambda a, b: a + b)

# Function for subtraction
def subtract():
    calculate(lambda a, b: a - b)

# Function for multiplication
def multiply():
    calculate(lambda a, b: a * b)

# Function for division (with zero check)
def divide():

    def safe_divide(a, b):
        if b == 0:

            # Raise error if trying to divide by zero
            raise ValueError("Cannot divide by zero.")
        
        return a / b
    calculate(safe_divide)



# Function to perform calculation and update result
def calculate(operation):
    try:

        # Get the numbers from input fields
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        # Apply the selected operation (add, subtract, etc.)
        result = operation(num1, num2)

        # Show result in the label
        result_label.config(text=f"Result: {result}")

    except ValueError as e:

        # Show error message if input is invalid
        messagebox.showerror("Error", str(e))


# Create main application window
window = tk.Tk()

 # Title of the window
window.title("Simple Calculator") 

 # Size of the window (width x height)
window.geometry("400x400") 

# Background color
window.config(bg="#f0f0f0")       


# Label and input for first number
tk.Label(window, text="Enter first number:", bg="#f0f0f0").pack(pady=5)

entry1 = tk.Entry(window, width=30)
entry1.pack(pady=5)


# Label and input for second number
tk.Label(window, text="Enter second number:", bg="#f0f0f0").pack(pady=5)

entry2 = tk.Entry(window, width=30)
entry2.pack(pady=5)


# Buttons for each operation
tk.Button(window, text="Add", command=add, width=15, bg="#d1e7dd").pack(pady=5)
tk.Button(window, text="Subtract", command=subtract, width=15, bg="#ffe5b4").pack(pady=5)
tk.Button(window, text="Multiply", command=multiply, width=15, bg="#cfe2ff").pack(pady=5)
tk.Button(window, text="Divide", command=divide, width=15, bg="#f8d7da").pack(pady=5)


# Label to display the result
result_label = tk.Label(window, text="Result: ", bg="#f0f0f0", font=("Arial", 12, "bold"))
result_label.pack(pady=20)

# Start the GUI event loop
window.mainloop()
