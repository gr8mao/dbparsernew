
from collections import OrderedDict
import os


def read_table(name_of_table):
    name_of_table += '.txt'
    try:
        file = open(name_of_table, 'r')
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


def save_table(table, name_of_table):
    name_of_table += '.txt'
    data = []
    for row in table:
        headers = list(row.keys())
        line = []
        for header in headers:
            elem = row[header]
            line.append(elem)
        data.append(line)
    data.insert(0, headers)
    file = open(name_of_table, 'w')
    for line in data:
        stri = ''
        for elem in line:
            stri += str(elem).ljust(20, " ") + '|'
        file.write(stri.rstrip("|") + '\n')


def show(name_of_table):
    table = read_table(name_of_table)
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
        
        
def get_headers(headers):
    types = []
    names = []
    for header in headers:
        header = header.split('>')
        header[0] = header[0][header[0].index('<') + 1:]
        types.append(header[0])
        names.append(header[1])
    return OrderedDict(zip(names, types))
    

def get_values_from_dict(table, keys):
    values = []
    for elem in table:
        for header in keys:
            values.append(elem[header])
    return values

def jointab (table1, table2):
    data1 = read_table(table1)
    data2 = read_table(table2)
    if all(map(lambda a, b: a == b, list(data1[0].keys()), list(data2[0].keys()))):
        # Если столбцы в таблице совпадают, добавить записи из таблицы 1 в таблицу 2 и записать в новый файл
        data1.extend(data2)
        save_table(data1, table1 + table2)
        table = read_table(table1 + table2)
        show(table1 + table2)
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
        while k != len(values1) + len(values2):
            if check:
                temp.append(values1[i])
                temp.append(values1[i + 1])
                i += 2
                k += 2
            else:
                temp.append(values2[j])
                temp.append(values2[j + 1])
                values.append(temp)
                temp = []
                j += 2
                k += 2
            check = not check
        table_ = []
        for elem in values:
            temp = OrderedDict(zip(headers, elem))
            table_.append(temp)
        save_table(table_, table1 + table2)
        show(table1 + table2)
if __name__ == '__main__': 
	jointab('test_table','table2')
