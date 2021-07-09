import json

menu = open("C:/Users/masse/OneDrive - 한양대학교/바탕 화면/123.txt.", 'r', encoding='UTF8')
data = menu.read()

target = '''"name":'''
index = -1
while True:
    index = data.find(target, index + 1)
    if index == -1:
        break
    flag = 1
    dp = 0
    name = ''
    new = ''
    while True:
        new = data[index + 6 + flag]
        name += new
        flag += 1
        if new == '''"''':
            dp += 1
        if dp == 2:
            print(name)
            break