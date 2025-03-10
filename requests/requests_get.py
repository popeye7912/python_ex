import requests

# 1. 직접 입력해서 보내기
# url에 보내고자 하는 데이터를 입력해서 전송한다.
URL = "http://google.com?user=comp&num=42"
response = requests.get(URL)
print("status code :", response.status_code)

# 2. dict 이용하기
param = { "user" : "comp", "num" : 42 }
response = requests.get(URL, params=param)
print("status code :", response.status_code)