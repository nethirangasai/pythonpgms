from zipfile import *
f=ZipFile('filG:\python by durga\screenshots\fileses.zip','r',ZIP_STORED)
lines=f.namelist()
for name in lines:
    print('File Name is',name)
    print(name,':File contentent is')
    f=open(name,'r')
    print(f.read())
    print('*'*10)