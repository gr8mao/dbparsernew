import os


def merging_sort(file_name):
    kol = 0
    f = open(file_name, 'r')
    if not f:
        print("\nИсходный файл не может быть прочитан...")
    else:
        while f.readline():
            kol += 1
        f.close()
    k = 1
    while k < kol:
        f = open(file_name, "r")
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
        f2.close()
        f1.close()
        f.close()



        f = open(file_name, "w")
        f1 = open("smsort_1", "r")
        f2 = open("smsort_2", "r")
        line1 = f1.readline()
        line2 = f2.readline()
        while 1:
            if not line1 and not line2:
                break
            i = 0
            j = 0
            while i < k and j < k:
                print('-----')
                print(line1)
                print(line2)
                print('-----')
                if int(line1) < int(line2):
                    f.write(line1)
                    line1 = f1.readline()
                    i += 1
                else:
                    f.write(line2)
                    line2 = f2.readline()
                    j += 1
                while i < k and line1:
                    f.write(line1)
                    line1 = f1.readline()
                    i += 1
                while j < k and line2:
                    f.write(line2)
                    line2 = f2.readline()
                    j += 1
            while line1:
                print(line1)
                f.write(line1)
                line1 = f1.readline()
            while line2:
                print(line2)
                f.write(line2)
                line2 = f2.readline()
        f2.close()
        f1.close()
        f.close()
        k *= 2


    # os.remove("smsort_1")
    # os.remove("smsort_2")


if __name__ == '__main__':
    merging_sort('sort_test.txt')
