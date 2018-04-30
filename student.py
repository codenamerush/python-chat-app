class STUDENT:
	totstu = 0
	def __init__(self, rollno, name, age, totmarks):
		self.rollno = rollno
		self.name = name
		self.age = age
		self.totmarks = totmarks
		STUDENT.totstu += 1

	def display_count(self):
		print("Total students = %d" % STUDENT.totstu)

	def display_student(self):
		print("Roll no.: ", self.rollno, "Name: ", self.name, "Age: ", self.age, "Marks: ", self.totmarks)

	def __eq__(self,other):
		return((self.totmarks) == (other.totmarks))

stu1 = STUDENT(1, "Rush", 21, 100)
stu2 = STUDENT(2, "AaRush", 22, 10)
stu3 = STUDENT(3, "AaRushi", 23, 100)	

'''
if(stu1==stu2):
	stu1.display_student()
	stu2.display_student()
elif(stu1==stu3):
	stu1.display_student()
	stu3.display_student()
else:
	stu3.display_student()
	stu2.display_student()
'''


