"""
第一页：https://www.maoyan.com/films?showType=3&sortId=3&yearId=&offset=0
第二页：https://www.maoyan.com/films?showType=3&sortId=3&yearId=&offset=30
第三页：https://www.maoyan.com/films?showType=3&sortId=3&yearId=&offset=60

规律： ffset=(page-1)*30
"""
import urllib.request
import urllib.parse
from lxml import etree
import csv

f = open('多页猫眼数据.csv', 'w', encoding='utf-8', newline='')  # utf-8-sig
csv_writer = csv.writer(f)
csv_writer.writerow(['name', 'score'])

# 获取网页源代码
def create_request(page):
    base_url='https://www.maoyan.com/films?showType=3&sortId=3&yearId=&'
    data={'offset':(page-1)*30}
    data=urllib.parse.urlencode(data)
    url=base_url+data
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
             'Cookie':'uuid_n_v=v1; uuid=302971A001A811EEB1C0EF0226805F3B9AFB3717082D4EAEA7A80B5F3EF74CE8; _csrf=a68112b205b7efbcca7ac9b1a2fce87202b0f4532d404c5039d9fb6b4c4cc956; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1685753239; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1887eb914b1c8-0c2e393af8100b-26031d51-1fa400-1887eb914b1c8; _lxsdk=302971A001A811EEB1C0EF0226805F3B9AFB3717082D4EAEA7A80B5F3EF74CE8; ci=223; recentCis=223; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1685753775; __mta=244258362.1685753238998.1685753771034.1685753775697.12; _lxsdk_s=1887eb914b2-2b7-be6-95a%7C%7C23',
             'Referer':'https://www.maoyan.com/films?showType=3&sortId=3&yearId=&offset=30',
             }
    requests=urllib.request.Request(url=url,headers=headers)
    response=urllib.request.urlopen(requests)
    content=response.read().decode('utf-8')
    return content
# print(content)

# 解析源代码

# 电影名
def analysis(content):
    tree=etree.HTML(content)
    ls1=tree.xpath("//div//dl[@class='movie-list']//a/text()")
    # print(ls1)
    name_ls=[]
    for i in ls1:
        if i[0]=='\n':
            continue
        else:
            name_ls.append(i)
    print(name_ls)

    # 评分
    ls2=tree.xpath("//div//dl[@class='movie-list']//i/text()")
    # print(ls2)
    score_ls=[]
    for i in range(0,len(ls2),2):  # 步长
        score_ls.append(ls2[i]+ls2[i+1])
    print(score_ls)

    # 保存数据
    for i in range(len(name_ls)):
        name = name_ls[i]
        score = score_ls[i]
        csv_writer.writerow([name, score])


if __name__ == '__main__':
    start_page=int(input("请输入起始页码："))
    end_page=int(input("请输入终止页码："))
    for page in range(start_page,end_page+1):
        content=create_request(page)
        analysis(content)