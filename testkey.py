import os
import pickle
from random import choice as __choi
from pypinyin import pinyin as __piny
from pypinyin import lazy_pinyin as __lazypin
from pypinyin import Style as __sty

file_0_=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r'pinmap0.bin'),'rb')
pinyin_map_0=pickle.load(file_0_)
file_0_.close()
file_1_=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r'pinmap1.bin'),'rb')
pinyin_map_1=pickle.load(file_1_)
file_1_.close()
