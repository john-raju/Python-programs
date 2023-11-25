import tkinter as tk

def calculate_grade():
    sem1 = float(entry1.get())
    sem2 = float(entry2.get())
    sem3 = float(entry3.get())
    sem4 = float(entry4.get())
    sem5 = float(entry5.get())
    sem6 = float(entry6.get())

    cgpa = (sem1 + sem2 + sem3 + sem4 + sem5 + sem6) / 6

    if cgpa >= 10:
        grade = 'O'
    elif cgpa >= 9:
        grade = 'A+'
    elif cgpa >= 8:
        grade = 'A'
    elif cgpa >= 7:
        grade = 'B'
    elif cgpa >= 6:
        grade = 'C'
    elif cgpa >= 5:
        grade = 'D'
    elif cgpa >= 4:
        grade = 'P'
    else:
        grade = 'F'

    result_label.config(text=f"CGPA: {cgpa:.2f}, Grade: {grade}")

root = tk.Tk()
root.title("Grade Calculator")

label1 = tk.Label(root, text="Enter semester 1 marks:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter semester 2 marks:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Enter semester 3 marks:")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()

label4 = tk.Label(root, text="Enter semester 4 marks:")
label4.pack()
entry4 = tk.Entry(root)
entry4.pack()

label5 = tk.Label(root, text="Enter semester 5 marks:")
label5.pack()
entry5 = tk.Entry(root)
entry5.pack()

label6 = tk.Label(root, text="Enter semester 6 marks:")
label6.pack()
entry6 = tk.Entry(root)
entry6.pack()

calculate_button = tk.Button(root, text="Calculate Grade", command=calculate_grade)
calculate_button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()
