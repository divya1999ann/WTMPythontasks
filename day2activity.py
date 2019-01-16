#1
sum_numbers = lambda x : sum(x)

#2
import os
stmarks = {'name':'Divya',1:90,2:70,3:100,4:75,5:60}
marks = open('student.txt', 'w')
marks.write(str(stmarks))
marks.close()

#3
def switch(x):
  if (x=='1'):
    pass
  elif (x=='2'):
    pass
  else:
    pass
    
#5
def func(name,age,school):
    obj={'name':name,'age':age,'school':school}
    return obj
x=func('divya',20,'gbcs')
print(x)
