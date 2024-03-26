from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # SMTP settings
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = EMAIL
        smtp_password = PASSWORD

        # Create message
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = smtp_username
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(email, smtp_username, text)
        server.quit()

        print("Email sent successfully.")
        return redirect('/')

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
