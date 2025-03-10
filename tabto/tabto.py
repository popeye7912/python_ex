# C:\lge\workspace_py\tryexcept\tabto\tabto.py
# py tabto.py a.txt b.txt v
import sys

src = sys.argv[1]
dst = sys.argv[2]
prm = sys.argv[3]

print("[ file1 : %s ] [ file2 : %s ] [option : %s]\n" % (src, dst, prm.upper))

f = open(src) # 파일 열기
tab_content = f.read() # 파일 줄단위로 읽기
f.close() # 파일 종료

print("<<origin tab content>>")
print(tab_content,"\n")

if prm.upper() == 'V':
    print("<<replace space content>>")
    space_content = tab_content.replace(" ", " "*2)
    f = open(dst, 'a')
    f.write(space_content+"\n")
    f = open(dst)
    replace_content = f.read()
    f.close()

    print(replace_content)