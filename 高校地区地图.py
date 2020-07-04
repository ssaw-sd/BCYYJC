import jieba

with open('dan_.txt','r',encoding='UTF-8') as onefile:
    danmu = onefile.readlines()
#print(danmu)

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


content = ''
for i in danmu:
    content = content + i
segs=jieba.cut(content)
print(segs)

with open('停用词表.txt','r',encoding='UTF-8') as stopfile:
    stopwords_list = stopfile.readlines()
# print(stopwords_list)  
stopwords = []
for j in stopwords_list:
    stopwords.append(j.replace('\n',''))
# print(stopwords) 

# 用字典记录词频
segment = {}
for seg in segs:
    if seg not in stopwords:
        segment[seg] = segment.get(seg,0) + 1
print(segment)

segment['北京师范大学'] += segment['北师大']
#print(segment['北京师范大学'])
segment['哈尔滨工业大学'] += segment['哈工大']+  segment.get('规格严格功夫到家',0)+ segment['工大'] +segment['HIT']+segment['生日快乐']+segment['百年']
segment['中国海洋大学'] = segment.get('中国海洋大学',0)+segment['海大']+ segment['海纳百川取则行远']
segment['大连理工大学'] += segment['大工']+ segment['团结进取求实创新']
segment['清华大学'] += segment['清华']+ segment['自强不息']+segment['THU']+segment['厚德载物']
segment['北京大学'] += segment['北大']+segment['PKU']+segment['燕园']
segment['中央财经大学'] = segment.get('中国财经大学',0)+segment['央财']+segment['中财']+segment['龙马担乾坤']
segment['北京理工大学'] += segment['北理工']+ segment['bit']+segment['BIT']+segment['德以明理学以精工']
segment['南开大学'] += segment['南开']+ segment['允公允能日新月异']
segment['中国传媒大学'] = segment.get('中国传媒大学',0)+segment['中传']+ segment['传媒']+segment.get('立德敬业博学竞先',0)
segment['北京航空航天大学'] =  segment.get('中国航空航天大学',0)+segment['北航']+ segment.get('德才兼备',0)+ segment['知行合一']
segment['西安交通大学'] =  segment.get('西安交通大学',0)+segment['西交']+segment['世界之光']
segment['中国人民大学'] =  segment.get('中国人民大学',0)+segment['人大']

segment['北京'] += segment['中国传媒大学'] + segment['北京大学'] +segment['清华大学'] +segment['北京理工大学'] +segment['中央财经大学']+ segment['中国人民大学'] +segment['北京师范大学']
segment['黑龙江'] = segment['哈尔滨工业大学']
segment['山东'] = segment['中国海洋大学']
segment['辽宁'] =segment['大连理工大学']
segment['天津'] = segment['南开大学']
segment['陕西'] = segment['西安交通大学']

needwords =['黑龙江','北京','山东','辽宁','陕西','天津']
t=[]
for key,value in segment.items():
    if key in needwords:
        t.append((key,value))
t.sort(reverse=True)
top_name = t[:30]
print(top_name)


from pyecharts.charts import Map
from pyecharts import options as opts


school_map = Map()
school_map.add("",top_name,'china')
school_map.set_global_opts(visualmap_opts = opts.VisualMapOpts('',is_piecewise=True,
                                                               pieces=[{"min":0,"max":99,"color":"#ffefd7"},
                                                                       {"min":100,"max":999,"color":"#ffd2a0"},
                                                                       {"min":1000,"max":2999, "color":"#fe8664"},
                                                                       {"min":3000,"max":5999,"color":"#e64b47"},
                                                                       {"min":6000,"max":9999,"color":"#9c0a0d"}]),
                           title_opts = opts.TitleOpts(title="北方高校版《入海》弹幕高频高校所在地图"))

school_map.render()

