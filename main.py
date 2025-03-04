import tkinter as tk
from tkinter import messagebox

alphats = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar (Direction , plain_text, shift_num):
    caesar_word=""
    if Direction=="decoder":
        shift_num*=-1
    for char in plain_text :
        if char in alphats :
            shift_position=alphats.index(char)+shift_num
            shift_position%=len(alphats)
            caesar_word+=alphats[shift_position]
        else:
            caesar_word+=char
    return caesar_word

def start():
    direction=direction_var.get().lower()
    shift=shift_entry.get()
    text=text_entry.get()
    if not shift.isdigit():
        messagebox.showerror("Error , shift must be number please")
        return
    shift=int(shift)
    result=caesar(Direction=direction,plain_text=text,shift_num=shift)
    result_label.config(text=f" The result of {direction} is {result}")

def reset():
    direction_var.set("encoder")
    text_entry.delete(0,tk.END)
    shift_entry.delete(0,tk.END)
    result_label.config(text="")


#//////////////////////////////

window=tk.Tk()
window.title("Caesar Cipher GUI")
window.geometry("400x300")
window.configure(bg="#f0f0f0")

welcome_label=tk.Label(window,text="Welcome To Our application",bg="#f0f0f0",font=("Arial",14,"bold"),fg="blue")
welcome_label.pack(pady=10)

direction_var=tk.StringVar(value="encoder")
direction_frame=tk.Frame(window,bg="#f0f0f0")
direction_frame.pack()

encoder_radiobutton=tk.Radiobutton(direction_frame,bg="#f0f0f0",text="Encoder",variable=direction_var,value="encoder",font=("AArial",12)).pack(side=tk.LEFT,padx=10)
decoder_radiobutton=tk.Radiobutton(direction_frame,bg="#f0f0f0",text="Decoder",variable=direction_var,value="decoder",font=("AArial",12)).pack(side=tk.LEFT,padx=10)

text_label=tk.Label(window,text="Enter Your word :",bg="#f0f0f0",font=("Arial",12))
text_label.pack(pady=5)
text_entry=tk.Entry(window,bg="#f0f0f0")
text_entry.pack()

shift_label=tk.Label(window,text="Enter Shift number :",bg="#f0f0f0",font=("Arial",12))
shift_label.pack(pady=5)
shift_entry=tk.Entry(window,bg="#f0f0f0")
shift_entry.pack()

result_label=tk.Label(window,text="",bg="#f0f0f0",fg="blue",font=("Arial",12))
result_label.pack(pady=10)

buttons_frame=tk.Frame(window,bg="#f0f0f0")
buttons_frame.pack(pady=10)

start_button=tk.Button(buttons_frame,text="Start",bg="Green",fg="White",font=("Arial",12),command=start).pack(side=tk.LEFT,padx=10)
reset_button=tk.Button(buttons_frame,text="Reset",bg="Red",fg="White",font=("Arial",12),command=reset).pack(side=tk.LEFT,padx=10)

window.mainloop()