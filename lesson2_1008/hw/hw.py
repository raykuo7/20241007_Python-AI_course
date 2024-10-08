import csv

with open('student.csv', encoding='utf-8') as file1:
    
    reader = csv.reader(file1)
    l1 = []
    for i in reader:
        l1.append(i)
    l2 = []
    for i in range(1,len(l1)):
        if l1[i][1] > 25:
            l2.append(l1[i])

with open('ageover25.csv', 'w',encoding='utf-8') as file:
    for i in l2:
        for j in i:
            file.write(j)
            file.write(',')
        file.write('\n')    
            