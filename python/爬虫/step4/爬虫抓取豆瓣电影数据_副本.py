# env:Python3.8(miniconda)
# 需求：获取豆瓣电影排行榜
'''
url:https://movie.douban.com/j/chart/top_list?type=24&interval_id=100:90&action=&start=20&limit=20
?后面为参数
User-Agent:Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
检查>respones里[]为列表(json类型)
'''
import requests
import json

url = 'https://movie.douban.com/j/chart/top_list?'
# ?通常要保留
# 参数处理,params通常用于处理参数
params = {
    'type':'24',
    'interval_id':'100:90',
    'action':'',
    'start':'0',
    'limit':'20',
}
# UA伪装
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}
response = requests.get(url=url,params=params,headers=headers)
list_data = response.json()
fp = open('./豆瓣喜剧排行榜.json','w',encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)
print("Successfully!")