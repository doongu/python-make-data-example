import random
import os 

CASE = int(input("Order_Table_Data의 데이터를 생성합니다. CASE를 입력해주세요 : "))
file_name = input("파일 이름을 작성해 주세요 : ")

def make_data_file(CASE, file_name):
    Customer_Table_Len = [-1, 1000, 100, 10, 1, 1000, 100, 10, 1]
    CASES = {1 : 100000, 2 : 100000, 3 : 100000, 4 : 100000,
              5 : 1000000, 6 : 1000000,  7 : 1000000 ,  8 : 1000000 }
    

    path = os.path.dirname(os.path.abspath(__file__))

    fd = open(path + '/data_files/' + file_name + '.txt', 'w')

    order_key = 1
    for _ in range(1, CASES[CASE] // Customer_Table_Len[CASE] + 1):
        for customer_key in range(1, Customer_Table_Len[CASE] + 1):
            fd.write(str(order_key) + ' ' + str(customer_key) + ' ' + str(random.randint(1, 1000000))+ '\n')
            order_key += 1
    else:
        fd.close()

make_data_file(CASE, file_name)