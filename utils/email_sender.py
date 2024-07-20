import os.path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import smtplib

import jinja2

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

    if attachment:
        if_file_exists = os.path.exists(attachment)
        if if_file_exists:
            basename = os.path.basename(attachment)
            filesize = os.path.getsize(attachment)
            file = MIMEBase('application', f'octet-stream; name={basename}')
            file.set_payload(open(attachment, 'br').read())
            file.add_header(
                'Content-Description',
                f'attachment; filename={attachment}, size={filesize}')
            encoders.encode_base64(file)
            msg.attach(file)

    mail = smtplib.SMTP_SSL(SMTP_SERVER)
    mail.login(USER, TOKEN)
    mail.sendmail(from_addr=USER, to_addrs=recipients, msg=msg.as_string())
    mail.quit()


def create_welcome_letter(params: dict) -> str:
    template_loader = jinja2.FileSystemLoader(searchpath='./')
    template_env = jinja2.Environment(loader=template_loader)
    template_file = 'templates/letter_template.html'
    template = template_env.get_template(template_file)
    output = template.render(params)
    return output
