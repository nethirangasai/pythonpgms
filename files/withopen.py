
with open('input.py') as f:
    print(f.tell())
    f.seek(10)
    print(f.tell())
    f.read()
    print(f.tell())
    # with open('writing1.txt','x+') as f2:
    #   print(f2.tell())
    #   #f2.write(f.read())
    #   #print(f2.tell())

