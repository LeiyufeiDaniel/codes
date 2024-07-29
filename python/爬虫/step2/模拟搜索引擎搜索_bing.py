# env：python3.8（miniconda）
# 需求：使用并抓取搜索引擎搜索页面
import requests
import time
# 1.指定url
url = 'https://cn.bing.com/search'

Guanjianzi = input("请输入要搜索的关键字：")
# 处理动态url：封装到字典中
param = {
    'q' : Guanjianzi
}
# param是参数的意思
# UA伪装(应对反爬机制)
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}
# 发请求
response = requests.get(url=url, params=param,headers=headers)

# 获取响应数据
page_text = response.text

# 存储
FileName = Guanjianzi+'.html'
with open(FileName,'w',encoding='utf-8') as file:
    file.write(page_text)
print("###")
time.sleep(0.3)
print("######")
time.sleep(0.3)
print("Successfully!")