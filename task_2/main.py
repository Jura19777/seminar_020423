"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.


Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json

def write_order_to_json(item, quantity, price, buyer, date):
    data = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }
    with open('orders1.json', 'w') as write_json:
        json.dump(data, write_json, indent=4, ensure_ascii=False)

write_order_to_json(
    item=['принтер', 'scaner', 'scaner', 'scaner'],
    quantity=[10, 20, 20, 20],
    price=[6700, 10000, 10000, 10000],
    buyer=['Ivanov I.I.', 'Petrov P.P.', 'Petrov P.P.', 'Petrov P.P.'],
    date=['24.09.2017', '11.01.2018', '11.01.2018', '11.01.2018'])