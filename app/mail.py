from flask_mailman import EmailMessage


def send_email(subject, body, to):
    msg = EmailMessage(subject, body, 'trashboyshub@gmail.com', [to],
                       reply_to=['trashboyshub@gmail.com'])
    msg.send()