commands = ['show', 'mktable', 'addnote', 'delnote', 'deltable', 'filter', 'sort', 'jointab']
mainPrinted = False
GenPrinted = False
table = 'table.txt'
main = ''


def errors_exec(code, *args):
    print({
              # Общие ошибки
              '0101': 'Не найдено ключевое слово',
              # Ошибки команды mktable
              '0201': 'Неверный синтаксис комнады mktable. Не найдено ключевое слово "inwhich"',
              '0202': 'Не указаны спецификации типов в команде mktable. Столбец',
              # Ошибки команды addnote
              '0301': 'Неверный синтаксис команды addnote. Не найдено ключевое слово ',
              '0302': 'Неверный синтаксис команды addnote. Не найдено навзвание таблицы',
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
          }.get(code), args[0], '(Строка: ', args[1], ')')
    exit(0)


def translator(action, *args):
    global mainPrinted, err, main, GenPrinted

    if not GenPrinted:
        file = open('new_funcs', 'r')
        if not file:
            raise IOError
        line = file.read()
        genral = find_between(line, '@GENERAL', '@SEP')
        rez = open('test1.py', 'a')
        rez.write(genral)
        GenPrinted = True

    if action == 'mktable':  # Функция создания таблицы ready
        file = open('new_funcs', 'r')
        if not file:
            raise IOError
        line = file.read()
        function = find_between(line, '@' + action, '@SEP')
        rez = open('test1.py', 'a')
        temp1 = open('test1.py', 'r')
        temp = temp1.read()
        if action not in temp:
            rez.write(function)
        if not mainPrinted:
            main += "if __name__ == '__main__': \n"
            mainPrinted = True
        main += "\t" + action + "('" + args[0] + "'," + str(args[1]) + ")\n"
    # Конец mktable

    if action == 'addnote':  # Функция создания записи в таблице ready
        file = open('new_funcs', 'r')
        if not file:
            raise IOError
        line = file.read()
        function = find_between(line, '@' + action, '@SEP')
        rez = open('test1.py', 'a')
        temp1 = open('test1.py', 'r')
        temp = temp1.read()
        if action not in temp:
            rez.write(function)
        if not mainPrinted:
            main += "if __name__ == '__main__': \n"
            mainPrinted = True
        main += "\t" + action + "('" + args[0] + "'," + str(args[1]) + "," + str(args[2]) + ")\n"
    # Конец addnote

    if action == 'deltable':  # Команда удаление таблицы ready
        file = open('new_funcs', 'r')
        if not file:
            raise IOError
        line = file.read()
        function = find_between(line, '@' + action, '@SEP')
        rez = open('test1.py', 'a')
        temp1 = open('test1.py', 'r')
        temp = temp1.read()
        if action not in temp:
            rez.write(function)
        if not mainPrinted:
            main += "if __name__ == '__main__': \n"
            mainPrinted = True
        main += "\t" + action + "('" + args[0] + "')\n"
    # Конец deltable

    if action == 'sort':  # Команда сортировки таблицы *переделать*
        file = open('new_funcs', 'r')
        if not file:
            raise IOError
        line = file.read()
        function = find_between(line, '@' + action, '@SEP')
        rez = open('test1.py', 'a')
        temp1 = open('test1.py', 'r')
        temp = temp1.read()
        if action not in temp:
            rez.write(function.replace('@key', str(args[1])))
        if not mainPrinted:
            main += "if __name__ == '__main__': \n"
            mainPrinted = True
        main += "\t" + action + "('" + args[0] + "')\n"
    # Конец sort

    if action == 'jointab':  # Команда объедения таблиц
        file = open('new_funcs', 'r')
        if not file:
            raise IOError
        line = file.read()
        function = find_between(line, '@' + action, '@SEP')
        rez = open('test1.py', 'a')
        temp1 = open('test1.py', 'r')
        temp = temp1.read()
        if action not in temp:
            rez.write(function)
        if not mainPrinted:
            main += "if __name__ == '__main__': \n"
            mainPrinted = True
        main += "\t" + action + "('" + args[0] + "','" + args[1] + "')\n"
    # Конец jointab

    if action == 'show':  # Команда показа таблицы
        if not mainPrinted:
            main += "if __name__ == '__main__': \n"
            mainPrinted = True
        main += "\t" + action + "('" + args[0] + "')\n"
    # Конец show

    if action == 'delnote':  # Команда удаление записи
        file = open('new_funcs', 'r')
        if not file:
            raise IOError
        line = file.read()
        function = find_between(line, '@' + action + '_' + args[3], '@SEP')
        rez = open('test1.py', 'a')
        temp1 = open('test1.py', 'r')
        temp = temp1.read()
        if action not in temp:
            function = function.replace('@key', str(args[1]))
            function = function.replace('@condition', str(args[2]))
            rez.write(function)
        if mainPrinted == 0:
            main += "if __name__ == '__main__': \n"
            mainPrinted = 1
        main += "\t" + action + "('" + args[0] + "')\n"
    # Конец delnote

    if action == 'filter':  # Команда филтер таблицы
        file = open('new_funcs', 'r')
        if not file:
            raise IOError
        line = file.read()
        function = find_between(line, '@' + action + '_' + args[3], '@SEP')
        rez = open('test1.py', 'a')
        temp1 = open('test1.py', 'r')
        temp = temp1.read()
        if action not in temp:
            function = function.replace('@key', str(args[1]))
            function = function.replace('@condition', str(args[2]))
            rez.write(function)
        if not mainPrinted:
            main += "if __name__ == '__main__': \n"
            mainPrinted = True
        main += "\t" + action + "('" + args[0] + "')\n"
        # Конец filter


