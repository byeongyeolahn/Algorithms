import random
import pandas as pd
import numpy as np
import csv


def swap(big_value, small_value):
    temp = big_value
    big_value = small_value
    small_value = temp

def Random_number():
    Random_list = list(range(1,1000000))
    random.shuffle(Random_list) # 랜덤 상태
    
    file = open('random_quicksort.csv', 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow(Random_list)
    file.close()




def Forward_sort():
    Forward_list = list(range(1,1000000))
    file = open('Forward_sort.csv', 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow(Forward_list)
    file.close()

def Reverse_sort():
    Reverse_list = list(range(1,1000000))
    Reverse_list.sort(reverse=True)
    
    file = open('Reverse_sort.csv', 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow(Reverse_list)
    file.close()
    
def sort_action():
    Random_csv = pd.read_csv('random_quicksort.csv')
    print(Random_csv.to_string())  
#csv 수정
#     Number_list = []
#     Random_number = []
#     for i in range(1000000):
#         Random_number.append(np.random.randint(1, 100))
    
#     Number_list.append(Random_number)
#     for end in range(1000000):
#         #순방향 정렬 구현하였으나 시간이 많이 걸려 주석 처리
#         # Random_number.append(np.random.randint(1,100))
#         # for i in range(end, 0, -1):
#         #     if i>=1:
#         #         if Random_number[i] < Random_number[i-1]:
#         #             Random_number[i], Random_number[i-1] = Random_number[i-1], Random_number[i]
#                 # swap(Random_number[i-1], Random_number(i))
    
