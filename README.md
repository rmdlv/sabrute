<p align="center">
    <img alt="logo" src="https://samp-mobile.com/style/img/logo.png">
</p>

<h1 align="center">Программа для подбора паролей SAMP Mobile</h1>

<p align="center">
    <img alt="Made with Python" src="https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white">
    <img alt="License" src="https://img.shields.io/github/license/UHl0aG9uZWVy/SA-MP-Mobile-Bruteforce?style=flat-square)">
</p>

> Разработчик не несет ответсвенности за неправомерное использование данной программы

## Системные требования
- Windows x64
- Python 3

## Настройка
### Файл с настройками имеет имя settings.json и следующую структуру
| Параметр | Тип |  Значение  |
| - | - | - |
| nickname | string | Никнейм игрока |
| files | array | Пути к основным файлам |
| type | string | Тип файла |
| path | string | Путь к файлу |

## Установка и запуск
```bash
$ pip install -r requirements.txt
$ python bruteforce.py
```

## Сборка
### С использованием [pyinstaller](https://www.pyinstaller.org/)
```bash
$ pyinstaller -F bruteforce.py
```

## Автор
- [VK](https://vk.com/vegvs)
