import tkinter as tk
from tkinter import messagebox

# Alphabet list
alphats = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Caesar cipher function
def caesar(direction, plain_text, shift_num):
    caesar_word = ""
    if direction == "decoder":
        shift_num *= -1
    for char in plain_text:
        if char in alphats:
            shift_position = alphats.index(char) + shift_num
            shift_position %= len(alphats)
            caesar_word += alphats[shift_position]
        else:
            caesar_word += char  # Keep non-alphabet characters as they are
    return caesar_word

# Function to handle the "Start" button click
def start():
    direction = direction_var.get().lower()
    text = text_box.get()
    shift = shift_box.get()

    # Validate shift amount
    if not shift.isdigit():
        messagebox.showerror("Error", "Shift amount must be a number!")
        return

    shift = int(shift)
    result = caesar(direction, text, shift)
    result_label.config(text=f"The Result of {direction} is: {result}")

# Function to handle the "Reset" button click
def reset():
    direction_var.set("encoder")
    text_box.delete(0, tk.END)
    shift_box.delete(0, tk.END)
    result_label.config(text="")

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher GUI")
window.geometry("400x300")  # Adjusted window size
window.configure(bg="#f0f0f0")  # Set background color

# Load and display the image
source_image = tk.PhotoImage(file=r"D:\Python Study\Python projects\Caesar word\Artboard 1.png")
label_image = tk.Label(window, image=source_image, bg="#f0f0f0")
label_image.pack(pady=10)

# Direction selection (Encoder/Decoder)
direction_var = tk.StringVar(value="encoder")
direction_frame = tk.Frame(window, bg="#f0f0f0")
direction_frame.pack()

tk.Radiobutton(direction_frame, text="Encoder", variable=direction_var, value="encoder", bg="#f0f0f0", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
tk.Radiobutton(direction_frame, text="Decoder", variable=direction_var, value="decoder", bg="#f0f0f0", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

# Text input
text_label = tk.Label(window, text="Enter Your Text:", bg="#f0f0f0", font=("Arial", 12))
text_label.pack(pady=5)
text_box = tk.Entry(window, font=("Arial", 12))
text_box.pack()

# Shift amount input
shift_label = tk.Label(window, text="Enter Shift Number:", bg="#f0f0f0", font=("Arial", 12))
shift_label.pack(pady=5)
shift_box = tk.Entry(window, font=("Arial", 12))
shift_box.pack()

# Result label
result_label = tk.Label(window, text="", bg="#f0f0f0", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start", command=start, bg="#4CAF50", fg="white", font=("Arial", 12))
start_button.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(button_frame, text="Reset", command=reset, bg="#f44336", fg="white", font=("Arial", 12))
reset_button.pack(side=tk.LEFT, padx=10)

# Run the application
window.mainloop()