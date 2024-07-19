# env：python3.8（miniconda）
# 需求：搜狗搜索页面数据
import requests

# 1.指定url
url = 'https://www.sogou.com/'
# 2.发送请求
response = requests.get(url=url)
    # 以get方法发送请求
# 3.获取响应数据
page_text = response.text
    #text返回的是字符串形式的响应数据
print(page_text)
# 4.存储
with open('./SogouSearch.html','w',encoding='utf-8') as file:
    # file可以任意替换，这里的作用是封装
    file.write(page_text)
print("Seccessfully!")