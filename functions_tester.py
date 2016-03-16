from collections import OrderedDict


def read_table(nameOfTable):
    try:
        file = open(nameOfTable, 'r')
    except IOError:
        print('Table is not exist')
        return
    data = []
    table = []
    for str in file:
        str = ''.join(str.split())
        temp = str.split('|')
        data.append(temp)
    for elem in data[1:]:
        temp = OrderedDict(zip(data[0], elem))
        table.append(temp)
    return table


def save_table(table, nameOfTable):
    data = []
    for row in table:
        headers = list(row.keys())
        line = []
        for header in headers:
            elem = row[header]
            line.append(elem)
        data.append(line)
    data.insert(0, headers)
    file = open(nameOfTable, 'w')
    for line in data:
        stri = ''
        for elem in line:
            stri += str(elem).ljust(20, " ") + '|'
        file.write(stri.rstrip("|") + '\n')


def show(table):
    data = []
    for row in table:
        headers = list(row.keys())
        line = []
        for header in headers:
            elem = row[header]
            line.append(elem)
        data.append(line)
    data.insert(0, headers)
    for line in data:
        stri = ''
        for elem in line:
            stri += str(elem).ljust(20, " ") + '|'
        print(stri.rstrip("|"))


def addnote(table, keys, values):
    if not len(keys) == len(values):
        print('Wrong number of arguments')
        return
    headers = list(table[0].keys())
    types = []
    names = []
    for header in headers:
        header = header.split('>')
        header[0] = header[0][header[0].index('<') + 1:]
        types.append(header[0])
        names.append(header[1])
    headers = OrderedDict(zip(names, types))
    if all(map(lambda a, b: a == b, keys, list(headers.keys()))):
        i = 0
        value = []
        for item in values:
            if headers[keys[i]] == 'int':
                try:
                    temp = int(item)
                    value.append(temp)
                except IOError:
                    print('Wrong type in', keys[i], ' value', item)
                    return
            elif headers[keys[i]] == 'float':
                try:
                    temp = float(item)
                    value.append(temp)
                except IOError:
                    print('Wrong type in', keys[i], ' value', item)
                    return
            elif headers[keys[i]] == 'str':
                temp = item
                value.append(temp)
            i += 1
        temp = OrderedDict(zip(list(table[0].keys()), value))
        table.append(temp)
        return table


def mkTable(name, args):
    name += '.txt'
    line = ''
    for elem in args:
        if (elem.find('<str>') != -1 or elem.find('<int>') != -1 or elem.find('<float>') != -1) and len(
                elem.split('>')) < 3:
            file = open(name, 'a')  # Проверить создание файла
            line += elem.ljust(15, " ") + '|'
        else:
            print('Wrong type or missing type in', elem)
            return
    file.write(line.rstrip("|") + '\n')


def jointab(table1='', table2=''):
    data1 = read_table(table1)
    data2 = read_table(table2)
    if all(map(lambda a, b: a == b, list(data1[0].keys()), list(data2[0].keys()))):
        # Если столбцы в таблице совпадают, добавить записи из таблицы 1 в таблицу 2 и записать в новый файл
        data1.extend(data2)
        save_table(data1, table1[:table1.index('.')] + table2)
        table = read_table(table1[:table1.index('.')] + table2)
        show(table)
        return
    if all(map(lambda a, b: a != b, list(data1[0].keys()), list(data2[0].keys()))) and (len(data1) == len(data2)):
        values1 = get_values_from_dict(data1, list(data1[0].keys()))
        values2 = get_values_from_dict(data2, list(data2[0].keys()))
        headers = list(data1[0].keys())
        headers.extend(list(data2[0].keys()))
        check = True
        i = 0
        j = 0
        k = 0
        values = []
        temp = []
        while k != len(values1)+len(values2):
            if check:
                temp.append(values1[i])
                temp.append(values1[i+1])
                i += 2
                k += 2
            else:
                temp.append(values2[j])
                temp.append(values2[j+1])
                values.append(temp)
                temp = []
                j += 2
                k += 2
            if k%2 == 0:
                check = not check
        table_ = []
        for elem in values:
            temp = OrderedDict(zip(headers, elem))
            table_.append(temp)
        save_table(table_,table1[:table1.index('.')] + table2)
        show(table_)


def get_values_from_dict(table, keys):
    values = []
    for elem in table:
        for header in keys:
            values.append(elem[header])
    return values


if __name__ == '__main__':
    jointab('test_table.txt','jopa.txt')