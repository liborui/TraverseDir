import os
import re

rootPath = "/Users/liborui/Desktop/EMNETS/0论文"

file_names = []

for root,dirs,files in os.walk(rootPath):
    for file in files:
        #获取文件所属目录
        # print(root)
        #获取文件路径
        # print(os.path.join(root,file))
        file_names.append(file)

words = []

for name in file_names:
    words += re.split(r"[\[\]\s]", name.replace("-",""))


print(words)

counter = {}
words_all = ""

for word in words:
    word = word.lower()
    words_all += word+" "
    if word not in counter:
        counter[word] = 0
    else:
        counter[word] += 1

counter_list = sorted(counter.items(), key=lambda x: x[1], reverse=True)

print(counter_list[:70])
#print(words_all)