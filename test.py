import random
import pandas as pd

df = pd.read_excel('./menu.xlsx')

menu = list(df['menu'])
tag = list(df['tag'])
rate = list(df['rate'])
dic = {}
filtered = []

for i in range(0, len(menu)):
    if "카페" not in tag[i] and "커피" not in tag[i] and "베이커리" not in tag[i] and "디저트" not in tag[i]\
            and "브런치" not in tag[i] and "포장마차" not in tag[i]:
        filtered.append(menu[i])

print(random.choice(filtered))
