import random
import pandas as pd

df = pd.read_excel('./menu.xlsx')

menu = list(df['menu'])
tag = list(df['tag'])
rate = list(df['rate'])
ban = {"카페", "커피", "베이커리", "디저트", "브런치", "포장마차"}
dic = {}
filtered = []

for i in range(0, len(menu)):
    tag_list = set(tag[i].split(","))
    if ban & tag_list == set():
        filtered.append(menu[i])

for i in range(0, 10):
    print(random.choice(filtered))
