# env:python3.8(miniconda)
# 需求：爬取KFC餐厅位置并保存到本地
import requests

post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
# UA伪装：
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'
}

city = input("请输入要查询的城市:")
params = {
    'cname':city,
    'pid':"",
    'pageIndex':"1",
    'pageSize':"10",
}
response = requests.post(url=post_url,params=params,headers=headers)
data = response.text
FileName = city + '.html'
with open(FileName,'w',encoding='utf-8') as fp:
    fp.write(data)
    # wite什么？当然是data啦！
    print("successfully!")
