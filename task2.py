#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""
import tkinter as tk
from math import sqrt

def calculate_hypotenuse():
    try:
        side1 = float(entry_side1.get())
        side2 = float(entry_side2.get())
        hypotenuse = sqrt(side1**2 + side2**2)
        entry_hypotenuse.delete(0, tk.END)
        entry_hypotenuse.insert(0, f"{hypotenuse:.2f}")
    except ValueError:
        entry_hypotenuse.delete(0, tk.END)
        entry_hypotenuse.insert(0, "Invalid input")

window = tk.Tk()
window.title("Right Triangle Hypotenuse Calculator")

label_side1 = tk.Label(window, text="Side 1:")
label_side1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_side1 = tk.Entry(window)
entry_side1.grid(row=0, column=1, padx=10, pady=10)

label_side2 = tk.Label(window, text="Side 2:")
label_side2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_side2 = tk.Entry(window)
entry_side2.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate Hypotenuse", command=calculate_hypotenuse)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

label_hypotenuse = tk.Label(window, text="Hypotenuse:")
label_hypotenuse.grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_hypotenuse = tk.Entry(window)
entry_hypotenuse.grid(row=3, column=1, padx=10, pady=10)

window.mainloop()
