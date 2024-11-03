import os
import re
fpath=input(r'路径：').strip('"')
fsuffix=input('原后缀名：')
lsuffix=input('后缀名改为：')
pattern=r'\.(?=[^.]*$)'
n=re.search(pattern,fpath)
num=n.start()
lpath=fpath[:num]+fpath[num:].replace(fsuffix,lsuffix)
os.rename(fpath,lpath)