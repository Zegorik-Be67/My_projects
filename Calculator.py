import re
import tkinter as tk
from tkinter import ttk
import math

def valid_math(value):
    return bool(re.fullmatch(r'[\d+\-*/().\s]+', value))

def on_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def negative():
    current = entry.get()
    if not current:
        return
    if current.startswith('-(') and current.endswith(')'):
        current = current[2:-1]
    else:
        current = f'-({current})'
    entry.delete(0, tk.END)
    entry.insert(0, current)

def sqrt():
    current = entry.get()
    try:
        result_sqrt = math.sqrt(float(current))
        if result_sqrt == int(result_sqrt):
            result_sqrt = int(result_sqrt)
        entry.delete(0, tk.END)
        entry.insert(0, str(result_sqrt))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, 'Ошибка')

def calculate():
    expr = entry.get()
    if valid_math(expr):
        try:
            result = eval(expr)
            if result == int(result):
                result = int(result)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(0, 'Деление на ноль')
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, 'Ошибка')
    else:
        entry.delete(0, tk.END)
        entry.insert(0, 'Неверно')

root = tk.Tk()
root.title('Calculator')
root.geometry('300x300')
root.resizable(False, False)

entry = tk.Entry(root, font=('Arial', 16), justify='right')
entry.grid(row=0, column=0, columnspan = 5, sticky='nsew')

buttons = [
    ('⭠', 1, 0), ('C', 1, 1), ('√', 1, 2), ('+-', 1, 3), ('=', 1, 4),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0), ('.', 5, 2), ('-', 5, 3)
]

for i in range(5):
    root.columnconfigure(i, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)

for text, row, col in buttons:
    if text == '0':
        btn = ttk.Button(text=text, command=lambda t=text: on_click(t))
        btn.grid(row=row, column=col, columnspan= 2, sticky='nsew')
    elif text == '=':
        btn = ttk.Button(text=text, command=calculate)
        btn.grid(row=row, column=col, rowspan= 5, sticky='nsew')
    elif text == '⭠':
        btn = ttk.Button(text=text, command=backspace)
        btn.grid(row=row, column=col, sticky='nsew')
    elif text == 'C':
        btn = ttk.Button(text=text, command=clear)
        btn.grid(row=row, column=col, sticky='nsew')
    elif text == '+-':
        btn = ttk.Button(text=text, command=negative)
        btn.grid(row=row, column=col, sticky='nsew')
    elif text == '√':
        btn = ttk.Button(text=text, command=sqrt)
        btn.grid(row=row, column=col, sticky='nsew')
    else:
        btn = ttk.Button(text=text, command=lambda t=text: on_click(t))
        btn.grid(row=row, column=col, sticky='nsew')

root.mainloop()