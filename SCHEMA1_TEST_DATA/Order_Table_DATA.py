import random
import os 

tuple_length = int(input("Order_Table_Data의 데이터를 생성합니다. \n\n 튜플의 갯수를 입력해주세요 : "))
file_name = input("파일 이름을 작성해 주세요 : ")

def make_data_file(tuple_length, file_name):
    path = os.path.dirname(os.path.abspath(__file__))

    fd = open(path + '/data_files/' + file_name + '.txt', 'w')

    for key in range(1, tuple_length + 1):

        fd.write(str(key) + ' ' + str(key) + ' ' + str(random.randint(1, 1000000))+ '\n')
    else:
        fd.close()

make_data_file(tuple_length, file_name)