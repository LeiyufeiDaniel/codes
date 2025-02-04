import time
import sys

a = time.time()

sys.set_int_max_str_digits(999999999)

number = 123456 ** 54321

with open('result.txt','w',encoding='utf-8') as fp:
    fp.write(str(number))

b = time.time()

print(b-a)
print("StartTime:",a/60/60/60/60/60)
print("EndTime:",b)