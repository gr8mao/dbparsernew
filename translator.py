commands = ['show', 'mktable', 'addnote', 'delnote', 'deltable', 'filter', 'sort', 'jointab']
mainPrinted = 0
GenPrinted = False
table = 'table.txt'
main = ''


def errors_exec(code, *args):
    print({
              '0101': 'Такой команды не существует',
              '0102': 'Неверный синтаксис команды',
              '0103': 'Неверное количество аргументов в команде',
              '0104': 'Не указаны спецификации типов в команде mktable столбец',
              '0105': 'Неверно указано условие в команде'
          }.get(code), args[0])
    exit(0)


def translator(action, *args):
    global mainPrinted, err, main, GenPrinted
    if not GenPrinted:
        file = open('functions', 'r')
        if not file:
            raise IOError
        line = file.read()
        genral = find_between(line, '@GENRAL', '@SEP')
        rez = open('test1.py', 'a')
        rez.write(genral)
        GenPrinted = True
    if action == 'mktable':  # Функция создания таблицы
        file = open('functions', 'r')
        if not file:
            raise IOError
        line = file.read()
        function = find_between(line, '@' + action, '@SEP')
        rez = open('test1.py', 'a')
        if action not in rez.read():
            rez.write(function)
        if mainPrinted == 0:
            main += "if __name__ == '__main__': \n"
            mainPrinted = 1
        main += "\t" + action + "('" + args[0] + "'," + str(args[1]) + ")\n"
    # Конец mktable

    if action == 'addnote':  # Функция создания записи в таблице
        file = open('functions', 'r')
        if not file:
            raise IOError
        line = file.read()
        function = find_between(line, '@' + action, '@SEP')
        rez = open('test1.py', 'a')
        if action not in rez.read():
            rez.write(function)
        if mainPrinted == 0:
            main += "if __name__ == '__main__': \n"
            mainPrinted = 1
        main += "\t" + action + "('" + args[0] + "'," + str(args[1]) + "," + str(args[1]) + ")\n"
    # Конец addnote

    if action == 'deltable':  # Команда удаление таблицы
        pass
    # Конец deltable

    if action == 'sort':  # Команда сортировки таблицы
        pass
    # Конец sort

    if action == 'jointab':  # Команда объедения таблиц
        pass
    # Конец jointab

    if action == 'show':  # Команда показа таблицы
        pass
    # Конец show

    if action == 'delnote':  # Команда удаление записи
        pass
    # Конец delnote

    if action == 'filter':  # Команда филтер таблицы
        pass
        # Конец filter


def reader(command):
    command = ' '.join(command.split())
    command = command.split(' ')
    action = command[0]
    if action not in commands:
        errors_exec('0101', action)
    check_syntax(command, action)


def check_syntax(command, action):
    if action == 'mktable':  # Функция создания таблицы
        if command[2] != 'inwitch':
            errors_exec('0102', action)
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
                    errors_exec('0104', arg)
            temp = []
            temp.append(name_of_table)
            temp.append(args)
            print(temp)
    # Конец mktable

    if action == 'addnote':  # Функция создания записи в таблице
        command.pop(0)
        try:
            keys = ''.join(command[:command.index('values')])
            keys.replace(' ', '')
        except:
            errors_exec('0102', action)
        command = command[command.index('values') + 1:]
        try:
            values = ''.join(command[:command.index('in')])
            values.replace(' ', '')
        except:
            errors_exec('0102', action)
        keys = keys.split(',')
        values = values.split(',')
        try:
            name_of_table = command[command.index('in') + 1:].pop(0)
        except:
            errors_exec('0102', action)

        print(keys, values, name_of_table)
    # Конец addnote

    if action == 'deltable':  # Команда удаление таблицы
        command.pop(0)
        if len(command) > 1:
            errors_exec('0103', action)
        name_of_table = command.pop()
        print(name_of_table)
    # Конец deltable

    if action == 'sort':  # Команда сортировки таблицы
        command.pop(0)
        name_of_table = command.pop(0)
        try:
            key = command[command.index('by') + 1:]
            if len(key) > 2:
                errors_exec('0103', action)
            key = key.pop(0)
        except:
            errors_exec('0102', action)
        try:
            mode = command[command.index(key) + 1:].pop(0)
        except:
            pass
        print(name_of_table, key, mode)
    # Конец sort

    if action == 'jointab':  # Команда объедения таблиц
        command.pop(0)
        if command[1] != 'with':
            errors_exec('0102', action)
        if len(command) > 3:
            errors_exec('0103', action)
        name_of_table1 = command.pop(0)
        command.pop(0)
        name_of_table2 = command.pop(0)
        print(name_of_table1, name_of_table2)
    # Конец jointab

    if action == 'show':  # Команда показа таблицы
        command.pop(0)
        if len(command) > 1:
            errors_exec('0103', action)
        name_of_table = command.pop()
        print(name_of_table)
    # Конец show

    if action == 'delnote':  # Команда удаление записи
        command.pop(0)
        if command[1] != 'where':
            errors_exec('0102', action)
        name_of_table = command.pop(0)
        condition = command[command.index('where') + 1:]
        condition = ' '.join(condition)
        temp = condition.split(' ')
        if len(temp) < 3:
            errors_exec("0105", action)
        key = temp.pop(0)
        print(name_of_table, key, condition)
    # Конец delnote

    if action == 'filter':  # Команда филтер таблицы
        command.pop(0)
        if command[1] != 'by':
            errors_exec('0102', action)
        name_of_table = command.pop(0)
        condition = command[command.index('by') + 1:]
        condition = ' '.join(condition)
        temp = condition.split(' ')
        if len(temp) < 3:
            errors_exec("0105", action)
        key = temp.pop(0)
        print(name_of_table, key, condition)
        # Конец filter


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


if __name__ == '__main__':
    pass
    reader('filter table by id == 1')
    # reader('mktable name inwitch tyt, ewr, we')
