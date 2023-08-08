import pandas as pd
import os
print('-'*50)
print('*'*5+'毕业证书的出生日期转化为中文'+'*'*5)
print('-'*50)
while True:
    fname = input('请输入表格的文件全名:>')
    fname = fname.strip()
    if os.path.exists(fname):
        break
    else:
        print('输入的文件不存在')
        print('-'*50)
df = pd.read_excel(fname)
df['身份证件号'] = df['身份证件号'].str.strip()
df['年'] = df['身份证件号'].apply(lambda x:x[6:10])
df['月'] = df['身份证件号'].apply(lambda x:x[10:12])
df['日'] = df['身份证件号'].apply(lambda x:x[12:14])
def year(x):
    y = {'1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九','0':'0'}
    z =''
    for i in x:
        z +=  y[i]
    return z
month = {'01':'一','02':'二','03':'三','04':'四','05':'五','06':'六','07':'七','08':'八','09':'九','10':'十','11':'十一','12':'十二'}
day = {'01':'一','02':'二','03':'三','04':'四','05':'五','06':'六','07':'七','08':'八','09':'九','10':'十','11':'十一','12':'十二','13':'十三','14':'十四','15':'十五','16':'十六','17':'十七','18':'十八','19':'十九','20':'二十','21':'二十一','22':'二十二','23':'二十三','24':'二十四','25':'二十五','26':'二十六','27':'二十七','28':'二十八','29':'二十九','30':'三十','31':'三十一'}
df.loc[: ,'年'] = df['年'].apply(year)
df.loc[: ,'月'] = df['月'].map(month)
df.loc[: ,'日'] = df['日'].map(day)
df.to_excel('new_'+fname,index=False)
print('-'*50)
print('程序执行结束，新文件已产生')
print('-'*50)
os.system('pause')