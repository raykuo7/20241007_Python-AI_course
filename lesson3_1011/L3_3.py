import tools

print(tools.SAT)

p1 = tools.Person('ray' , 1000)
print(p1)


s1 =tools.Student('Lala',1502,30,40,90)
print(s1.name)
print(s1.age)
print(s1.english)
print(s1.math)
print(s1.chinese)
print(s1.total)
print(s1.average())

p3 = tools.get_person('asdf',22)
print(p3)
print('========')

s2 = tools.get_student(name='王xx',age=28)
print(s2)
print(s2.total)
print(s2.average())