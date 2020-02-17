import csv


theFile = './data.csv'
def changeThe(choose):
    studentName = input("Enter The Student Name: ")
    if choose == 'Name':
        with open('./data.csv' ,'r') as csv_file:
            reader = csv.reader(csv_file)
            line = list(reader)
            for array in line: 
                if studentName in array[0]:
                    newV = input("Enter New Name: ")
                    line[line.index(array)][0] = newV
                    print(array)
                    with open(theFile,'w') as csv_fole:
                        writer = csv.writer(csv_fole)
                        writer.writerows(line)
    elif choose == 'Age':
        with open('./data.csv' ,'r') as csv_file:
            reader = csv.reader(csv_file)
            line = list(reader)
            for array in line: 
                if studentName in array[0]:
                    newV = input("Enter New Age: ")
                    line[line.index(array)][1] = newV
                    print(array)  
                    with open(theFile,'w') as csv_fole:
                        writer = csv.writer(csv_fole)
                        writer.writerows(line)
    elif choose == 'ReportMark':
        with open('./data.csv' ,'r') as csv_file:
            reader = csv.reader(csv_file)
            line = list(reader)
            for array in line: 
                if studentName in array[0]:
                    newV = input("Enter New Mark: ")
                    line[line.index(array)][2] = newV
                    print(array)  
                    with open(theFile,'w') as csv_fole:
                        writer = csv.writer(csv_fole)
                        writer.writerows(line)
    elif choose == 'Grade':
        with open('./data.csv' ,'r') as csv_file:
            reader = csv.reader(csv_file)
            line = list(reader)
            for array in line: 
                if studentName in array[0]:
                    newV = input("Enter New Grade: ")
                    line[line.index(array)][3] = newV
                    print(array)  
                    with open(theFile,'w') as csv_fole:
                        writer = csv.writer(csv_fole)
                        writer.writerows(line)
    elif choose == 'Path':
        with open('./data.csv' ,'r') as csv_file:
            reader = csv.reader(csv_file)
            line = list(reader)
            for array in line: 
                if studentName in array[0]:
                    newV = input("Enter New Path: ")
                    line[line.index(array)][4] = newV
                    print(array)  
                    with open(theFile,'w') as csv_fole:
                        writer = csv.writer(csv_fole)
                        writer.writerows(line)
    else:
        print('The Name That You Just Entered is not exist')
