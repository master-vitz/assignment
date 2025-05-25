class restaurant:
    def __init__(self, name, menu, specialmeal,location):
        self.name=name
        self.menu=menu
        self.specialmeal=specialmeal
        self.location=location
    def __str__(self):
        return self.name + " restaurant offers "+ self.menu + " as menu and the special meal available is "+ self.specialmeal +  ". Its located in "+ self.location+"."
       
restaurant1=restaurant("Cj's","breakfast,lunch and dinner","dinner","nairobi")
restaurant2=restaurant("Art caffe","food and drinks","breakfast", "thika")

print(restaurant1)
print(restaurant2)

class marks:
    def __init__(self,subjectA,subjectB,subjectC,subjectD):
        self.subjectA=subjectA
        self.subjectB=subjectB
        self.subjectC=subjectC
        self.subjectD=subjectD
        self.totalmarks=(self.subjectA+self.subjectB+self.subjectC+self.subjectD)/4
student1=marks(50,70,47,60)
student2=marks(70,40,90,80)
print("total mark for student 1 is ", +student1.totalmarks)
print("total mark for student 2 is ", +student2.totalmarks)

class unit:
   def __init__(self,school,name,year,semester,studentstotal):
       self.school=school
       self.name=name
       self.year=year
       self.semester=semester
       self.studentstotal=studentstotal
unit1=unit("school of education","phsychology","year2","semester2","300")
unit2=unit("school of science and informatics","introduction to computer","year1","sem1","50")

print("unit1 undertaken by "+ unit1.school + " is " + unit1.name + "by "+ unit1.year+" "+unit1.semester+" students")