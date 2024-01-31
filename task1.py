"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
import tkinter as tk

def display_info():
    name = name_entry.get()
    student_number = student_number_entry.get()
    grade = grade_entry.get()
    
    info_display.delete(0, tk.END) 
    info_display.insert(tk.END, f"Name: {name}\nStudent Number: {student_number}\nGrade: {grade}")

window = tk.Tk()
window.title("Student Information")

name_label = tk.Label(window, text="Name:")
name_entry = tk.Entry(window)

student_number_label = tk.Label(window, text="Student Number:")
student_number_entry = tk.Entry(window)

grade_label = tk.Label(window, text="Grade:")
grade_entry = tk.Entry(window)

display_button = tk.Button(window, text="Enter", command=display_info)

info_display = tk.Entry(window, width=30, state='disabled')

name_label.pack()
name_entry.pack()

student_number_label.pack()
student_number_entry.pack()

grade_label.pack()
grade_entry.pack()

display_button.pack()

info_display.pack()

window.mainloop()

