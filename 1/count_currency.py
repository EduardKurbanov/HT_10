"""
1. Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот.

   Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна "загрузити" деяку кількість банкнот (вибирається номінал і кількість).

   Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом - видається мінімальна кількість банкнот наявного номіналу. P.S. Будьте обережні з використанням "жадібного" алгоритму (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) - в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн., а в наявності є банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).

   Особливості реалізації:

   - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;

   - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:

     - переглянути наявні купюри;

     - змінити кількість купюр;

   - видача грошей для користувачів відбувається в межах наявних купюр;

   - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя, та й, наскільки я розумію, банкомати все, що в нього входить, відкладає в окрему касету.

2. Для кращого засвоєння - перед написанням коду із п.1 - видаліть код для старої програми-банкомату і напишіть весь код наново (завдання на самоконтроль).

   До того ж, скоріш за все, вам прийдеться і так багато чого переписати
"""
from database import get_available_currency, update_available_currency


def console_admin(valid):
    data = get_available_currency()

    while True:
        if valid == "incasation":
            print("*" * 32)
            print("1. look at the obvious banknote: ")  # переглянути наявні купюри
            print("2. change the number of bills: ")  # змінити кількість купюр
            print("3. Exit")
            print("*" * 32)
            menu_item = input("Choose : ")
            if int(menu_item) == 1:
                for i, j in data.items():
                    print(f"denomination {i} -> {j} things")
            elif int(menu_item) == 2:
                for i, j in data.items():
                    print(f"denomination {i} -> {j} things")
                    s_i = input("how many bills do you want to charge -> ")
                    if s_i.isdigit():
                        data[i] = data[i] + abs(int(s_i))
                    else:
                        print("not the number of bills")
                        continue

                update_available_currency(data)
            elif int(menu_item) == 3:
                exit()
            else:
                print("<choice error>")