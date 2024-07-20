from utils import email_sender


def main():
    list_of_recipients = [
        'vika24358@ukr.net',
        'vika24358@ukr.net',
    ]

    for res in list_of_recipients:
        params = {'recipient_name': res,
                  'company_name': 'The Best Company',
                  'company_email': 'vika24358@gmail.com', 
                  'age': 13}
        body = email_sender.create_welcome_letter(params)
        email_sender.send_email(
            recipients=list_of_recipients, mail_subject='Head', mail_body=body, attachment='data.json'
        )


if __name__ == '__main__':
    main()
