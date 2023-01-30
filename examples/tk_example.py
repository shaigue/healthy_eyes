import tkinter as tk
import time
window = tk.Tk()

# frame1 = tk.Frame(relief=tk.GROOVE, borderwidth=5)
# frame2 = tk.Frame(relief=tk.SUNKEN, borderwidth=5)

# label = tk.Label(
#     text="hello tkinter",
#     foreground="black",
#     background="white",
#     width=10,
#     height=10,
#     master=frame1,
# )
# label.pack()
# button = tk.Button(
#     text="button",
#     foreground="yellow",
#     background="red",
#     width=10,
#     height=5,
#     master=frame1,
# )
# button.pack()

# entry = tk.Entry(foreground='yellow', background='blue', width=50, master=frame2)
# entry.pack()
# entry.insert(0, 'place your text here')
# print(entry.get())
# entry.delete(0)
# print(entry.get())
# entry.delete(0, 2)
# print(entry.get())

# text_box = tk.Text(master=frame1, width=10, height=10)
# text_box.pack()


# frame1.pack()
# frame2.pack()



# frm3 = tk.Frame(relief=tk.GROOVE, borderwidth=5, master=window)
lbl_counter = tk.Label(text='0',width=10, height=10)
def increase_handler():
    value = int(lbl_counter['text'])
    value += 1
    lbl_counter['text'] = str(value)

def decrese_handler():
    value = int(lbl_counter['text'])
    value -= 1
    lbl_counter['text'] = str(value)
    
btn_increase = tk.Button(text='+', command=increase_handler, width=10, height=10)
btn_decrese = tk.Button(text='-', command=decrese_handler, width=10, height=10)

btn_increase.grid(row=0, column=0)
lbl_counter.grid(row=0, column=1)
btn_decrese.grid(row=0, column=2)

# def key_press_handler(event):
#     # attr = list(filter(lambda s: not s.startswith('_'), dir(event)))
#     # print(attr)
#     print(event.char)

# window.bind('<KeyPress>', key_press_handler)

window.mainloop()