import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "your_email@example.com")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "your_password")

def send_email(to: str, code: str):
    subject = "Your Verification Code"
    body = f"Your verification code is {code}. It is valid for 1 minute."

    msg = MIMEMultipart()
    msg['From'] = SMTP_USERNAME
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        text = msg.as_string()
        server.sendmail(SMTP_USERNAME, to, text)
        server.quit()
        print(f"Email sent to {to}")
    except Exception as e:
        print(f"Failed to send email to {to}. Error: {e}")
        raise
