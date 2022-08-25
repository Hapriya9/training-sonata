class student :
    def __init__(self,student_name,student_id):
        self.id=student_id
        self.name=student_name
    def getstudent(self):
        return self,id_, self.name
st1=student(22798,"Haripriya")
display=st1.getstddet
print(display)
setattr(st1,'student_class',10)
print(getattr(st1,'student_class'))
delattr(st1,'name')
print(hasattr(st1,"student_name"))
st1=student(22798,"Haripriya")
display=st1.getstddet()
print(display)