def reader(command, line_number):
    command = ' '.join(command.split())
    command = command.split(' ')
    action = command[0]
    if action not in commands:
        errors_exec('0101', action, line_number)
    check_syntax(command, action, line_number)


def check_syntax(command, action, line_number):
    if action == 'mktable':  # Функция создания таблицы
        if command[2] != 'inwhich':
            errors_exec('0201', action)
        else:
            command.pop(0)
            command.pop(1)
            name_of_table = command.pop(0)
            args = ''.join(command)
            args.replace(' ', '')
            args = args.split(',')
            for arg in args:
                if arg.find('<str>') != -1 or arg.find('<int>') != -1 or arg.find('<float>') != -1:
                    continue
                else:
                    errors_exec('0202', arg, line_number)
            translator(action, name_of_table, args)
    # Конец mktable

    if action == 'addnote':  # Функция создания записи в таблице
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
        translator(action, name_of_table, keys, values)
    # Конец addnote в check_syntax

    if action == 'deltable':  # Команда удаление таблицы
        command.pop(0)
        if len(command) > 1 or len(command) == 0:
            errors_exec('0401', command, line_number)
        name_of_table = command.pop()
        translator(action, name_of_table)
    # Конец deltable

    if action == 'sort':  # Команда сортировки таблицы
        command.pop(0)
        name_of_table = command.pop(0)
        try:
            key = command[command.index('by') + 1:]
            if len(key) > 2:
                errors_exec('0502', 1, line_number)
        except:
            errors_exec('0501', "by", line_number)
        key = key.pop(0)
        # try:
        #     mode = command[command.index(key) + 1:].pop(0)
        # except:
        #     pass
        translator(action, name_of_table, key)
    # Конец sort

    if action == 'jointab':  # Команда объедения таблиц
        command.pop(0)
        if command[1] != 'with':
            errors_exec('0601', 'with', line_number)
        if len(command) > 3:
            errors_exec('0602', '', line_number)
        name_of_table1 = command.pop(0)
        command.pop(0)
        name_of_table2 = command.pop(0)
        translator(action, name_of_table1, name_of_table2)
    # Конец jointab

    if action == 'show':  # Команда показа таблицы
        command.pop(0)
        if len(command) > 1:
            errors_exec('0701', command, line_number)
        name_of_table = command.pop()
        translator(action, name_of_table)
    # Конец show

    if action == 'delnote':  # Команда удаление записи
        command.pop(0)
        if command[1] != 'where':
            errors_exec('0801', 'where', line_number)
        name_of_table = command.pop(0)
        condition = command[command.index('where') + 1:]
        condition = ' '.join(condition)
        temp = condition.split(' ')
        if len(temp) < 3:
            errors_exec("0802", condition, line_number)
        key = temp.pop(0)
        print(condition)
        value = temp.pop()
        type = check_type(value)
        translator(action, name_of_table, key, condition, type)
    # Конец delnote

    if action == 'filter':  # Команда филтер таблицы
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
        translator(action, name_of_table, key, condition, type)
        # Конец filter


def check_type(value):
    if value.isdigit():
        return 'int'
    elif value.isdecimal():
        return 'float'
    else:
        return 'str'


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


if __name__ == '__main__':
    file = open('test1.py', 'w')
    file.close()
    enter_file = open('to_compile.txt', 'r')
    for index, line in enumerate(enter_file):
        reader(line, index + 1)
    file = open('test1.py', 'a')
    file.write(main)
