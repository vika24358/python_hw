from utils import email_sender


def main():
    list_of_recipients = [
        'vika24358@ukr.net',
        'miroshnicelena@ukr.net',
    ]
    email_sender.send_email(
       list_of_recipients, 'Head', "Body"
    )


if __name__ == '__main__':
    main()
