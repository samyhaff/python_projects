### EMPLOYEE ###

import datetime

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def applyraise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if (day.weekday == 5 or day.weekday == 6):
            return False
        return True

class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #paramètres de la classe Emplyee
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay) #paramètres de la classe Emplyee
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

emp_1 = Employee('Samy', 'Haffoudhi', 100000)
emp_2 = Employee('Marc', 'Partensky', 0)
emp_str_3 = "Paul-Vaugier-1000000000"
emp_3 = Employee.from_string(emp_str_3)
print(emp_1.fullname())
# parfaitement équivalent à Employee.fullname(emp_1)
emp_1.applyraise()
print(emp_3.first)
print(emp_1.pay)
date = datetime.date(2018, 1, 1)
print(Employee.is_workday(date))
dev_1 = Developer('Samy', 'Haffoudhi', 10000, 'Ocaml')
print(dev_1.prog_lang)
mgr_1 = Manager('Elon', 'Musk', '1000000000', [dev_1])
print(mgr_1.email)

### FRA&CTION ###

def pgcd(a,b):
	t = b
	b = a % b

	if b == 0:
		return t
	else:
		return gcd(t,b)

class Fraction:

    def __init__(self, num, den):
        common = pgcd(num, den)
        self.num = num #// common
        self.den = den #// common

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = pgcd(newnum,newden)
        return Fraction(newnum // common, newden // common)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = pgcd(newnum,newden)
        return Fraction(newnum // common, newden // common)

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.den
        common = pgcd(newnum, newden)
        return Fraction(newnum // comon, newden // common)

    def __floordiv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        common = pgcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __gt__(self, otherfraction):
        if self // otherfraction > 1:
            return True
        return False

    def __gt__(self, otherfraction):
        if self // otherfraction < 1:
            return True
        return False

frac = Fraction(2, 5)
frac.show()
