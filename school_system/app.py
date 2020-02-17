import csv
import json
import conk
import prog
###############################################
def readRow(item):
    with open('data.csv', 'r') as csv_reader:
        reader =  csv.reader(csv_reader)
        line = list(reader)
        for array in line:
            if item == 'Name':
                print(f'Name:{array[0]}')
            elif item == 'Age':
                print(f'Age:{array[1]}')
            elif item == 'ReportMark':
                print(f'ReportMark:{array[2]}')
            elif item == 'Grade':
                print(f'Grade:{array[3]}')
            elif item == 'Path':
                print(f'Path:{array[4]}')


if conk.Admin is True:
    print("""
    1)Register
    2)see the Students
    3)see the Mark
    4)see the names
    5)see the ages
    6)see the grades
    7)see the paths
    8)Change Student Data
    """)

    bool_c = input('Enter A number\n:')

#             Conditions Hi Guys             #
    if bool_c == '1':


    #Here We are Taking an input from the user()


        name = input('Enter Your Name: ')
        age = int(input('Enter Your Age: '))
        reportMark = float(input('Enter your ReportMark: '))
        grade = input('Enter Which Grade You are in: ')
        path = input('Enter Which Path You are in: ')


#Here We are Writeing Data to the csv File()

        with open('./data.csv' ,'a+') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([name,age,reportMark,grade,path])   
            

#Here we are showing The student data()


    elif bool_c == '2': 
        with open('data.csv', 'r') as csv_reader:
            reader =  csv.reader(csv_reader)
            line = list(reader)
            for array in line:
                print(f'Name:{array[0]}|Age:{array[1]}|Mark:{array[2]}|Grade:{array[3]}|Path:{array[4]}')
                



#Here We are Showing the Student Marks


    elif bool_c == '3': 
        readRow('ReportMark')


#Here We are Showing the Student Names



    elif bool_c == '4': 
        readRow('Name')


#Here We are Showing the Student Age



    elif bool_c == '5': 
        readRow('Age')


#Here We are Showing the Student Grade


    elif bool_c == '6': 
        readRow('Grade')

#Here We are Showing the Student Path


    elif bool_c == '7': 
        readRow('Path')
    


    elif bool_c == '8':
        print("""What Do You Want To Change
        1)Name
        2)Age
        3)ReportMark
        4)Grade
        5)Path""")
        bloody_c = input("Enter an Number:\n")
        if bloody_c == '1':
            prog.changeThe('Name')
        elif bloody_c == '2':
            prog.changeThe('Age')
        elif bloody_c == '3':
            prog.changeThe('ReportMark')
        elif bloody_c == '4':
            prog.changeThe('Grade')
        elif bloody_c == '5':
            prog.changeThe('Path')
            
#####################################
                

#####################################
    else:
        print('Please Enter one of The Numbers')


#####################################
#####################################
if conk.student is True:
    print("""
    1)see the Mark
    2)see the names
    3)see the ages
    4)see the grades
    5)see the paths
    """)

    bool_l = input('Enter A number\n:')

#             Conditions Hi Guys             #
    if bool_l == '1':

#Here We are Showing the Student Marks

        readRow('ReportMark')


#Here We are Showing the Student Names



    elif bool_l == '2': 
        readRow('Name')


#Here We are Showing the Student Age



    elif bool_l == '3': 
        readRow('Age')


#Here We are Showing the Student Grade


    elif bool_l == '4': 
        readRow('Grade')


#Here We are Showing the Student Path


    elif bool_l == '5': 
        readRow('Path')

#####################################
    
    else:
        print('Please Enter one of The Numbers')
            
