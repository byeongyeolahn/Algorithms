import Quicksort
import time
import sys

if __name__ =="__main__":
    start = time.time()

    Quicksort.Filedata_input()
    end = time.time()
    # Quicksort.pandas_csv()
    print("시간 성능 측정 : ",time.time()-start)