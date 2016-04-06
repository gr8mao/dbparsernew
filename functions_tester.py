from collections import OrderedDict
import os


def show(name_of_table):
    try:
        file = open(name_of_table, 'r')
    except OSError:
        print('Table is not exist')
        return
    index = 5
    print(file.readline().replace('\n', ''))
    for i in range(index - 1):
        line = file.readline().replace('\n', '')
        print(line)
    while line:
        line = file.readline().replace('\n', '')
        ch = input(line)
        if ch == '+':
            pass
        elif ch == '++':
            for i in range(index - 1):
                line = file.readline().replace('\n', '')
                print(line)
        else:
            break


def addnote(name_of_table, keys, values):
    if not len(keys) == len(values):
        print('Wrong number of arguments')
        return
    try:
        file = open(name_of_table, 'r')
    except OSError:
        print('Table is not exist')
        return
    headers = get_headers(file.readline())
    file.close()
    if all(map(lambda a, b: a == b, keys, list(headers.keys()))) and (len(keys) == len(list(headers.keys()))):
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
        stri = ''
        for elem in value:
            stri += str(elem).ljust(20, " ") + '|'
        try:
            file = open(name_of_table, 'a')
        except OSError:
            print('Table is not exist')
            return
        file.write(stri.rstrip("|") + '\n')


def get_headers(headers):
    types = []
    names = []
    headers = ''.join(headers.split())
    headers = headers.split('|')
    for header in headers:
        header = header.split('>')
        header[0] = header[0][header[0].index('<') + 1:]
        types.append(header[0])
        names.append(header[1])
    return OrderedDict(zip(names, types))


def mktable(name, args):
    name += '.txt'
    line = ''
    for elem in args:
        if (elem.find('<str>') != -1 or elem.find('<int>') != -1 or elem.find('<float>') != -1) and len(
                elem.split('>')) < 3:
            file = open(name, 'a')
            line += elem.ljust(15, " ") + '|'
        else:
            print('Wrong type or missing type in', elem)
            return
    file.write(line.rstrip("|") + '\n')
    file.close()


def jointab(name_of_table1, name_of_table2):
    try:
        table1 = open(name_of_table1, 'r')
        table2 = open(name_of_table2, 'r')
    except OSError:
        print('Table is not exist')
        return
    t1_headers = table1.readline()
    t2_headers = table2.readline()
    headers1 = get_headers(t1_headers)
    headers2 = get_headers(t2_headers)
    if all(map(lambda a, b: a == b, list(headers1.keys()), list(headers2.keys()))):
        # Если столбцы в таблице совпадают, добавить записи из таблицы 1 в таблицу 2 и записать в новый файл
        try:
            new_table = open(name_of_table1 + name_of_table2, 'w')
        except OSError:
            print('File can not be created')
            return
        new_table.write(t1_headers)
        for line in table1:
            new_table.write(line)
        for line in table2:
            new_table.write(line)
        table1.close()
        table2.close()
        return
    if all(map(lambda a, b: a != b, list(headers1.keys()), list(headers2.keys()))):
        try:
            new_table = open(name_of_table1 + name_of_table2, 'w')
        except OSError:
            print('File can not be created')
            return
        headers = t1_headers.replace('\n', '|') + t2_headers.replace('\n', '')
        headers = ''.join(headers.split())
        headers = headers.split('|')
        stri = ''
        for header in headers:
            stri += str(header).ljust(20, " ") + '|'
        new_table.write(stri.rstrip("|") + '\n')
        line1 = table1.readline()
        line2 = table2.readline()
        while line1 and line2:
            line = line1.replace('\n', '|') + line2
            line = ''.join(line.split())
            line = line.split('|')
            stri = ''
            for elem in line:
                stri += str(elem).ljust(20, " ") + '|'
            new_table.write(stri.rstrip("|") + '\n')
            line1 = table1.readline()
            line2 = table2.readline()


def delnote(name_of_table, key, value):
    try:
        table = open(name_of_table, 'r')
        file = open('temp.txt', 'w')
    except OSError:
        print('Table is not exist')
        return
    headers = table.readline()
    header_dict = get_headers(headers)
    try:
        index = list(header_dict.keys()).index(key)
    except IndexError:
        print('Key is not exist in this table')
        return
    file.write(headers)
    for line in table:
        line = ''.join(line.split())
        line = line.split('|')
        if int(line[index]) != value:
            stri = ''
            for elem in line:
                stri += str(elem).ljust(20, " ") + '|'
            file.write(stri.rstrip("|") + '\n')
    table.close()
    file.close()
    try:
        table = open(name_of_table, 'w')
        file = open('temp.txt', 'r')
    except OSError:
        print('Table is not exist')
        return
    for line in file:
        table.write(line)


def deltable(name_of_table):  # Ready
    choice = input("Are you sure? (y/n) ")
    if choice is 'y' or 'Y':
        name_of_table += '.txt'
        try:
            os.remove(name_of_table)
        except OSError:
            print('Table is not exist')
            return


def filter(name_of_table, key, value):
    try:
        table = open(name_of_table, 'r')
    except OSError:
        print('Table is not exist')
        return
    headers = table.readline()
    header_dict = get_headers(headers)
    try:
        index = list(header_dict.keys()).index(key)
    except:
        print('Key is not exist in this table')
        return
    print(headers.replace('\n', ''))
    for line in table:
        line = ''.join(line.split())
        line = line.split('|')
        if int(line[index]) > value:
            stri = ''
            for elem in line:
                stri += str(elem).ljust(20, " ") + '|'
            print(stri.rstrip("|"))
    table.close()


def sort(name_of_file, key):
    try:
        file = open(name_of_file, 'r')
        nfile = open('sort_temp.txt', 'w')
    except OSError:
        print('Table is not exist')
        return

    headers = file.readline()
    header_dict = get_headers(headers)
    try:
        index = list(header_dict.keys()).index(key)
    except IndexError:
        print('Key is not exist in this table')
        return

    for line in file:
        nfile.write(line)

    file.close()
    nfile.close()

    service_names = 'temp/temp{0}.txt'

    try:
        source = open('sort_temp.txt', 'r')
    except OSError:
        print('Error. File is not exist')
        return

    total = 0
    for line in source:
        total += 1

    source.close()
    source = open('sort_temp.txt', 'r')

    line1 = source.readline()
    line2 = source.readline()

    for i in range(total + 1):
        exit_file = open(service_names.format(i), 'w')

        if i != 0:
            line1 = source.readline()
            line2 = source.readline()

        while True:
            line_1 = ''.join(line1.split())
            line_1 = line_1.split('|')
            line_2 = ''.join(line2.split())
            line_2 = line_2.split('|')

            if not line1:
                exit_file.write(line2)
                break

            if int(line_2[index]) < int(line_1[index]):
                exit_file.write(line1)
            else:
                tmp = line1
                line1 = line2
                line2 = tmp
                exit_file.write(line1)

            line1 = source.readline()

        source = open(service_names.format(i), 'r')

    file = open(service_names.format(total - 1), 'r')
    os.remove(name_of_file)
    try:
        temp = open(name_of_file,'r')
    except OSError:
        pass
    result = open(name_of_file, 'w')

    result.write(headers)
    while True:
        line = file.readline()
        if line:
            result.write(line)
            print(line)
        else:
            result.close()
            file.close()
            break

if __name__ == '__main__':
    addnote('table2.txt',['id','Name','Fame'],['1','werw','weq'])
