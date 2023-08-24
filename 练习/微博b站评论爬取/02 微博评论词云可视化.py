
import jieba
import pandas as pd
import stylecloud

# 导入数据
df_wb=pd.read_csv("02 微博评论.csv")
def get_cut_words(content_series):
    # 提取关键词
    stop_words=[]
    with open('E:/python数据/stop_words.txt','r',encoding='utf-8') as f:
        lines=f.readlines()
        for line in lines:
            stop_words.append(line.strip())
    # 添加关键词
    my_words=['恭喜呀','666','震惊']
    for i in my_words:
        jieba.add_word(i)
    # 分词
    word_num=jieba.lcut(content_series.str.cat(sep='。'),cut_all=False)
    # 条件筛选
    word_num_selected=[i for i in word_num if i not in stop_words and len(i)>=1]
    return word_num_selected

text=get_cut_words(content_series=df_wb['message'])
print(text)
ls=[]
for i in text:
    if len(i)==1 or i=='doge' or i=='回复':
        continue
    else:
        ls.append(i)
ls=' '.join(ls)

stylecloud.gen_stylecloud(
    text=''.join(ls),
    collocations=False,
    font_path=r'C:\Windows\Fonts\SIMLI.TTF',
    icon_name='fas fa-heart',      # far fa-heart
    size=768,
    output_name='02 微博评论词云.png'
)
