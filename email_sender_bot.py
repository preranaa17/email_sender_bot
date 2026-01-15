import smtplib
import csv
import time
import logging
from email.message import EmailMessage

# ================= CONFIG =================
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Credentials are NOT hardcoded for security reasons
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "YOUR_GMAIL_APP_PASSWORD"

ATTACHMENT_PATH = "attachment.pdf"   # optional
DELAY = 5  # delay between emails (seconds)
# ==========================================

# Logging setup
logging.basicConfig(
    filename="email_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def send_email(name, receiver_email, server):
    try:
        msg = EmailMessage()
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email
        msg["Subject"] = "Automated Email Notification"

        msg.set_content(f"""
Hello {name},

This is an automated email sent using a Python Email Sender Bot.

Regards,
Email Sender Bot
""")

        # Attachment (optional)
        try:
            with open(ATTACHMENT_PATH, "rb") as file:
                msg.add_attachment(
                    file.read(),
                    maintype="application",
                    subtype="octet-stream",
                    filename=ATTACHMENT_PATH
                )
        except FileNotFoundError:
            pass

        server.send_message(msg)
        logging.info(f"Email sent to {receiver_email}")
        print(f"Email sent to {receiver_email}")

    except Exception as e:
        logging.error(f"Failed to send email to {receiver_email}: {e}")
        print(f"Error sending email to {receiver_email}")

def main():
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, APP_PASSWORD)

    with open("recipients.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            send_email(row["name"], row["email"], server)
            time.sleep(DELAY)

    server.quit()
    print("All emails processed.")

if __name__ == "__main__":
    main()
