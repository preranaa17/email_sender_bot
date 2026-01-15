# Email Sender Bot (Python)

## Overview
Email Sender Bot is a Python-based automation project that sends emails using Gmail SMTP.
The program reads recipient details from a CSV file, sends personalized emails,
supports optional attachments, and logs the email sending status.

This project is developed as part of an internship task to demonstrate
Python automation and secure coding practices.

## Features
- Automated email sending using Gmail SMTP
- Reads recipient data from CSV file
- Personalized email content
- Optional attachment support
- Email sending status logging
- Secure handling of credentials (no hardcoded passwords)

## Technologies Used
- Python
- smtplib
- email.message
- CSV module
- Logging module


## Project Structure

├── email_sender_bot.py  
├── recipients.csv  
├── attachment.pdf (optional)  
├── email_log.txt  
└── README.md  

## How It Works
1. The program reads names and email addresses from a CSV file.
2. It establishes a secure connection with Gmail SMTP using TLS.
3. Emails are sent one by one with a fixed delay.
4. The status of each email is recorded in a log file.


## How to Run
1. Install Python 3 on your system.
2. Open the terminal in the project folder.
3. Run the following command:
   python email_sender_bot.py


## Security Note
For security reasons, sensitive credentials such as the Gmail App Password
are not hardcoded in the source code. Placeholder values are used instead.
Users must generate their own Gmail App Password before running the program.

Because of this, authentication errors may occur during execution.
This behavior is intentional and follows secure coding practices.


