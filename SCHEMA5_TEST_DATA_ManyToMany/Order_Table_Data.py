import random
import os 

CASE = int(input("Order_Table_Data의 데이터를 생성합니다. CASE를 입력해주세요 : "))
file_name = input("파일 이름을 작성해 주세요 : ")

def make_data_file(CASE, file_name):
    Customer_Table_Len = [-1, 1, 10, 100, 1, 10, 100, 1000]
    CASES = {1 : 100000, 2 : 10000, 3 : 1000, 4 : 1000000,
              5 : 100000, 6 : 10000,  7 : 1000 }
    

    path = os.path.dirname(os.path.abspath(__file__))

    fd = open(path + '/data_files/' + file_name + '.txt', 'w')

    for order_key in range(1, CASES[CASE]  + 1):
        for customer_key in range(1, Customer_Table_Len[CASE] + 1):
            fd.write(str(order_key) + ' ' + str(customer_key) + ' ' + str(random.randint(1, 1000000))+ '\n')

    else:
        fd.close()

make_data_file(CASE, file_name)