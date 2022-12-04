import string
import pandas as pd

with open('./data/raw/data.txt') as f:
    lines = f.readlines()

with open('./data/raw/greetings.txt') as f:
    l = f.readlines()
    

greetings= []
order = []
size = []
thanks = []


# Getting text from txt file and saving to python list 
for i in lines:
    if i[0] == '1':
        text = i.split("\t", 1)[0]
        text = text.split('1', 1)[1].strip().replace('"', '')
        order.append(text)
    elif i[0] == '2':
        text = i.split("\t", 1)[0]
        text = text.split('2', 1)[1].strip().replace('"', '')
        size.append(text)

for i in l:
    if i[0] == '1':
        text = i.split("\t", 1)[0]
        text = text.split('1', 1)[1].strip().replace('"', '')
        greetings.append(text)

    if i[0] == '4':
        text = i.split("\t", 1)[0]
        text = text.split('4', 1)[1].strip().replace('"', '')
        thanks.append(text)

    


df = pd.DataFrame(columns=['text', 'label'])
df1 = pd.DataFrame(columns=['text', 'label'])



#Train dataset
for i in order[:1000]:
    series = pd.Series([i, 1],index=['text','label'])
    df = df.append(series, ignore_index=True)


for i in size[:1000]:
    series = pd.Series([i, 2],index=['text','label'])
    df = df.append(series, ignore_index=True)

for i in greetings[:1000]:
    series = pd.Series([i, 3],index=['text','label'])
    df = df.append(series, ignore_index=True)

for i in thanks[:1000]:
    series = pd.Series([i, 4],index=['text','label'])
    df = df.append(series, ignore_index=True)




# Test Dataset
for i in order[1000:1100]:
    series = pd.Series([i, 1],index=['text','label'])
    df1 = df1.append(series, ignore_index=True)

for i in size[1000:1100]:
    series = pd.Series([i, 2],index=['text','label'])
    df1 = df1.append(series, ignore_index=True)

for i in greetings[1000:1100]:
    series = pd.Series([i, 3],index=['text','label'])
    df1 = df1.append(series, ignore_index=True)

for i in thanks[1000:1100]:
    series = pd.Series([i, 4],index=['text','label'])
    df1 = df1.append(series, ignore_index=True)


df = df.sample(frac=1)
df1= df1.sample(frac=1)


df.to_csv('./data/processed/train.csv')
df1.to_csv('./data/processed/test.csv')

print(len(order))
print(len(size))
print(len(greetings))
print(len(thanks))

