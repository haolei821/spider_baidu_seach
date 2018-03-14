
# coding: utf-8


import requests
from lxml import etree
import pandas as pd

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
#     'Cookie':'BAIDUID=709C927117FC02E5C47BCE95A4FF6D75:FG=1; BIDUPSID=709C927117FC02E5C47BCE95A4FF6D75; PSTM=1511700187; BDUSS=W9XYmJydDZ-cFBxSzI3R3RPSVRnOUpsfmFoNnVJajJqNUtUcnhwS0Z0WDZRMEphQVFBQUFBJCQAAAAAAAAAAAEAAABAsHlD0MTM-LvY0uRsbAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPq2Glr6thpad; BD_UPN=123353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; H_PS_PSSID=1431_21099_20719; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_CK_SAM=1; PSINO=1; sugstore=1; H_PS_645EC=41e0COCwSO9q1TT58IFN8hgmGhjO%2BOfKUzNwzf6w3ZuVJ62V3BYGim67Qh1JVCgaCQ1r; BDSVRTM=0; locale=zh',
    'Host':'www.baidu.com',
    'Upgrade-Insecure-Requests':1,
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
}

def get_html(word): # 获取网页源码
    url = 'https://www.baidu.com/s?wd=' + word
    response = requests.get(url, headers=headers).text
    return response
    
def parse_html(response): # 解析网页
    html = etree.HTML(response)
    tags = html.xpath('//div[@id="content_left"]/div')   #获取每个结果的div
#     print(tags)
    return tags

def get_content(tags):
    title = [''.join(tag.xpath('h3/a//text()')) for tag in tags]  #从结果中找到标题
    link = [','.join(tag.xpath('h3/a/@href')) for tag in tags]    # 从结果中找到链接
    result = {
        'title':title,
        'link':link
    }
    return result
    
def table(result):
    df = pd.DataFrame(result)
    return df

def main():
    word = input("输入要搜索的内容：")
    response = get_html(word)
    tags = parse_html(response)
    result = get_content(tags)
    df = table(result)
    print(df)
main()

