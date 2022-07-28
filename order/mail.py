import smtplib
from email.mime.text import MIMEText
import os

astorun_pass = os.environ.get('MAIL_PASS')


def send_email(order, link):
    sender = os.environ.get('MAIL_SENDER')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    receiver = order.customer_email
    order_id = str(order.id)
    order_price = str(order.order_price)
    created = str(order.created)[:16]
    name = order.customer_name

    try:
        message = 'Hello, {}, here you can see an information about your order\n' \
                  'Order ID: {}\n' \
                  'Order price: {} UAH\n' \
                  'Was created: {}\n\n' \
                  'We will contact you as soon as possible\n\n' \
                  'Details about this order you can find here {}\n\n' \
                  'Best regards, ASTORUN.SHOP' .format(name, order_id, order_price, created, link)
        message = MIMEText(message)
        server.login(sender, astorun_pass)
        message['Subject'] = 'We have received your order'
        server.sendmail(sender, receiver, message.as_string())
        print('mail have been sent to customer!')
        return 'OK'


    except Exception as ex:
        return ex


