import datetime

# 오늘 날짜
today = datetime.date.today()

# weekday 구하기
dict = {0:'월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}
print('오늘날짜:', today.strftime('%Y-%m-%d'), '(', dict[today.weekday()], ')', sep='')
#dict2 = {1:'월요일', 2:'화요일', 3:'수요일', 4:'목요일', 5:'금요일', 6:'토요일', 7:'일요일'}
#print('오늘날짜2:', today.strftime('%Y-%m-%d'), '(', dict2[today.isoweekday()], ')', sep='')

# 이번주(월요일~일요일 중) 월요일 날짜 구하기
if today.weekday() == 0:
    monday = today
    print( '오늘은 월요일', monday, '입니다.' )
else:
    monday = today - datetime.timedelta(days=today.weekday())
    print( '이번주 월요일은', monday, '입니다.' )

today = (today + datetime.timedelta(days=1))
sunday = today + datetime.timedelta(days=6-today.weekday())
print( '테스트 오늘은', today, '입니다.')
print( '테스트 일요일은', sunday, '입니다.' )


dict3 = {0:'월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}
print(today.strftime('%Y-%m-%d'), '(', dict3[today.weekday()], ')', sep='')

sunday = today + datetime.timedelta(days=3+today.weekday())
print( '마지막', sunday, '입니다.' )

if today.weekday() < 3:
    sunday = today + datetime.timedelta(days=today.weekday())
    print( '1' )
elif today.weekday() > 3:
    sunday = today - datetime.timedelta(days=6+today.weekday())
    print( '2' )
else:
    sunday = today
    print( '3' )
    
