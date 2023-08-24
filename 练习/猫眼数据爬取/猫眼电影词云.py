
# 导包
import urllib.request
from lxml import etree
import jieba
from wordcloud import WordCloud
from PIL import Image    # 对图片进行操作
import numpy as np       # 把图片转换成数组

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

# 电影名
tree=etree.HTML(content)
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

# 将电影名用jieba分词
# jieba.load_userdict('E:/python数据/movie_dict.txt')
ls=['满江红', '流浪地球2', '熊出没·伴我"熊芯"', '无名', '深海', '铃芽之旅', '阿凡达：水之道', '保你平安', '人生路不熟', '长空之王']
for i in range(len(ls)):
    jieba.add_word(ls[i])
words = ' '.join(jieba.cut(' '.join(ls)))
# print(words)

# 生成词云
mask=np.array(Image.open("E:/python数据/五角星.jpg"))
# wc2=WordCloud(font_path="C:\Windows\Fonts\SIMLI.TTF",mask=mask)
wc = WordCloud(width=1000,height=700,background_color='white',font_path='msyh.ttc',mask=mask)
wc.generate(words)
wc.to_file('猫眼电影词云.png') # 保存词云图片


