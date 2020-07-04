from snownlp import SnowNLP

stopwords = [u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',
                u'通常',u'如果',u'我们',u'需要',u'/',u'n',u'\\',u'>']

#定义情感分析函数
def danmuSentiment(danmu):
    danmu = SnowNLP(danmu)
    sen = danmu.sentiments
    if sen <= 0.4:
        return 'negative'
    elif sen <= 0.6:
        return 'neutral'
    else:
        return 'positive'
    

with open('北区入海.txt','r', encoding = 'utf-8')as file:
    danmu = file.read()
    


d = SnowNLP(danmu)
#主题词
print(d.keywords(5))
print(d.sentiments)
#摘要
#print(d.summary(5))





