"""
词云的由来：
百度年度搜索的关键字，做成了词云
统计词语出现的频率

"""
from wordcloud import WordCloud
import csv
# 目前中文中最大的分词工具库  模糊  正常  精确
import jieba
# Pillow  图像处理库
from PIL import Image
import numpy as np

def readData():
#     容器
    contentList= []
    #  python中操作文件的语法  with as 上下文
    with open('video.csv','r',encoding='utf-8') as file:
        csvReader = csv.reader(file)
#         上面得到的是一个结果集合
        for item in csvReader:
            contentList.append(item)
    print(contentList)
    return contentList

# 读取文件的方法实现
def read_Data():
    contentList = []
#     只会读取用户给与了评分的评论
#     5⭐
    community = ['里洲小区','天奥经纬府邸','锦苑春天','恒茂城市花园','肖公庙','紫金城']
    with open('data_nc.csv','r',encoding='utf-8') as file:
        csvReader =csv.reader(file)
        for item in csvReader:
            if item[3] in community:
                contentList.append(item[2])
    print(contentList)
    return contentList

# 生成词云图
def get_wordcloud():
    comments = read_Data()
#     字符串形式的数据
    finalComment = ''
    for comment in comments:
        finalComment+=comment
    print(finalComment)
    # 分词
    finalComment = '|'.join(jieba.cut(finalComment))
    print(finalComment)
#     根据图片的形状  进行实现词云图
    img = np.array(Image.open('ci.jpg'))
    word = WordCloud(
    #     字体选择 本机的字体
        font_path='C://Windows/Fonts/msyhbd.ttc',
        background_color='white',
        # max_font_size=40,
        mask=img
    ).generate(finalComment)
    word.to_file('小区名称词云图.jpg')
if __name__ == '__main__':
    get_wordcloud()
