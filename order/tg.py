import requests
import os

bot_token = os.environ.get('BOT_TOKEN')
bot_chatID = os.environ.get('CHAT_ID')


def telegram_bot_send_order_text(order, products):
    order_id = str(order.id)
    user_name = str(order.customer_name)
    user_email = str(order.customer_email)
    user_phone = str(order.customer_phone)
    order_price = str(order.order_price)
    delivery_region = str(order.delivery_region)
    if order.delivery_district:
        delivery_district = str(order.delivery_district)
    else:
        delivery_district = "wasn't set"
    delivery_city = str(order.delivery_city)
    nova_poshta = str(order.nova_poshta_departament)
    created = str(order.created)[:16]
    if order.comment:
        comment = str(order.comment)
    else:
        comment = 'no comments'

    items = 'Ordered products:' + '\n'
    i = 1
    for item in products:
        items += str(i) + '. title : ' + item.product.title + '\n'
        items += '  size : ' + item.size + '\n'
        items += '  color : ' + item.color + '\n'
        items += '  quantity : ' + str(item.quantity) + '\n'
        items += '  price per item : ' + str(item.price_per_item) + 'UAH\n'
        i += 1

    bot_message = 'New order created!' + '\n' + created + '\n\n' + 'order id : ' + order_id + '\n' + \
                  'user name : ' + user_name + '\n' + \
                  'user email : ' + user_email + '\n' + \
                  'user phone : ' + user_phone + '\n' + \
                  'order price : ' + order_price + 'UAH' + '\n' + \
                  'comment :' + comment + '\n\n' + \
                  'Delivery' + '\n' + \
                  'region : ' + delivery_region + '\n' + \
                  'district : ' + delivery_district + '\n' + \
                  'city : ' + delivery_city + '\n' + \
                  'nova poshta : ' + nova_poshta + '\n\n'

    bot_message += items

    send_text = 'https://api.telegram.org/bot' + bot_token + \
                '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response.json()


def telegram_bot_send_col_order_text(order, products):
    order_id = str(order.id)
    user_name = str(order.customer_name)
    user_email = str(order.customer_email)
    user_phone = str(order.customer_phone)
    order_price = str(order.order_price)
    discount_percent = str(order.discount_percent)
    delivery_region = str(order.delivery_region)
    if order.delivery_district:
        delivery_district = str(order.delivery_district)
    else:
        delivery_district = "wasn't set"
    delivery_city = str(order.delivery_city)
    nova_poshta = str(order.nova_poshta_departament)
    created = str(order.created)[:16]
    if order.comment:
        comment = str(order.comment)
    else:
        comment = 'no comments'

    items = 'Ordered products:' + '\n'
    i = 1
    for item in products:
        items += str(i) + '. title : ' + item.product.title + '\n'
        items += '  size : ' + item.size + '\n'
        items += '  color : ' + item.color + '\n'
        items += '  price per item : ' + str(item.price_per_item) + 'UAH\n'
        i += 1

    bot_message = 'New COLLECTION order created!' + '\n' + created + '\n\n' + 'order id : ' + order_id + '\n' + \
                  'user name : ' + user_name + '\n' + \
                  'user email : ' + user_email + '\n' + \
                  'user phone : ' + user_phone + '\n' + \
                  'order price : ' + order_price + 'UAH' + '\n' + \
                  'discount : ' + discount_percent + '\n' + \
                  'comment :' + comment + '\n\n' + \
                  'Delivery' + '\n' + \
                  'region : ' + delivery_region + '\n' + \
                  'district : ' + delivery_district + '\n' + \
                  'city : ' + delivery_city + '\n' + \
                  'nova poshta : ' + nova_poshta + '\n\n'

    bot_message += items

    send_text = 'https://api.telegram.org/bot' + bot_token + \
                '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response.json()


def contact_us(data):
    bot_message = 'New massage from "CONTACTS"' + '\n\n'
    bot_message += 'From: ' + data['customer_name'] + '\n'
    bot_message += 'User email: ' + data['customer_email'] + '\n\n'
    bot_message += 'Text: ' + data['customer_message']

    send_text = 'https://api.telegram.org/bot' + bot_token + \
                '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response.json()
