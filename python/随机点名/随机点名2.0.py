import random
import time

start = time.time()
NameList = open("./名单","r",encoding='utf-8')
Name = NameList.readlines()
result = random.choice(Name)
print(result)
end = time.time()
print("用时：",end-start)
