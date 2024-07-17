from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

import config


def send_email(
    *,
    recipients: list[str],
    mail_body: str,
    mail_subject: str,
    attachment: str = None,
):
    TOKEN = config.TOKEN_UKR_NET
    USER = config.MAIL_USER
    SMTP_SERVER = config.SMTP_SERVER

    msg = MIMEMultipart('alternative')
    msg['Subject'] = mail_subject
    msg['From'] = f'<Email was sent from {USER}>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = USER
    msg['Return-Path'] = USER
    msg['X-Mailer'] = 'decorator'

    text_to_send = MIMEText(mail_body, 'html')
    msg.attach(text_to_send)

    mail = smtplib.SMTP_SSL(SMTP_SERVER)
    mail.login(USER, TOKEN)
    mail.sendmail(USER, recipients, msg.as_string())
    mail.quit()
