from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()

    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="oops", message="Please make sure you haven't left any fields empty")

    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {
            email} \nPassword: {password} \nIs it okay to save?")

        if is_okay:
            with open('data.txt', mode='a') as data:
                data_info = f"{website} | {email} | {password}\n"
                data.write(data_info)
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas()
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label declarations and grid layout
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

Email_label = Label(text="Email/Username:")
Email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry widgets and grid layout with highlightthickness=0
website_entry = Entry(width=35, highlightthickness=0)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()


email_entry = Entry(width=35, highlightthickness=0)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "emma@gmail.com")


password_entry = Entry(width=19, highlightthickness=0)
password_entry.grid(column=1, row=3)

# Buttons and grid layout with highlightthickness=0
generate_pass_btn = Button(text="Generate Password",
                           highlightthickness=0, command=generate_password)
generate_pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, highlightthickness=0, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
