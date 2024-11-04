from pypinyin import pinyin, lazy_pinyin, Style
import pickle
src=open(r'c:\Users\lenovo\desktop\3500.txt','r',encoding='utf-8')
s=src.read()
src.close()
pinmap={}
for c in s:
    pl=pinyin(c,style=Style.NORMAL,heteronym=True)[0]
    for p in pl:
        if pinmap.get(p)!=None:
            pinmap[p].append(c)
        else:
            pinmap[p]=list(c)

sav=open(r'pinmap1.bin','wb')
pickle.dump(pinmap,sav,protocol=4)
sav.close()
