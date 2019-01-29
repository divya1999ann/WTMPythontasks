#1
class circle:
	def__init__(self,rad):
		self.rad=rad
	def getarea(self):
		area=3.14*self.rad*self.rad
		printf("Area is ",area)
	def circum(self):
		cir=2*3.14*self.rad
		printf("Circumference is ",cir)
c=circle(int(input("Enter radius"))
c.getarea()
c.circum()

#2
class temp:
	def __init__(self,t):
		self.t=t
	def celfar(self):
		f=((self.t*9)/5)+32
		print("Celsius to farenheit ",f)
	def farcel(self):
		c=((self.t-32)*5)/9
		print("Farenheit to celsius ",c)
tp=temp(int(input("\nEnter temperature in celsius")
tp.celfar()
t2=temp(int(input("\nEnter temperature in farenhiet")
t2.farcel()

#3
class student:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def dispaly(self):
		print("\nName is "+self.name)
		print("\nAge is "+self.age)
	def setage(self):
		self.age=int(input("\nEnter age"))
	def setmarks(self):
		self.marks=float(input("\nEnter marks"))
		display()
n=input("\nEnter name")
m=int(input("\nEnter age"))
s1=student(n,m)
s1.setage()
s1.setmarks()
	    
#email task
import smtplib
content="hi hello there "
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('divya.kurien@gmail.com','divyamol')
mail.sendmail('divya.kurien@gmail.com','lisa.wst@gmail.com',content)
mail.close()	    
	    
	    
	    
	    

