from collections import OrderedDict

commands = ['show', 'mktable', 'addnote', 'delnote', 'deltable', 'filter', 'sort', 'jointab']  # Возможные функции
mainPrinted = False  # Флаг о записи вызова функции main
GenPrinted = False  # Флаг о записи общего модуля
main = ''  # Хранение вызовов функций в транслированной программе


def errors_exec(code, *args):  # Модуль ошибок. Выводит текст ошибки на экран в зависимости от кода ошибки и завершает программу
    print({
              # Общие ошибки
              '0101': 'Не найдено ключевое слово',
              # Ошибки команды mktable
              '0201': 'Неверный синтаксис комнады mktable. Не найдено ключевое слово "inwhich"',
              '0202': 'Не указаны спецификации типов в команде mktable. Столбец',
              '0203': 'Указано 2 или более одинаковых поля в команде mktable.',
              # Ошибки команды addnote
              '0301': 'Неверный синтаксис команды addnote. Не найдено ключевое слово ',
              '0302': 'Неверный синтаксис команды addnote. Не найдено название таблицы',
              '0303': 'В команде addnote недопустимое количество символов в аргументе',
              # Ошибки команды deltable
              '0401': 'В команде deltable недопустимое количество аргументов. Найдено ',
              # Ошибки команды sort
              '0501': 'Неверный синтаксис команды sort. Не найдено ключевое слово ',
              '0502': 'Неверное количество аргументов в команде sort. Ожидалось аргументов ',
              # Ошибки команды jointab
              '0601': 'Неверный синтаксис команды jointab. Не найдено ключевое слово ',
              '0602': 'Неверное количество аргументов в команде jointab.',
              # Ошибки команды show
              '0701': 'В команде show недопустимое количество аргументов. Найдено ',
              # Ошибки команды delnote
              '0801': 'Неверный синтаксис команды delnote. Не найдено ключевое слово ',
              '0802': 'Неверно указано условие в команде delnote. Найдено ',
              # Ошибки команды filter
              '0901': 'Неверный синтаксис команды filter. Не найдено ключевое слово ',
              '0902': 'Неверно указано условие в команде filter. Найдено ',
          }.get(code), args[0], '( Строка:', args[1], ')')
    exit(int(code))


