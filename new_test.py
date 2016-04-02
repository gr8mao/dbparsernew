def file_sorting(name_of_file):
    service_names = 'temp/temp{0}.txt'

    try:
        source = open(name_of_file, 'r')
    except OSError:
        print('Error. File is not exist')

    total = 0
    for line in source:
        total += 1

    source.close()
    source = open(name_of_file, 'r')

    line1 = source.readline()
    line2 = source.readline()

    for i in range(total + 1):
        exit_file = open(service_names.format(i), 'w')

        if i != 0:
            line1 = source.readline()
            line2 = source.readline()

        while True:
            if not line1:
                exit_file.write(line2)
                break

            if int(line2) < int(line1):
                exit_file.write(line1)
            else:
                tmp = line1
                line1 = line2
                line2 = tmp
                exit_file.write(line1)

            line1 = source.readline()

        source = open(service_names.format(i), 'r')

    file = open(service_names.format(total - 1), 'r')
    result = open(name_of_file, 'w')

    while True:
        line = file.readline()
        if line:
            result.write(line)
        else:
            break


if __name__ == '__main__':
    file_sorting('sort_test.txt')
