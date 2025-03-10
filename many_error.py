# many_error.py
import requests
try:
    a = [1,2]
    print(a[3])
    4/0
except requests.exceptions.RequestException as e:
    print(f"오류 : {e}")
finally:
    print("끝")