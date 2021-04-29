import random
import schedule
import time

from twilio.rest import Client

account_sid = 'AC5b082b76df92caeed32973100d59615b'
auth_token = '66d9fbb483f16b3b8da6bdec1675ce7d'
client = Client(account_sid, auth_token)
cellphone = "+12404829395"
twilio_number = "+19164963741"

GOOD_MORNING_QUOTES = [
    "Good Morning, babe! Have an amazing day!",
    "Good Morning, sweet heart. Seize the day!",
    "Hope you have a great day today, my love!",
    "Love you so much, I know that the day is yours",
    "Eat some breakfast, take your vitamins, and have a great day",
    "Good Morning, do notwork too hard, but work hard enough"
]

GOOD_EVENING_QUOTES = [
    "Good Evening, babe",
    "Sleep tight, my love!",
    "Goodnight pumpkin, dream big!",
    "Love you! I hope you dream about me tonight!"
]


def send_message(quotes_list=None):
    if quotes_list is None:
        quotes_list = GOOD_MORNING_QUOTES
    account = account_sid
    token = auth_token
    client = Client(account, token)
    quote = quotes_list[random.randint(0, len(quotes_list) - 1)]

    client.messages.create(to=cellphone,
                           from_=twilio_number,
                           body=quote
                           )


# send a message in the morning
schedule.every().day.at("06:00").do(send_message, GOOD_MORNING_QUOTES)

# send a message in the evening
schedule.every().day.at("20:00").do(send_message, GOOD_EVENING_QUOTES)


while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)
