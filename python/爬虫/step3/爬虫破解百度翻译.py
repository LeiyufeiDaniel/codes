# env：python3.8（miniconda）
# 需求：使用爬虫破解百度翻译
'''
分析：
    -阿贾克斯请求为XHR（在检查>XHR）
    -请求方式：post
    -·加密方法：post
    url:
        https://fanyi.baidu.com/sug
    User-Agent:
        Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0
'''
import requests
# 导入json模块
import json
post_url = 'https://fanyi.baidu.com/sug'
# UA伪装：
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}
word = input("请输入要翻译成中文的词：")
# post请求的参数处理
data = {
    'kw':word
}
response = requests.post(url=post_url,data=data,headers=headers)
# 获取响应数据，因为返回的是json对象，所以使用.json而不是.text
dir_obj = response.json()

# json持久化存储!!!
FileName = word + '.json'
fp = open(FileName,'w',encoding='utf-8')
json.dump(dir_obj,fp=fp,ensure_ascii=False)
# 有中文，所以不能使用ascii编码
print("Successfully!")