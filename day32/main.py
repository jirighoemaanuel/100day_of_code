import datetime as dt
from dotenv import load_dotenv
import os
import smtplib
import random

load_dotenv()

password = os.getenv("PASSWORD")
email = os.getenv("EMAIL")


# with smtplib.SMTP('smtp.gmail.com') as connection:

#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(
#         from_addr=email,
#         to_addrs="emmanueljirigho@gmail.com",
#         msg="Subject:Hello\n\nEmail body",
#     )
#     connection.close()


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open('quotes.txt') as quote_file:
        all_qoutes = quote_file.readlines()
        quote = random.choice(all_qoutes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email,
                            to_addrs=email,
                            msg=f"Subject:Monday Motivation\n\n{quote}"
                            )
