import pandas
import random
import datetime

from dotenv import load_dotenv
import os
import smtplib


load_dotenv()

password = os.getenv("PASSWORD")
email = os.getenv("EMAIL")


letters_file_name = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt',]
date = datetime.datetime.now()
(day, month) = date.day, date.month

data = pandas.read_csv('birthdays.csv')
birthdays_data = data.to_dict(orient='records')
for birthday in birthdays_data:
    if birthday['day'] == day and birthday['month'] == month:
        letter_file_name = random.choice(letters_file_name)
        with open(f'letter_templates/{letter_file_name}') as letter:
            letter = letter.readlines()
            letter[0] = letter[0].replace('[NAME]', f"{birthday['name']}")
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(email, password)
                connection.sendmail(from_addr=email,
                                    to_addrs=email,
                                    msg=f"Subject:Happy Birthday\n\n{''.join(letter)}")
