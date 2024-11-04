import os
import pickle
import jieba
from random import choice as __choi
from pypinyin import pinyin as __piny
from pypinyin import lazy_pinyin as __lazypin
from pypinyin import Style as __sty
#from pypinyin import pinyin,lazy_pinyin,Style

file_0_=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r'pinmap0.bin'),'rb')
pinyin_map_0=pickle.load(file_0_)
file_0_.close()
file_1_=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r'pinmap1.bin'),'rb')
pinyin_map_1=pickle.load(file_1_)
file_1_.close()
jieba.setLogLevel(20)
jieba.cut('初始化')

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False
    
def is_chsen(sentence):
    '''判断是否存在汉语'''
    for c in sentence:
        if is_chinese(c):
            return True
    return False

def topinmap(hanyu,tone=True):
    '''
:param hanyu: 汉语句子
:param tone: 是否有声调,默认为True
:return: 每个字为键,可能拼音的列表为值的字典
    '''
    s=[i for i in hanyu if is_chinese(i)]
    return dict(zip(s,
                    __piny(s,
                    style=(__sty.TONE if tone else __sty.NORMAL),heteronym=True)))

def xieyin(sentence, pattern=0,accurate=False):
    '''
:param sentence: 原文
:param pattern: 0 or 1 默认为0, 0:限制声调 1:不限制声调
:param accurate: 是否根据分词更精确匹配,默认为False
:return: 随机谐音句子
    '''
    if sentence=='':
        raise Exception('Invalid Sentence')
    s=sentence
    ret=[]
    if pattern!=0 and pattern!=1:
        raise Exception('Invalid Pattern')
    if not accurate:
        for c in s:
            if not is_chinese(c):
                ret.append(c)
                continue;
            pin=__choi(__piny(c,style=(__sty.TONE if pattern==0 else __sty.NORMAL),heteronym=True)[0])
            charlist=(pinyin_map_0 if pattern==0 else pinyin_map_1).get(pin)
            if charlist==None:
                ret.append(c)
            else:
                ret.append(__choi(charlist)) 
    else:
        wordlist=jieba.cut(s)
        for word in wordlist:
            if not is_chsen(word):
                ret.append(word)
                continue
            pinyinlist=__piny(word,style=(__sty.TONE if pattern==0 else __sty.NORMAL))
            for sublist in pinyinlist:
                charlist=(pinyin_map_0 if pattern==0 else pinyin_map_1).get(sublist[0])
                if charlist==None:
                    raise Exception('Unknown pinyin')
                else:
                    ret.append(__choi(charlist))
    return ''.join(ret)
def main():
    print(
'''谐音句子生成 ver:0.0.2
又名"zjs黑话生成"
输入句子来进行谐音(黑话)生成
输入quit退出''')
    while True:
        s=input('>')
        if s=='':
            print('Invalid Sentence')
            continue
        elif s=='quit':
            break
        else:
            print(xieyin(s,accurate=True))
if __name__=='__main__':
    main()

