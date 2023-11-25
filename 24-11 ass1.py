import tkinter as tk

def subtract_numbers():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    result_label.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Subtraction App")

label1 = tk.Label(root, text="Enter first number:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

subtract_button = tk.Button(root, text="Subtract", command=subtract_numbers)
subtract_button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()
