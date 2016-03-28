
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
    if len(data) < 2:
        temp = dict(zip(data[0], ['']*len(temp)))
        table.append(temp)
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

def sort(nameOfTable, key, mode='inc'):
    table = read_table(nameOfTable)
    if not table:
        print("Table is not exist")
        return
    headers = get_headers(list(table[0].keys()))
    key = '<' + headers[key] + '>' + key
    if key not in list(table[0].keys()):
        print("No such key in table", nameOfTable)
        return
    if mode == 'inc':
        table = sorted(table, key=lambda d: d[key])
    elif mode == 'dec':
        table = sorted(table, key=lambda d: d[key], reverse=True)
    save_table(table, nameOfTable)
    show(nameOfTable)


if __name__ == '__main__':
	sort('test_table','id','inc')
	show('test_table')
