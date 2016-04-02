
from collections import OrderedDict
import os


def show(name_of_table):
    name_of_table += '.txt'
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



def sort(name_of_file):
    name_of_file += '.txt'
    try:
        file = open(name_of_file, 'r')
        nfile = open('sort_temp.txt', 'w')
    except OSError:
        print('Table is not exist')
        return

    headers = file.readline()
    header_dict = get_headers(headers)
    try:
        index = list(header_dict.keys()).index('id')
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
	sort('table2')
