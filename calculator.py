import tkinter as tk

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.title("Calculator")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill=tk.X, ipadx=8, padx=10, pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row, col = 1, 0

for button in buttons:
    button_frame = tk.Button(frame, text=button, font="lucida 15 bold", padx=20, pady=20)
    button_frame.grid(row=row, column=col)
    button_frame.bind("<Button-1>", click)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
