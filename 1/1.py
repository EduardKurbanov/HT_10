"""


1. Доповніть програму-банкомат наступним функціоналом:

   - новий пункт меню, який буде виводити поточний курс валют (API Приватбанк)

2. Написати скрипт, який буде приймати від користувача назву валюти і початкову дату.

   - Перелік валют краще принтануть.

   - Також не забудьте указати, в якому форматі коритувач повинен ввести дату.

   - Додайте перевірку, чи введена дата не знаходиться у майбутньому ;)

   - Також перевірте, чи введена правильна валюта.

   Виконуючи запроси до API архіву курсу валют Приватбанку, вивести інформацію про зміну

   курсу обраної валюти (Нацбанк) від введеної дати до поточної. Приблизний вивід наступний:

   Currency: USD

   Date: 12.12.2021

   NBU:  27.1013   -------

   Date: 13.12.2021

   NBU:  27.0241   -0,0772

   Date: 14.12.2021

   NBU:  26.8846   -0,1395

3. Конвертер валют. Прийматиме від користувача назву двох валют і суму (для першої).

   Робить запрос до API архіву курсу валют Приватбанку (на поточну дату) і виконує

   конвертацію введеної суми з однієї валюти в іншу.

P.S. Не забувайте про файл requirements.txt

P.P.S. Не треба сходу ДДОСить Приватбанк - додайте хоча б по 0.5 секунди між запросами.

       Хоч у них і не написано за троттлінг, але будьмо чемними ;)

Інформація для виконання:

- документація API Приватбанка:

  - архів курсів: https://api.privatbank.ua/#p24/exchangeArchive

  - поточний курс: https://api.privatbank.ua/#p24/exchange

- інформація про використання форматування дати в Python: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

- модуль requests: https://docs.python-requests.org/en/latest/

Для уніфікації перевірки, в базі повинні бути 3 користувача:
  ім'я: user1, пароль: user1
  ім'я: user2, пароль: user2
  ім'я: admin, пароль: admin, special_key: admin (у цього коритувача - права інкасатора)
"""

from verification_password_login import verification_password_login
from check_balance import check_balance
from replenish_balance import replenish_balance
from withdraw_balance import withdraw_balance
from count_currency import console_admin
from database import close_database
from exchange_rate_processing import currency_console


def start():
    count = 3
    while True:
        try:
            login = input("enter login: ")
            password = input("enter password: ")
            print("if there is no additional key press skip the step: ")
            special_key = input("enter additional key: ")
            valid = verification_password_login(login, password,special_key)
            while count > 0:
                if valid == "incasation":
                    console_admin(valid)

                if valid:
                    print("*" * 25)
                    print("1. Look at the balance")
                    print("2. Replenish the balance")  # пополнить счет
                    print("3. Withdraw cash")  # снять наличные
                    print("4. Сurrent exchange rate")
                    print("5. Exit")
                    print("*" * 25)
                    menu_item = input("Choose : ")
                    if int(menu_item) == 1:
                        check_balance(login)
                    elif int(menu_item) == 2:
                        replenish_balance(login)
                    elif int(menu_item) == 3:
                        withdraw_balance(login)
                    elif int(menu_item) == 4:
                        currency_console(valid)
                    else:
                        close_database()
                        exit()
                else:
                    count -= 1
                    print(f"attempt -> {count}")
                    break

                if count > 0:
                    continue
                else:
                    print("<exit the program automatically>")
            if count == 0:
                break

        except Exception as err:
            print(f"<error -> {err}>")


if __name__ in "__main__":
    start()
