import jieba
from collections import Counter
import matplotlib.pyplot as plt

txt = open('dan_.txt','r', encoding = 'utf-8').read() #设置要分析的文本路径

#增添一些校训等不希望被分割的词

jieba.suggest_freq('允公允能日新月异', tune=True)
jieba.suggest_freq('立德敬业博学敬先', tune=True)
jieba.suggest_freq('燕园', tune=True)
jieba.suggest_freq('海纳百川取则行远', tune=True)
jieba.suggest_freq('龙马担乾坤', tune=True)
jieba.suggest_freq('德以明理学以精工', tune=True)
jieba.suggest_freq('bit', tune=True)
jieba.suggest_freq('BIT', tune=True)
jieba.suggest_freq('深圳大学', tune=True)
jieba.suggest_freq('国防科技大学', tune=True)
jieba.suggest_freq('规格严格功夫到家', tune=True)
jieba.suggest_freq('哈工大', tune=True)
jieba.suggest_freq('自强不息厚德载物', tune=True)
jieba.suggest_freq('团结进取求实创新', tune=True)
jieba.suggest_freq('德才兼备', tune=True)
jieba.suggest_freq('中国传媒大学', tune=True)
jieba.suggest_freq('世界之光', tune=True)




seg_list = [x for x in jieba.cut(txt) if len(x)>=2]
lists=Counter(seg_list).most_common(10)
String_x=[]
Number_y=[]


for i in range(10):
    String_x.append(lists[i][0])
    Number_y.append(lists[i][1])

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['KaiTi']
# plt.rcParams['axes.unicode_minus'] = False

plt.figure('条形图')
plt.xlabel('高频词汇')
plt.ylabel('弹幕数量')
plt.title('《入海》北方高校版弹幕高频词汇')
plt.bar(String_x,Number_y)

plt.show()

    