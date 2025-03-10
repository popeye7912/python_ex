import requests
from bs4 import BeautifulSoup
import csv
import random
from collections import Counter
import urllib3
import datetime, time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

start = time.time()
today = datetime.datetime.now()
now_date = today.strftime('%Y%m%d')
numDate = int(now_date)

dict = {0:'월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}
print(today.strftime('%Y-%m-%d'), '(', dict[today.weekday()], ')', sep='')
sunday = today + datetime.timedelta(days=6-today.weekday())

if today.weekday() == 6:
    sunday = today
    print( '<<오늘은 발표날짜', sunday.strftime('%Y-%m-%d'), '>>' )
else:
    monday = today - datetime.timedelta(days=today.weekday())
    print( '<<이번주 발표날짜', sunday.strftime('%Y-%m-%d'), '>>' )

def get_simple_random_number():
    try:
        start = time.time()
        data = random.sample(range(1,46),6)
        end = time.time()
        print(f"Count : 00000, Final Simple : ", sorted(data), " , time :", datetime.timedelta(seconds=(end - start)))
        
    except requests.exceptions.RequestException as e:
        print(f"오류가 발생했습니다: {e}")

def get_lotto_numbers(draw_no, maxnum):
    print(f"Loop Count :", draw_no)

    start = time.time()
    final = []
    array = []
    try:
        for drowno in range(0, draw_no):
            randomNum = random.randint(1, maxnum)
            api_url = f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={randomNum}"

            response = requests.get(api_url, verify=False)
            response.raise_for_status()

            data = response.json()
            # print(f"### {randomNum}회 결과추출 : {data}")

            for i in range(1, 7):
                array.append(data[f"drwtNo{i}"])
                print("\rCount : ", drowno, end=", ")

        numbers = Counter(array).most_common(6)
        # print(f"Counter :" , numbers)
        for idx in range(0, 6):
            finalNum = numbers[idx][0]
            final.append(finalNum)

        end = time.time()
        print(f"Final API : ", sorted(final), " , time :", datetime.timedelta(seconds=(end - start)))

        return {
            'drwNo' : data['drwNo'],
            'date': data['drwNoDate'], 
            'lottoNumb': [str(data[f"drwtNo{i}"]) for i in range(1, 7)], 
            'bonusNumb': data['bnusNo']
        }
        
    except requests.exceptions.RequestException as e:
        print(f"오류가 발생했습니다: {e}")
            
def maxRound():
    url = "https://dhlottery.co.kr/common.do?method=main"
    html = requests.get(url, verify=False).text
    soup = BeautifulSoup(html, "lxml")
    max_numb = soup.find(name="strong", attrs={"id": "lottoDrwNo"}).text
    return int(max_numb)

def get_lotto_random_numbers(draw_no):
    # print(f"Loop Count :", draw_no)

    start = time.time()
    final = []
    array = []
    try:
        for drowno in range(0, draw_no):
            data = random.sample(range(1,46),6)

            for num in data:
                array.append(num)
                print("\rCount : ", drowno, end=", ")

        numbers = Counter(array).most_common(6)
        # print(f"Counter :" , numbers)
        for idx in range(0, 6):
            finalNum = numbers[idx][0]
            final.append(finalNum)

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
                data = random.sample(range(1,46),1)[0]
                array.append(data)
                print("\rCount : ", drowno, end=",  ")

            numbers = Counter(array).most_common(6)

            for idx in range(0, 6):
                finalNum = numbers[idx][0]
                final.append(finalNum)

            end = time.time()
            print(f"Final Random",loop+1 ,":", sorted(final), " , time :", datetime.timedelta(seconds=(end - start)))
            
        except requests.exceptions.RequestException as e:
            print(f"오류가 발생했습니다: {e}")

def get_random_del_number(draw_no):
        start = time.time()
        array = []
        odd = []
        even = []
        try:
            for drowno in range(0, draw_no):
                data = random.sample(range(1,46),6)
                io = drowno % 2
                if io == 0:
                    even.append(sorted(data))
                else:
                    odd.append(sorted(data))
                    
            # print("odd :", odd.__len__())
            # print("even :", even.__len__())
                
            if draw_no%2 == 0:
                array = even
                # print("even array check")
            else:
                array = odd
                # print("odd array check")

            idx = 0
            while True:
                randomnum = random.randint(0, array.__len__())
                if randomnum < array.__len__():
                    del array[randomnum]
                    if array.__len__() == 1:
                        break
                idx = idx + 1
                print("\rCount : ", idx, end=", ")
            
            end = time.time()
            print(f"Final Del Num :", array[0], " , time :", datetime.timedelta(seconds=(end - start)))
            
        except requests.exceptions.RequestException as e:
            print(f"오류가 발생했습니다: {e}")

param1 = 5000
param2 = 5000*4
# res = get_lotto_numbers(random.randint(param1, param2), maxRound())
res = get_lotto_random_numbers(random.randint(param1, param2*10))
res = get_random_numbers(random.randint(param1, param2))
get_random_del_number(random.randint(param1, param2*12))
get_simple_random_number()
# print(res)