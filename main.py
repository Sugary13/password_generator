from tkinter import *
from tkinter import  messagebox
from random import  choice, randint, shuffle
import pyperclip

LABEL_FONT = ("Arial", 10)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #



def save_password():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if not website or not email_username or not password:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return


    is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \n Email: {email_username}\n "      
                                                  f"Password: {password} \nIs it ok to save?")
    if is_ok:
        with open("data.txt", "a") as f:
            f.write(f"{website} | {email_username} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text="Website:", font=LABEL_FONT)
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:", font=LABEL_FONT)
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=LABEL_FONT)
password_label.grid(column=0, row=3)

# Entries

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2,  sticky="EW")
website_entry.focus()

email_username_entry = Entry(width=35)
email_username_entry.insert(0, "youremailhere@hotmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2,  sticky="EW")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="W")

# Button

generate_button = Button(text="Generate Password", font=LABEL_FONT, command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, font=LABEL_FONT, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()