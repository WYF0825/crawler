
"""
爬取微博评论
数据来源：微博：胡歌官宣
"""

# 导包
import requests
import urllib.parse
import csv

# 获取源码
# https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4863981833423714&is_show_bulletin=2&is_mix=0&count=10&uid=1223178222&fetch_level=0
# https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4863981833423714&is_show_bulletin=2&is_mix=0&max_id=3423244138589493&count=20&uid=1223178222&fetch_level=0
# https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4863981833423714&is_show_bulletin=2&is_mix=0&max_id=454287865745550&count=20&uid=1223178222&fetch_level=0
# https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4863981833423714&is_show_bulletin=2&is_mix=0&max_id=246067851243431&count=20&uid=1223178222&fetch_level=0

def get_content():
    # url="https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4863981833423714&is_show_bulletin=2&is_mix=0&count=10&uid=1223178222&fetch_level=0"
    base_url = "https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4863981833423714&is_show_bulletin=2&is_mix=0&"
    data = {
        "max_id":3423244138589493,
        "count":20,
        "uid":1223178222,
        "fetch_level":0
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    headers={
             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
             "Referer":"https://weibo.com/1223178222/MqQsvemFc",
             "Cookie":"UOR=www.baidu.com,app.weibo.com,www.baidu.com; SINAGLOBAL=6384736705990.839.1684313529588; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhukBvVXRoX_9Dy6SlN8r8p5NHD95Q0ehz0So.ce0qpWs4Dqcjci--ciKnRiK.ci--Ri-88i-zRi--ciK.Ri-8si--NiKLhiKLsi--NiKLWiKnXi--Xi-zRi-zc; ALF=1686906036; SUB=_2A25JYOgjDeRhGeVO6VEX-SjPzT2IHXVqqohrrDV8PUJbkNAGLVCgkW1NTTpOYTazlD_Bui5iJNTbYr8At49XEbBm; XSRF-TOKEN=54dP5RSATib7kASp8BYp8lJe; _s_tentry=weibo.com; Apache=8720697249840.51.1685102052085; ULV=1685102052145:3:3:2:8720697249840.51.1685102052085:1685089939947; WBPSESS=V7E6P3M3f5o-vdN1p1C915t1h8xdOJtp4Xo3DpHQdb_SiuP968OaNPQuraRrJPvvQRRvVIfQ5vQJ2lIEIiur0wME0RqMRZgwSx-y1ad9G9VMUt2-VIVTU_K1o1iPR90_YKuhGX_cCEJYW9_2TIvm3g=="
             }
    response=requests.get(url=url,headers=headers)
    # print(response.text)
    content=response.json()
    return content

# 解析数据
# 结构化数据：json数据，转成字典，使用字典取值 或 re。 非结构化数据：网页源代码，lxml，bs4，parsel，re  css/xpath/re
def analysis_data(content):
    data_list=content['data']
    # print(data_list)
    # max_id=content['max_id']
    name=[]
    message=[]
    for data in data_list:
        name.append(data['user']['screen_name'])
        message.append(data['text_raw'])
        # print(name,message)
    return name,message

# 保存数据
def writer_data(name_message):
    f = open('02 微博评论.csv', 'a', encoding='utf-8-sig', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(['name', 'message'])
    for i in name_message:
        csv_writer.writerow(i)

# 主函数
if __name__ == '__main__':
    content=get_content()
    # print(content)
    name,message=analysis_data(content)
    # print(name,message)
    name_message=[]
    for i in range(len(name)):
        name_message.append((name[i],message[i]))
    print(name_message)
    writer_data(name_message)
