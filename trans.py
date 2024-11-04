from pypinyin import pinyin, lazy_pinyin, Style
import pickle
from random import choice
file=open(r'pinmap.bin','rb')
pinmap=pickle.load(file)
file.close()
print('你哥黑话转换器 ver1.0')
while True:
    s=input('>')
    ret=[]
    pl=lazy_pinyin(s,style=Style.TONE)
    for p in pl:
        if pinmap.get(p)==None:
            ret.append(s[pl.index(p)])
        else:
            ret.append(choice(pinmap[p]))
    print(''.join(ret))
