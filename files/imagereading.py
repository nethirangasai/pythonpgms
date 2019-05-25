import os
# if os.path.isfile('sai.JPEG'):
#     print('yes')

with open('G:/python by durga/python pgms/files/sai.jpeg','rb') as f:
    with open('rangasai.jpg','wb') as f1:
        f1.write(f.read())
    print('photo is succesfully copied')