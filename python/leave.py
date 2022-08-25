class Leave:
   def _init_(self,Employeeid,Name,LeaveBalance):
        self.employeeid=Employeeid
        self.name=Name
        self.leavebalance=LeaveBalance
   def display(self):
        return self.employeeid,self.name,self.leavebalance
l1=Leave(22798,"Priya",20)
l2=l1.display()
print(l2)