import csv

with open ('lesson2_1008\hw1\student.csv' , encoding='utf-8' , newline='') as file:
    reader = csv.reader(file)
    rdict = list(csv.DictReader(file))
    for i in rdict:
        print(i)
    l1 = []
    print('Age over 25')
    for i in rdict:
        if int(i['age']) > 25:
            print(i)
            l1.append(i)
    
with open('lesson2_1008\hw1\AgeOver25.csv','w',encoding='utf-8' , newline='') as file2:
    filenames = ['name' , 'age' , 'city']
    dict_writer = csv.DictWriter(file2,fieldnames=filenames)
    dict_writer.writeheader()
    for i in l1:
        dict_writer.writerow(i)
    