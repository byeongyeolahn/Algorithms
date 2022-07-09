import random
import pandas as pd
import csv


   
Number_list = []
for i in range(1000000):
    Random_number = random.randint(1, 100)
    random.shuffle(Number_list) # 랜덤 상태
file = open('random_quicksort.csv', 'w', encoding='utf-8', newline='')
csv_writer = csv.writer(file)
csv_writer.writerows(Number_list)
file.close()
#csv 수정

# CSV 저장하는 것 추가 
