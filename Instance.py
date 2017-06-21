import datetime
class Employee:
    num_of_emp=0 #class variables
    def __init__(self, first, last, pay):
        self.fname=first   #instance variables
        self.lname=last
        self.salary=pay
        self.email=first+'.'+'last'+'@'+'company.com'
        Employee.num_of_emp+=1
    @property
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)

    @fullname.setter
    def fullname(self,name):
        self.fname, self.lname= name.split(' ')

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return (Employee(first,last,pay))

    @staticmethod   # if we do not use any class or instance variable then use static method
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True


class Developer(Employee): # inheritance
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog=prog_lang



class Manager(Employee):
    def __init__(self,first,last,pay,employee=None):
        super().__init__(first,last,pay)
        if employee is None:
            self.emp=[]
        else:
            self.emp=employee

    def add_emp(self,employee):
        if employee not in self.emp:
            self.emp.append(employee)

    def rem_emp(self,employee):
        if employee in self.emp:
            self.emp.remove(employee)

    def print(self):
        for emp in self.emp:
            print(emp.fullname)



if __name__ == '__main__':
    emp_1=Employee('Deepak','Haldar', '50000')
    emp_2=Employee('John', 'Cory', '60000')
    emp_3_str=  "John-Zoe-70000"
    emp_3=Employee.from_string(emp_3_str)
    dev_1=Developer('Matt','Hardy','90000','Python')
    mgr_1=Manager('Vince','McMahon','100000',[dev_1])
    mgr_1.add_emp(emp_1)
    mgr_1.rem_emp(emp_1)

    emp_1.fullname='John Cena'
    print("Number of Employees:", Employee.num_of_emp)
    print("Employee 1:",emp_1.fullname)
    print ("Employee 2:",emp_2.fullname)
    print("Employee 3:",emp_3.fullname)
    print("Developer 1:",dev_1.fullname)
    my_day=datetime.date(2017,6,10) #yy-mm-dd
    print("Is Working Day:",Employee.is_workday(my_day))
    print( dev_1.fullname,"skill:", dev_1.prog)
    mgr_1.print()

