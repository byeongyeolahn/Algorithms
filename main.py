import Quicksort
import time

if __name__ =="__main__":
    start = time.time()
    Quicksort.Random_number()
    Quicksort.Forward_sort()
    Quicksort.Reverse_sort()
    Quicksort.sort_action()
    end = time.time()
    print(time.time()-start)