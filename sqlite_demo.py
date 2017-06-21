import sqlite3
from Instance import Employee

class EmployeeDatabase:
    def insert(self,emp):
        with con:
            c.execute("""INSERT INTO employees VALUES(:first, :last, :pay)""",{'first':emp.fname, 'last':emp.lname, 'pay': emp.salary})

    def update(self,emp,salary):
        with con:
            c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""",
                  {'pay':salary, 'first': emp.fname,'last':emp.lname })

    def delete(self,emp):
        with con:
            c.execute("""DELETE FROM employees WHERE first= :first AND last= :last""", {'first':emp.fname,'last':emp.lname})
        Employee.num_of_emp-=1

    def get_emps(self,name):
        c.execute("""SELECT * FROM employees WHERE last= :last""",{'last':name})
        return c.fetchall()


    def data(self):
        c.execute("""SELECT * FROM employees""")
        return c.fetchall()

if __name__ == '__main__':
    con = sqlite3.connect(':memory:')  # to be used for testing. Creates a new database in memory at every run
    c = con.cursor()  # Creating cursor
    with con:
        c.execute(""" CREATE TABLE employees(
            first text,
            last text,
            pay real)""")
    emp_1= Employee('Deepak','Haldar','90000')
    emp_2= Employee('Matt', 'Hardy', '85000.95')
    emp_3= Employee('Jeff', 'Hardy', '100000')

    d=EmployeeDatabase()
    d.insert(emp_1)
    d.insert(emp_2)
    d.insert(emp_3)
    d.delete(emp_2)
    d.update(emp_1,'25')
    data=d.data()
    print(data)
    print("Number of Employees:",Employee.num_of_emp)
