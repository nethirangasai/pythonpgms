import csv
with open('students.csv','w',newline='') as f:
    lines=csv.writer(f)
    lines.writerow(['RollNo','Name','Marks'])
    while 1:
        rollno=eval(input('Enter Employee RollNo:'))
        name = input('Enter Employee Name:')
        marks = float(input('Enter Employee Marks:'))
        lines.writerow([rollno,name,marks])
        option=input("do u want to enter one more employee details[yes/no]")
        if option=='no' :
            break