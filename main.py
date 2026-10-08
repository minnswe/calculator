import tkinter as tk


# -----------------------------
# Calculator functions
# -----------------------------

def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


# -----------------------------
# Main window
# -----------------------------

root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x500")
root.resizable(False, False)

# -----------------------------
# Display
# -----------------------------

display = tk.Entry(
    root,
    font=("Segoe UI", 28),
    justify="right",
    bd=0
)

display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=20,
    sticky="nsew"
)

# -----------------------------
# Buttons
# -----------------------------

buttons = [
    ("C", 1, 0),
    ("⌫", 1, 1),
    ("(", 1, 2),
    (")", 1, 3),

    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),
    ("/", 2, 3),

    ("4", 3, 0),
    ("5", 3, 1),
    ("6", 3, 2),
    ("*", 3, 3),

    ("1", 4, 0),
    ("2", 4, 1),
    ("3", 4, 2),
    ("-", 4, 3),

    ("0", 5, 0),
    (".", 5, 1),
    ("=", 5, 2),
    ("+", 5, 3),
]


for text, row, column in buttons:

    if text == "C":
        command = clear

    elif text == "⌫":
        command = backspace

    elif text == "=":
        command = calculate

    else:
        command = lambda value=text: button_click(value)

    button = tk.Button(
        root,
        text=text,
        font=("Segoe UI", 18),
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5,
        ipadx=10,
        ipady=10,
        sticky="nsew"
    )


# Make rows and columns expand equally
for i in range(6):
    root.rowconfigure(i, weight=1)

for i in range(4):
    root.columnconfigure(i, weight=1)


root.mainloop()