def translator(action, *args):  # Функция транслирования файла. Входные данные: код программы, массив аргументов
    global mainPrinted, err, main, GenPrinted 

    if not GenPrinted:  # Запись общего модуля
        file = open('functions', 'r')
        if not file:
            raise IOError
        line = file.read()
        genral = find_between(line, '@GENERAL', '@SEP')
        rez = open('test1.py', 'a')
        rez.write(genral)
        GenPrinted = True

    if action == 'mktable':  # Запись модуля создания таблицы
        file = open('new_funcs', 'r')
        if not file:
            raise IOError
        line = file.read()
        function = find_between(line, '@' + action, '@SEP')  # Считываем код функции-эквивалента из базы
        rez = open('test1.py', 'a')
        res_file = open('test1.py', 'r')
        temp = res_file.read()
        if action not in temp:  # Записана ли функция в выходной файл?
            rez.write(function)
        if not mainPrinted:
            main += "if __name__ == '__main__': \n"
            mainPrinted = True
        main += "\t" + action + "('" + args[0] + "'," + str(args[1]) + ")\n"  # Формирование вызова функции mktable
    # Конец модуля создания таблицы

    if action == 'addnote':  # Запись модуля создания записи в таблице
        file = open('new_funcs', 'r')
        if not file:
            raise IOError
        line = file.read()
        function = find_between(line, '@' + action, '@SEP')
        rez = open('test1.py', 'a')
        res_file = open('test1.py', 'r')
        temp = res_file.read()
        if action not in temp:
            rez.write(function)
        if not mainPrinted:
            main += "if __name__ == '__main__': \n"
            mainPrinted = True
        main += "\t" + action + "('" + args[0] + "'," + str(args[1]) + "," + str(args[2]) + ")\n"
    # Конец addnote

    if action == 'deltable':  # Запись модуля удаления таблицы
        file = open('new_funcs', 'r')
        if not file:
            raise IOError
        line = file.read()
        function = find_between(line, '@' + action, '@SEP')
        rez = open('test1.py', 'a')
        res_file = open('test1.py', 'r')
        temp = res_file.read()
        if action not in temp:
            rez.write(function)
        if not mainPrinted:
            main += "if __name__ == '__main__': \n"
            mainPrinted = True
        main += "\t" + action + "('" + args[0] + "')\n"
    # Конец deltable

    if action == 'sort':  # Запись модуля сортировки таблицы
        file = open('new_funcs', 'r')
        if not file:
            raise IOError
        line = file.read()
        function = find_between(line, '@' + action, '@SEP')
        rez = open('test1.py', 'a')
        res_file = open('test1.py', 'r')
        temp = res_file.read()
        if action not in temp:
            rez.write(function.replace('@key', str(args[1])))
        if not mainPrinted:
            main += "if __name__ == '__main__': \n"
            mainPrinted = True
        main += "\t" + action + "('" + args[0] + "')\n"
    # Конец sort

    if action == 'jointab':  # Запись модуля объедения таблиц
        file = open('new_funcs', 'r')
        if not file:
            raise IOError
        line = file.read()
        function = find_between(line, '@' + action, '@SEP')
        rez = open('test1.py', 'a')
        res_file = open('test1.py', 'r')
        temp = res_file.read()
        if action not in temp:
            rez.write(function)
        if not mainPrinted:
            main += "if __name__ == '__main__': \n"
            mainPrinted = True
        main += "\t" + action + "('" + args[0] + "','" + args[1] + "')\n"
    # Конец jointab

    if action == 'show':  # Запись модуля показа таблицы
        if not mainPrinted:
            main += "if __name__ == '__main__': \n"
            mainPrinted = True
        main += "\t" + action + "('" + args[0] + "')\n"
    # Конец show

    if action == 'delnote':  # Запись модуля удаления записи
        file = open('new_funcs', 'r')
        if not file:
            raise IOError
        line = file.read()
        function = find_between(line, '@' + action + '_' + args[3], '@SEP')
        rez = open('test1.py', 'a')
        res_file = open('test1.py', 'r')
        temp = res_file.read()
        if action not in temp:
            function = function.replace('@key', str(args[1]))
            function = function.replace('@condition', str(args[2]))
            rez.write(function)
        if mainPrinted == 0:
            main += "if __name__ == '__main__': \n"
            mainPrinted = 1
        main += "\t" + action + "('" + args[0] + "')\n"
    # Конец delnote

    if action == 'filter':  # Запись модуля филтер таблицы
        file = open('new_funcs', 'r')
        if not file:
            raise IOError
        line = file.read()
        function = find_between(line, '@' + action + '_' + args[3], '@SEP')
        rez = open('test1.py', 'a')
        res_file = open('test1.py', 'r')
        temp = res_file.read()
        if action not in temp:
            function = function.replace('@key', str(args[1]))
            function = function.replace('@condition', str(args[2]))
            rez.write(function)
        if not mainPrinted:
            main += "if __name__ == '__main__': \n"
            mainPrinted = True
        main += "\t" + action + "('" + args[0] + "')\n"
        # Конец filter


def get_headers(headers):  # Функция создания создания словаря (<Поле в таблице>: <тип данных в поле>)
    types = []
    names = []
    headers = ''.join(headers.split())
    headers = headers.split('|')
    for header in headers:
        header = header.split('>')
        header[0] = header[0][header[0].index('<') + 1:]  # Выделение спецификации типа из строки
        types.append(header[0])
        names.append(header[1])
    return OrderedDict(zip(names, types))  # Возравщает упорядоченный словарь (<Поле в таблице>: <тип данных в поле>)


