import random
import pandas as pd
import csv


   
Number_list = []
for i in range(1000000):
    Random_number = random.randint(1,100)
    Number_list.append(Random_number)
    random.shuffle(Number_list) # 랜덤 상태
file = open('random_quicksort.csv', 'w', encoding='utf-8', newline='')
# CSV 저장하는 것 추가 
