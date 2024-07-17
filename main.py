from utils import email_sender


def main():
    list_of_recipients = [
        'vika24358@ukr.net',
        'vika24358@ukr.net',
    ]
    email_sender.send_email(
       recipients=list_of_recipients, mail_subject='Head', mail_body="<h1>BODY!!!!</h1>"
    )


if __name__ == '__main__':
    main()
