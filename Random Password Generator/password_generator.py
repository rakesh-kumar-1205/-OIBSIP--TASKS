from tkinter import *
import random
import string
import pyperclip


def generate_password():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all_chars = small_alphabets + capital_alphabets + numbers + special_characters
    password_length = int(length_Box.get())

    password = ''.join(random.sample(all_chars, password_length))
    password_Field.delete(0, END)
    password_Field.insert(0, password)


def copy():
    random_password = password_Field.get()
    pyperclip.copy(random_password)


root = Tk()
root.config(bg="black")
choice = IntVar()
Font = ('arial', 12, 'bold')

# Password Generator Label
password_Label = Label(root, text='Password Generator:', fg="white", bg="black", font=Font)
password_Label.pack(pady=5)

# Radio Buttons
weak_button = Radiobutton(root, text="Weak Password", variable=choice, value=1, font=Font)
weak_button.pack(pady=5)

medium_button = Radiobutton(root, text="Medium Password", variable=choice, value=2, font=Font)
medium_button.pack(pady=5)

strong_button = Radiobutton(root, text="Strong Password", variable=choice, value=3, font=Font)
strong_button.pack(pady=5)

# Password Length Label
length_Label = Label(root, text="Password Length", fg="white", bg="black", font=Font)
length_Label.pack()

# Password Length Spinbox
length_Box = Spinbox(root, from_=5, to=20, fg="white", bg="black", font=Font)
length_Box.pack(pady=5)

# Generate Button
generate_Button = Button(root, text='Generate', font=Font, command=generate_password)
generate_Button.pack(pady=5)

# Password Field Entry
password_Field = Entry(root, fg="white", bg="black", font=Font)
password_Field.pack(pady=10)

# Copy Button
copy_Button = Button(root, text='Copy', font=Font, command=copy)
copy_Button.pack(pady=5)

root.mainloop()
