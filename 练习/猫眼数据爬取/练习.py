
# 导包
import urllib.request
from lxml import etree

# 获取网页源代码
# url='https://www.maoyan.com/films/588362'
url='https://www.maoyan.com/films/1277939'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#          'Cookie':'__mta=244258362.1685753238998.1686228842638.1686229628294.24; uuid_n_v=v1; uuid=302971A001A811EEB1C0EF0226805F3B9AFB3717082D4EAEA7A80B5F3EF74CE8; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1887eb914b1c8-0c2e393af8100b-26031d51-1fa400-1887eb914b1c8; _lxsdk=302971A001A811EEB1C0EF0226805F3B9AFB3717082D4EAEA7A80B5F3EF74CE8; recentCis=223; _csrf=6df583b05bc172a8b1c5b3241b45253635fa26e763091fa0cf1957ab35f702b6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1685774944,1685801885,1685801969,1686228698; __mta=244258362.1685753238998.1685774972433.1686228699113.22; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1686229628; _lxsdk_s=1889b10048a-04e-726-c97%7C%7C7',
#          'Referer':'https://www.maoyan.com/films?showType=3&sortId=3&yearId=&offset=0',
#          }
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
         'Cookie':'__mta=244258362.1685753238998.1686279849766.1686279852169.34; uuid_n_v=v1; uuid=302971A001A811EEB1C0EF0226805F3B9AFB3717082D4EAEA7A80B5F3EF74CE8; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1887eb914b1c8-0c2e393af8100b-26031d51-1fa400-1887eb914b1c8; _lxsdk=302971A001A811EEB1C0EF0226805F3B9AFB3717082D4EAEA7A80B5F3EF74CE8; recentCis=223; _csrf=411820de352bb2537f5fd5bbe1248a15142ee4ef02b4d20da58c35d8929b75cf; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1685801885,1685801969,1686228698,1686277892; __mta=244258362.1685753238998.1686278303735.1686278394037.31; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1686279852; _lxsdk_s=1889dfea6d5-c3b-6ea-526%7C%7C23',
         'Referer':'https://www.maoyan.com/films?showType=3&sortId=3&yearId=&offset=0',
         }
requests=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(requests)
content=response.read().decode('utf-8')
# print(content)

# 解析网页源代码
tree = etree.HTML(content)
# ls=tree.xpath('//*[@id="app"]/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/ul/li[1]/div/a')
ls=tree.xpath('//div[@class="celebrity-group"]/ul/li/div/a[@class="name"]/text()')
print(ls)