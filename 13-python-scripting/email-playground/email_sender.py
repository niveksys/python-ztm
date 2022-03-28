import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# python3 email_sender.py

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Sender'
email['to'] = 'receiver@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

# email.set_content('I am a Python Master!')
email.set_content(html.substitute({'name': 'Receiver'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender@gmail.com', 'password')
    smtp.send_message(email)

    print('all good boss!')
