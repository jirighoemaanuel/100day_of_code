from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

password = os.getenv("PASSWORD")
email = os.getenv("EMAIL")


with smtplib.SMTP('smtp.gmail.com') as connection:

    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs="emmanueljirigho@gmail.com",
        msg="Subject:Hello\n\nEmail body",
    )
    connection.close()
