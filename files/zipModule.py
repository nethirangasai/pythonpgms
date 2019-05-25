from  zipfile import ZipFile,ZIP_DEFLATED
f=ZipFile('files.zip','w',ZIP_DEFLATED)
f.write('csvReading.py')
f.write('csvWriting.py')
f.write('students.csv')
f.close()