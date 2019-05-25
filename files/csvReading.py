import csv
with open('students.csv','r+') as f:
    r=csv.reader(f)
    w = csv.writer(f)
    # print(type(r))
    data=list(r)
    for line in data:
        #print(line,'\t',end='')
        #print(line[0],line[1],line[2])
        if line[1]=='avi':
            #w.writerow([line[0],line[1],180.0])
            print('updated')


