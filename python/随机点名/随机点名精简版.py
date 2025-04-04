import random
import time

Name_List = ['Daniel','lei','fox','李花荣','杨瑞安']

r = random.choice(Name_List)
# 打印提示
print("输入1单个随机，2多个随机")
# 开始选择
choice = int(input("请选择模式："))
if choice == 1:
    # 单选
    print(r)
elif choice == 2:
    # 多选
    for i in range(1,10,1):
        name = random.choice(Name_List)
        print(name,'\n')
        time.sleep(0.5)

else:
    print("输入错误，请重新运行本程序！")