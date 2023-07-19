import tkinter as tk
import string
import random
import pyperclip

# Function to generating password
def generate_password():
    length = int(length_var.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Function to copy to clipboard
def copy_to_clipboard():
    generated_password = password_var.get()
    if generated_password:
        pyperclip.copy(generated_password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.configure(bg="black")

# Variable to hold the password length
length_var = tk.StringVar()
length_var.set("12")  # Default password length

# Variable to hold the generated password
password_var = tk.StringVar()
password_var.set("")

# Function to set the password length
def set_password_length():
    try:
        password_length = int(length_var.get())
        if password_length <= 0:
            password_length = 1
        length_var.set(str(password_length))
    except ValueError:
        length_var.set("1")

# Widgets
# Password length label
length_label = tk.Label(window, text="Password Length:")
length_label.pack(pady=10, side="top")
length_label.configure(fg="white" ,bg="black", font=("Arial", 14,"bold" ))

# Password length display
length_entry = tk.Entry(window, textvariable=length_var, width=10)
length_entry.pack(pady=5)
length_entry.configure(fg="white" ,bg="black", font=("Arial", 14,"bold" ))

# Generate password button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)
generate_button.configure(fg="black" ,bg="orangered", font=("Arial", 12,"bold" ))

# Generated password label
password_label = tk.Label(window, text="Generated Password:")
password_label.pack(pady=5)
password_label.configure(fg="white" ,bg="black", font=("Arial", 14,"bold" ))

# Generated password display
generated_password = tk.Label(window, textvariable=password_var, relief="solid", font=("Arial", 12))
generated_password.pack(pady=5)
generated_password.configure(fg="limegreen" ,bg="black", font=("Arial", 14,"bold" ))

# Copy button
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)
copy_button.configure(fg="black" ,bg="orangered", font=("Arial", 12,"bold" ))

# Start the main loop
window.mainloop()