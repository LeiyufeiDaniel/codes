for i in range(1,100,2):
    i = i+1
    print(i,'\n')
    result = str(i)
    with open('./passwd.txt','w',encoding='utf-8') as fp:
        fp.write(result)
