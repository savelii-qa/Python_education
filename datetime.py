import time
import re


def check_my_date(date):
    try:
        time.strptime(date, '%d/%m/%Y')
        # strtime - конвертирующая функция
        # %d/%m/%Y - задаем формат времни описателями строк
        # %d - день 1-31
        # %m - месяц 1-12
        # %Y - год в четырехзначном формате YYYY
        # Выбрал этот вариант  ввиду того, что он простой и короткий
        # Как вариант иожно было написать код с конструкциями if/elif/else проверяя каждое значение отдельно
        # Для дней это прверка на тип(инта), 1-31, 28-29 для февраля будет зависеть от проверки высокосный год или нет
        # Для месяца тип(инта)б 1-12
        # Для года тип, 1-inf
        print(True)
    except ValueError:
        print(False)


date = input('Enter your value at dd/mm/yyyy format ')
#date = '32/01/2020'

match = re.fullmatch(r'\d\d/\d\d/\d{4}', date)
if not match:
    raise ValueError('Incorrect value')
check_my_date(date)

