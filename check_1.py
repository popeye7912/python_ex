import requests
from bs4 import BeautifulSoup
import csv
import random
from collections import Counter
import urllib3
import datetime, time, math

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

start = time.time()
today = datetime.datetime.now()
now_date = today.strftime('%Y%m%d')
numDate = int(now_date)

dict = {0:'월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}
print('오늘날짜:', today.strftime('%Y-%m-%d'), '(', dict[today.weekday()], ')', sep='')
sunday = today + datetime.timedelta(days=6-today.weekday())

if today.weekday() == 6:
    sunday = today
    print( '오늘은 발표날짜', sunday.strftime('%Y-%m-%d'), '입니다.' )
else:
    monday = today - datetime.timedelta(days=today.weekday())
    print( '이번주 발표날짜', sunday.strftime('%Y-%m-%d'), '입니다.' )



def get_simple_random_number():
    try:
        start = time.time()
        data = random.sample(range(1,46),6)
        end = time.time()
        print(f"Final Simple : ", sorted(data), " , time :", datetime.timedelta(seconds=(end - start)))
        
    except requests.exceptions.RequestException as e:
        print(f"오류가 발생했습니다: {e}")

            
def get_lotto_random_numbers(draw_no):
    # print(f"Loop Count :", draw_no)

    start = time.time()
    final = []
    array = []
    try:
        for drowno in range(0, draw_no):
            data = random.sample(range(1,45),6)

            for num in data:
                array.append(num)
                print("\rCount : ", drowno, end=",  ")

        numbers = Counter(array).most_common(6)
        # print(f"Counter :" , numbers)
        for idx in range(0, 6):
            finalNum = numbers[idx][0]
            final.append(finalNum)

        math.factorial(100000)
        end = time.time()
        print(f"Final 6-Random : ", sorted(final), " , time :", datetime.timedelta(seconds=(end - start)))
        
    except requests.exceptions.RequestException as e:
        print(f"오류가 발생했습니다: {e}")

def get_random_numbers(draw_no):
    for loop in range(0, 2):

        start = time.time()
        final = []
        array = []
        try:
            for drowno in range(0, draw_no*6):
                data = random.sample(range(1,45),1)[0]
                array.append(data)
                print("\rCount : ", drowno, end=",  ")

            numbers = Counter(array).most_common(6)

            for idx in range(0, 6):
                finalNum = numbers[idx][0]
                final.append(finalNum)

            math.factorial(100000)
            end = time.time()
            print(f"Final Random",loop+1 ,":", sorted(final), " , time :", datetime.timedelta(seconds=(end - start)))
            
        except requests.exceptions.RequestException as e:
            print(f"오류가 발생했습니다: {e}")

def maxRound():
    url = "https://dhlottery.co.kr/common.do?method=main"
    html = requests.get(url, verify=False).text
    soup = BeautifulSoup(html, "lxml")
    max_numb = soup.find(name="strong", attrs={"id": "lottoDrwNo"}).text
    return int(max_numb)

get_simple_random_number()
param = random.randint(10000, 50000)
print("param :", param)
# res = get_loop_random_number(param)
param1 = 5000
param2 = 5000*2
# res = get_lotto_random_numbers(random.randint(param1, param2))
# res = get_random_numbers(random.randint(param1, param2))
# print(res)