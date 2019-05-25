import os
name=input("enter file name:")
lines=words=chars=0
if os.path.isfile(name):
     with open(name,'r') as f:
        for line in f:
            lines=lines+1
            word=line.split()
            words=words+len(word)
            chars=chars+len(line)
        print(lines,words,chars)
else:
    print('file doesnot exists')



