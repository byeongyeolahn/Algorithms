import random
import pandas as pd
import csv

Number_list = [1000000]
for i in Number_list:
    Random_number = random.randint(1,2147483647)
    Number_list.append(Random_number)
    print(Random_number)
# CSV 저장하는 것 추가 
