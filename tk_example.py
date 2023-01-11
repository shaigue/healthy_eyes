import tkinter as tk
import time
window = tk.Tk()
label = tk.Label(
    text="hello tkinter",
    foreground="black",
    background="white",
    width=10,
    height=10,
)
label.pack()
button = tk.Button(
    text="button",
    foreground="yellow",
    background="red",
    width=10,
    height=5
)
button.pack()
window.mainloop()
# x = input()
# print(x)
