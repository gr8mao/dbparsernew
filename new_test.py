import os

def merge_sorting(name_of_file):
    pass
    n = 0
    source_file = open(name_of_file, 'r')
    if source_file:
        for line in source_file:
            n += 1
        source_file.close()
    else:
        print('File is not exist')

    k = 1
    while k < n:
        f = open(name_of_file, "r")
        f1 = open("smsort_1", "w")
        f2 = open("smsort_2", "w")
        line = f.readline()
        while 1:
            for i in range(0, k):
                f1.write(line)
                line = f.readline()
                if not line:
                    break
                i += 1
            for j in range(0, k):
                f2.write(line)
                line = f.readline()
                if not line:
                    break
                j += 1
            if not line:
                break
        f.close()
        f1.close()
        f2.close()

        file1 = open('smsort_1','r')
        file_1 = open('smsort_1c','w')
        line_st = file1.readline()
        for line in file1:
            if (int(line) < int(line_st)):
                file_1.write(line)
                file_1.write(line_st)
            else:
                file_1.write(line_st)
                file_1.write(line)
                line_st = line
        # os.remove('smsort_1')
        file_1.close()
        file1.close()

        file2 = open('smsort_2','r')
        file_2 = open('smsort_2c','w')
        line_st = file2.readline()
        for line in file2:
            if (int(line) < int(line_st)):
                file_2.write(line)
                file_2.write(line_st)
            else:
                file_2.write(line_st)
                file_2.write(line)
                line_st = line
        # os.remove('smsort_1')
        file_2.close()
        file2.close()

        result_file = open('sort_test.txt','w')
        file1 = open('smsort_1c','r')
        file2 = open('smsort_2c','r')
        line1 = file1.readline()
        line2 = file2.readline()
        while line1 and line2:
            if int(line2) < int(line1):
                result_file.write(line2)
                line2 = file2.readline()
            else:
                result_file.write(line1)
                line1 = file1.readline()
        


        k *= 2



if __name__ == '__main__':
    merge_sorting('sort_test.txt')
