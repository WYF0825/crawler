# import jieba
# import jieba.analyse
#
#
# f=open("E:/python数据/b站评论.txt","r",encoding="UTF-8")
# data=f.read()
# f.close()
# jieba.load_userdict('E:/python数据/自定义词典.txt')   # 导入自定义的词典
# words=jieba.lcut(data)
#
#
# dict1={}
# for word in words:
#     if len(word)==1:   # 单词长度为1的跳过
#         continue
#     else:
#         try:
#             dict1[word]=dict1[word]+1   # 字典的key不需要输入，只需要给value赋值即可
#         except KeyError:
#             dict1[word]=1
# ls=[]
# for key in dict1:
#     ls.append([key,dict1[key]])
# ls.sort(key=lambda x:x[1],reverse=True)   # 对二维数组指定元素进行排序
# print(ls)
# for i in range(0,10):
#     for j in range(0,2):
#         print(ls[i][j],end=" ")
#     print()     # 输出空来作为换行

# import matplotlib.pyplot as plt
#
# # 定义数据
# positive_proportion = 0.7727
# negative_proportion = 0.2272
#
# # 定义标签
# labels = ['Positive', 'Negative']
#
# # 定义占比
# sizes = [positive_proportion, negative_proportion]
#
# # 定义颜色
# colors = ['#ff9999','#66b3ff']
#
# # 绘制饼状图
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
#
# # 添加中心圆（可选）
# # 中心圆半径为0，即为一个空心圆，并添加白色边框，使之更美观
# # centre_circle = plt.Circle((0,0),0.70,fc='white',edgecolor='black')
# # fig = plt.gcf()
# # fig.gca().add_artist(centre_circle)
#
# # 设置图形标题
# plt.title('Emotion Proportion')
#
# # 显示图形
# plt.show()


"""
词云
"""

# 导包
# import requests
# import re
# from wordcloud import WordCloud
# import jieba
# from PIL import Image    # 对图片进行操作
# import numpy as np       # 把图片转换成数组
#
# # 获取源码
# url="https://api.bilibili.com/x/v2/reply/main?csrf=8c210c32620c05f3974b9ee52b3db94a&mode=3&oid=683586187&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&type=1"
# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
#     "Referer":"https://www.bilibili.com/video/BV1VS4y1w7zS/?spm_id_from=333.337.search-card.all.click&vd_source=5d9345d36cb27683986204c09e79a610",
#     "Cookie":"buvid3=76D2F9CB-512F-BB2F-AA25-22D65E8AE08333576infoc; b_nut=1685087433; i-wanna-go-back=-1; b_ut=7; b_lsid=BFD1036F3_1885709B643; bsource=search_baidu; _uuid=8EB28DF3-62F8-8B6A-C792-8557A104EC32934317infoc; FEED_LIVE_VERSION=V8; header_theme_version=undefined; home_feed_column=4; browser_resolution=1234-892; buvid_fp=518d8f40bcb8035e3002ca4fc26e19ef; SESSDATA=c88239c4%2C1700639476%2C49395%2A52; bili_jct=8c210c32620c05f3974b9ee52b3db94a; DedeUserID=474520936; DedeUserID__ckMd5=2f38c5f08dfc5f98; sid=6i1cuubc; nostalgia_conf=-1; CURRENT_FNVAL=4048; rpdid=0z9ZwfQlIo|Fazq3Dv|2SDm|3w1Q2seW; buvid4=D48235A3-F6E6-DCC1-1C73-24B7CF5545A034464-023052615-7XDfT9HnZ743D2Ddi6PU4pD26M8LkfU4/HB7Km++YmBOTPk8+Rvh6Q%3D%3D"
# }
# res=requests.get(url=url,headers=headers)
# # print(res.content.decode())
#
# # 解析
# messages=re.findall(r'"message":"(.*?)"',res.content.decode())[1:67]
#
# # 写入到本地
# f=open("E:/python数据/b站评论.txt","w",encoding="UTF-8")
# for i in messages:
#     f.write(i)
#     f.write("\n")
# f.close()
#
# f=open("E:/python数据/b站评论.txt","r",encoding="UTF-8")
# text=f.read()
# f.close()
# data=jieba.lcut(text)      # 剔除一些单词：doge、回复
# ls=[]
# for i in data:      # 去除一个词的单词
#     if len(i)==1 or i=='doge' or i=='回复':
#         continue
#     else:
#         ls.append(i)
# words=" ".join(ls)  # 以空格分隔词语
# print(words)
#
#
# # mask=np.array(Image.open("E:/python数据/五角星.jpg"))
# # print(type(Image.open("E:/心形.jpg")))  # <class 'PIL.JpegImagePlugin.JpegImageFile'>
# wc2=WordCloud(font_path="C:\Windows\Fonts\SIMLI.TTF")
# wc2.generate(words)
# wc2.to_file("b站评论词云.png")


import matplotlib.pyplot as plt

# 设置饼状图的标签和数值
labels = ['Positive', 'Negative']
sizes = [92.1, 7.9]

# 设置饼状图的颜色
colors = ['#9B59B6', '#00FFFF']

# 绘制饼状图
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

# 添加标题
plt.title('Emotion Proportion')

# 显示图像
plt.show()


# SST数据集
# import matplotlib.pyplot as plt
#
# # 设置饼状图的标签和数值
# labels = ['very Positive','Positive', 'Negative','very Negative']
# sizes = [18.2,55.4,21.7,4.7]
#
# # 设置饼状图的颜色
# colors = ['#FF0000','#FFA07A', '#888888','#333333']   #FFA07A
#
# # 绘制饼状图
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
#
# # 添加标题
# plt.title('Emotion Proportion')
#
# # 显示图像
# plt.show()