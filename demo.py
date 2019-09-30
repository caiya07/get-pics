# -*- coding:utf-8 -*-
import requests, re, random

def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    html = requests.get(url=url,headers=headers,timeout=10).text
    p = r'src="(http://.*?\.jpg)"'
    list = re.findall(p,html)
    return list

def download_img(img_url):
    filename = '{}.jpg'.format(random.randint(666666, 888888))
    img = requests.get(url=img_url).content
    with open(filename, 'wb') as f:
        f.write(img)

if __name__ == '__main__':
    url = 'http://www.16sucai.com/'
    html = get_html(url)
    i = 1
    for img_url in html:
        print('正在下载第：{} 张'.format(i))
        i = i + 1
        download_img(img_url)

    input('请按任意键退出...')

