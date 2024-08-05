import requests

url = 'https://music.163.com/#/playlist?id=2008935342'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'
}
response = requests.post(url=url,headers=headers)
page_text = response.json()
with open('./data.html','w',encoding='utf-8') as fp:
    fp.write(page_text)
    print("Successfully")