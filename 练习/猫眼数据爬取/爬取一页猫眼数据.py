
"""
爬取一页猫眼数据
"""
import urllib.request
from lxml import etree
import csv

# 获取网页源代码
url='https://www.maoyan.com/films?showType=3&sortId=3&yearId=&offset=0'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
         'Cookie':'uuid_n_v=v1; uuid=302971A001A811EEB1C0EF0226805F3B9AFB3717082D4EAEA7A80B5F3EF74CE8; _csrf=a68112b205b7efbcca7ac9b1a2fce87202b0f4532d404c5039d9fb6b4c4cc956; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1685753239; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1887eb914b1c8-0c2e393af8100b-26031d51-1fa400-1887eb914b1c8; _lxsdk=302971A001A811EEB1C0EF0226805F3B9AFB3717082D4EAEA7A80B5F3EF74CE8; ci=223; recentCis=223; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1685753775; __mta=244258362.1685753238998.1685753771034.1685753775697.12; _lxsdk_s=1887eb914b2-2b7-be6-95a%7C%7C23',
         'Referer':'https://www.maoyan.com/films?showType=3&sortId=3&yearId=&offset=30',
         }
requests=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(requests)
content=response.read().decode('utf-8')
# print(content)

# 解析源代码

tree=etree.HTML(content)

# 电影名
ls1=tree.xpath("//div//dl[@class='movie-list']//a/text()")
# print(ls1)
name_Ls=[]
for i in ls1:
    if i[0]=='\n':
        continue
    else:
        name_Ls.append(i)
# print(len(name_Ls))
print(name_Ls)

# 评分
ls2=tree.xpath("//div//dl[@class='movie-list']//i/text()")
# print(ls2)
score_ls=[]
for i in range(0,len(ls2),2):  # 步长
    score_ls.append(ls2[i]+ls2[i+1])
print(score_ls)

# 链接
ls3=tree.xpath("//div/dl[@class='movie-list']//div/a/@href")
# print(ls3)
link_ls=[]
for i in range(0,len(ls3),3):
        link_ls.append("https://www.maoyan.com"+ls3[i])
print(link_ls)

ls4=[]
for i in range(len(link_ls)):
    url=link_ls[i]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Cookie': 'uuid_n_v=v1; uuid=302971A001A811EEB1C0EF0226805F3B9AFB3717082D4EAEA7A80B5F3EF74CE8; _csrf=a68112b205b7efbcca7ac9b1a2fce87202b0f4532d404c5039d9fb6b4c4cc956; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1685753239; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1887eb914b1c8-0c2e393af8100b-26031d51-1fa400-1887eb914b1c8; _lxsdk=302971A001A811EEB1C0EF0226805F3B9AFB3717082D4EAEA7A80B5F3EF74CE8; ci=223; recentCis=223; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1685753775; __mta=244258362.1685753238998.1685753771034.1685753775697.12; _lxsdk_s=1887eb914b2-2b7-be6-95a%7C%7C23',
        'Referer': 'https://www.maoyan.com/films?showType=3&sortId=3&yearId=&offset=30',
        }
    requests = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(requests)
    content = response.read().decode('utf-8')
    # print(content)
    tree = etree.HTML(content)
    ls4.append(tree.xpath('//div[@class="celebrity-group"]/ul/li/div/a[@class="name"]/text()'))
    print(ls4)

# 保存数据
# f=open('一页猫眼数据.csv', 'w', encoding='utf-8', newline='')    # utf-8-sig
# csv_writer=csv.writer(f)
# csv_writer.writerow(['name','score'])
# for i in range(len(name_Ls)):
#     name=name_Ls[i]
#     score=score_ls[i]
#     csv_writer.writerow([name,score])