def check_syntax(command, line_number):  # Функция синатксического и лексического разбора команды
    command = ' '.join(command.split())
    command = command.split(' ')
    action = command[0]

    if action not in commands:  # Проверка ключего слова команды
        errors_exec('0101', action, line_number)

    if action == 'mktable':  # Проверка синтаксиса команды создания таблицы
        if command[2] != 'inwhich':
            errors_exec('0201', action,line_number)
        else:
            command.pop(0)
            command.pop(1)
            name_of_table = command.pop(0)
            temp = ''.join(command)
            temp.replace(' ', '')
            args = temp.split(',')
            n = 0
            for arg in args:
                if arg.find('<str>') != -1 or arg.find('<int>') != -1 or arg.find('<float>') != -1:  # Проверка указания спецификации типов
                    n += 1
                    continue
                else:
                    errors_exec('0202', arg, line_number)
            if n != len(list(get_headers(temp.replace(',','|')).keys())):  # Проверка на указание одинаковых имен полей
                errors_exec('0203','',line_number)

            translator(action, name_of_table, args)  # Передача аргументов команды в транслятор
    # Конец mktable

    if action == 'addnote':  # Проверка синтаксиса команды создания записи в таблице
        command.pop(0)

        try:
            keys = ''.join(command[:command.index('values')])
            keys.replace(' ', '')
        except:
            errors_exec('0301', "values", line_number)

        command = command[command.index('values') + 1:]

        try:
            values = ''.join(command[:command.index('in')])
            values.replace(' ', '')
        except:
            errors_exec('0301', "in", line_number)

        keys = keys.split(',')
        values = values.split(',')

        try:
            name_of_table = command[command.index('in') + 1:].pop(0)
        except:
            errors_exec('0302', name_of_table, line_number)

        for value in values:
            if len(value) > 20:
                errors_exec('0303', value, line_number)

        translator(action, name_of_table, keys, values) # Передача аргументов команды в транслятор
    # Конец addnote в check_syntax

    if action == 'deltable':  # Проверка синтаксиса команды удаление таблицы
        command.pop(0)

        if len(command) > 1 or len(command) == 0:
            errors_exec('0401', command, line_number)

        name_of_table = command.pop()
        translator(action, name_of_table)
    # Конец deltable

    if action == 'sort':  # Проверка синтаксиса команды сортировки таблицы
        command.pop(0)
        name_of_table = command.pop(0)

        try:
            key = command[command.index('by') + 1:]
            if len(key) > 2:
                errors_exec('0502', 1, line_number)
        except:
            errors_exec('0501', "by", line_number)

        key = key.pop(0)
        translator(action, name_of_table, key)
    # Конец sort

    if action == 'jointab':  # Проверка синтаксиса команды объедения таблиц
        command.pop(0)

        if command[1] != 'with':
            errors_exec('0601', 'with', line_number)

        if len(command) > 3:
            errors_exec('0602', '', line_number)

        name_of_table1 = command.pop(0)
        command.pop(0)
        name_of_table2 = command.pop(0)

        translator(action, name_of_table1, name_of_table2) # Передача аргументов команды в транслятор
    # Конец jointab

    if action == 'show':  # Проверка синтаксиса команды показа таблицы
        command.pop(0)

        if len(command) > 1:
            errors_exec('0701', command, line_number)

        name_of_table = command.pop()

        translator(action, name_of_table) # Передача аргументов команды в транслятор
    # Конец show

    if action == 'delnote':  # Проверка синтаксиса команды удаление записи
        command.pop(0)

        if command[1] != 'where':
            errors_exec('0801', 'where', line_number)

        name_of_table = command.pop(0)
        condition = command[command.index('where') + 1:]
        condition = ' '.join(condition)

        if condition.find('=') != -1:
            condition = condition.replace('=','==')

        temp = condition.split(' ')

        if len(temp) < 3:
            errors_exec("0802", condition, line_number)

        key = temp.pop(0)
        print(condition)
        value = temp.pop()
        type = check_type(value)
        translator(action, name_of_table, key, condition, type) # Передача аргументов команды в транслятор
    # Конец delnote

    if action == 'filter':  # Проверка синтаксиса команды филтер таблицы
        command.pop(0)

        if command[1] != 'by':
            errors_exec('0901', 'by', line_number)

        name_of_table = command.pop(0)
        condition = command[command.index('by') + 1:]
        condition = ' '.join(condition)
        temp = condition.split(' ')

        if len(temp) < 3:
            errors_exec("0902", condition, line_number)

        key = temp.pop(0)
        value = temp.pop()
        type = check_type(value)

        translator(action, name_of_table, key, condition, type) # Передача аргументов команды в транслятор
        # Конец filter


def check_type(value):  # Функция проверки типа. Возвращает наименование типа
    if value.isdigit():
        return 'int'
    elif value.isdecimal():
        return 'float'
    else:
        return 'str'


def find_between(s, first, last):  # Функция считывания по разделителям
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


if __name__ == '__main__':  # Функция main
    file = open('test1.py', 'w')
    file.close()
    enter_file = open('to_compile.txt', 'r')
    for index, line in enumerate(enter_file):
        check_syntax(line, index + 1)
    file = open('test1.py', 'a')
    file.write(main)
    print('Файл успешно транслирован')  # Вывод сообщение об успешной транляции
