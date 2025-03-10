import requests
from bs4 import BeautifulSoup
import csv
import random
from collections import Counter
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_global_random_numbers():
    final = []
    array = get_random_numbers()

    numbers = Counter(array).most_common(6)

    for idx in range(0, 6):
        finalNum = numbers[idx][0]
        final.append(finalNum)

    print(f"Final Random :", final)

def get_random_numbers():
    for loop in range(0, 3):
        final = []
        array = []
        try:
            for drowno in range(0, random.randint(5000, 100000)):
                data = random.sample(range(0,10),6)[0]
                array.append(data)
                print("\rCount : ", drowno, end=",  ")

            numbers = Counter(array).most_common(6)

            for idx in range(0, 6):
                finalNum = numbers[idx][0]
                final.append(finalNum)

            print(f"Final Random",loop+1 ,":", final)
            
        except requests.exceptions.RequestException as e:
            print(f"오류가 발생했습니다: {e}")
    return array

def get_test():
    final = []
    array = []
    try:
        for drowno in range(0, random.randint(5000, 100000)):
            data = random.sample(range(0,10),7)[0]
            array.append(data)
            print("\rCount : ", drowno, end=",  ")

        numbers = Counter(array).most_common(6)

        for idx in range(0, 6):
            finalNum = numbers[idx][0]
            final.append(finalNum)

        print(f"Final Random :", final)
        
    except requests.exceptions.RequestException as e:
        print(f"오류가 발생했습니다: {e}")

    return array

res = get_random_numbers()
# res = get_test()