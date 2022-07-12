import random
import pandas as pd
import numpy as np
import csv


   
def Random_number():
    Number_list = []
    # for i in range(1000000):
    np.random.seed()
    Random_number = np.random.randint(1, 100, size = 1000000)
    print(Random_number)
    Number_list.append(Random_number)
    print(Number_list)
    random.shuffle(Number_list) # 랜덤 상태
    print(Number_list)
    file = open('random_quicksort.csv', 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow(Number_list)
    file.close()
    #csv 수정

    # CSV 저장하는 것 추가 

