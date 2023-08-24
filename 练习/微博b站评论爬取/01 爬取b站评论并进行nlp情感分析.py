
"""
爬取b站的评论并进行nlp情感分析
数据来源：b站：如果你不想结婚，一定要做到这3件事
"""

# 导包
import requests
import re
import xlwt
from snownlp import SnowNLP

# 获取源码
url="https://api.bilibili.com/x/v2/reply/main?csrf=8c210c32620c05f3974b9ee52b3db94a&mode=3&oid=683586187&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&type=1"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Referer":"https://www.bilibili.com/video/BV1VS4y1w7zS/?spm_id_from=333.337.search-card.all.click&vd_source=5d9345d36cb27683986204c09e79a610",
    "Cookie":"buvid3=76D2F9CB-512F-BB2F-AA25-22D65E8AE08333576infoc; b_nut=1685087433; i-wanna-go-back=-1; b_ut=7; b_lsid=BFD1036F3_1885709B643; bsource=search_baidu; _uuid=8EB28DF3-62F8-8B6A-C792-8557A104EC32934317infoc; FEED_LIVE_VERSION=V8; header_theme_version=undefined; home_feed_column=4; browser_resolution=1234-892; buvid_fp=518d8f40bcb8035e3002ca4fc26e19ef; SESSDATA=c88239c4%2C1700639476%2C49395%2A52; bili_jct=8c210c32620c05f3974b9ee52b3db94a; DedeUserID=474520936; DedeUserID__ckMd5=2f38c5f08dfc5f98; sid=6i1cuubc; nostalgia_conf=-1; CURRENT_FNVAL=4048; rpdid=0z9ZwfQlIo|Fazq3Dv|2SDm|3w1Q2seW; buvid4=D48235A3-F6E6-DCC1-1C73-24B7CF5545A034464-023052615-7XDfT9HnZ743D2Ddi6PU4pD26M8LkfU4/HB7Km++YmBOTPk8+Rvh6Q%3D%3D"
}
res=requests.get(url=url,headers=headers)
# print(res.content.decode())

# 解析
messages=re.findall(r'"message":"(.*?)"',res.content.decode())[1:67]  # 67
# print(messages)
uname=re.findall(r'"uname":"(.*?)"',res.content.decode())
# print(uname)
unames=[]
for i in uname:
    if i  not in unames:
        unames.append(i)
# print(unames)
print(len(messages),len(unames))

# 实例化表格
workbook=xlwt.Workbook(encoding="utf-8")
worksheet=workbook.add_sheet('sheet_01')
worksheet.write(0,0,'姓名')
worksheet.write(0,1,'评论')
worksheet.write(0,2,'情感得分')
worksheet.write(0,3,'分析结果')


# nlp分类，小于0.5为消极情绪，大于等于0.5为积极情绪
pos_count=0   # 积极情绪计数器
neg_count=0   # 消极情绪计数器
for i in range(len(messages)): # messages
    name = unames[i]
    message=messages[i]
    score=SnowNLP(message).sentiments
    if score<0.5:
        tag="消极"
        neg_count+=1
    else:
        tag="积极"
        pos_count+=1
    worksheet.write(i+1,0,name)
    worksheet.write(i+1,1,message)
    worksheet.write(i+1,2,score)
    worksheet.write(i+1,3,tag)
workbook.save('01 b站评论分析.xls')

# 分析占比
print(f"积极情绪占比：{pos_count/(pos_count+neg_count)}")
print(f"消极情绪占比：{neg_count/(pos_count+neg_count)}")