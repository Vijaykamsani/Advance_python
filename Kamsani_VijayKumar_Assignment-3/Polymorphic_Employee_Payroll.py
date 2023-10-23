"""
homework-3
Problem -2
 vijay kumar Kamsani
"""

from abc import ABC, abstractmethod


# Class Employee declaring  the methods and properties that all employees should have
class Employee(ABC):
    def __init__(self, first_name, last_name, ssn):
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn

    @property
    def first_name(self):
        return f'{self._first_name}'

    @property
    def last_name(self):
        return f'{self._last_name}'

    @property
    def ssn(self):
        return f'{self._ssn}'

    @abstractmethod
    def earnings(self):
        pass

    def __str__(self):
        return self._first_name + " " + self._last_name + "\nsocial security number: " + self._ssn


# subclass of  a SalariedEmployee
class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, ssn, salary):
        super().__init__(first_name, last_name, ssn)
        if salary > 0:
            self._salary = salary
        else:
            raise ValueError("Salary must be greater than $0")

    @property
    def salary(self):
        return f'{self._salary}'

    @salary.setter
    def salary(self, salary):
        if salary > 0:
            self._salary = salary
        else:
            raise ValueError("Salary must be greater than $0")

    def earnings(self):
        return self._salary

    def __str__(self):
        return "SalariedEmployee: " + super().__str__() + "\nsalary: " + "{:.2f}".format(self._salary)


# Subclass of a HourlyEmployee
class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, ssn, hours, hourly_rate):
        super().__init__(first_name, last_name, ssn)
        if hours in range(1, 168):
            self._hours = hours
        else:
            raise ValueError("Hours must be greater than 0 and less than 168")
        if hourly_rate > 0:
            self._hourly_rate = hourly_rate
        else:
            raise ValueError("Hourly rate must be greater than 0.0")

    @property
    def hours(self):
        return f'{self._hours}'

    @hours.setter
    def hours(self, hours):
        if hours in range(1, 168):
            self._hours = hours
        else:
            raise ValueError("Hours must be greater than 0 and less than 168")

    @property
    def hourly_rate(self):
        return f'{self._hourly_rate}'

    #  hourly rate are in range (0-168) and is always non-negative.
    @hourly_rate.setter
    def hourly_rate(self, hourly_rate):
        if hourly_rate > 0:
            self._hourly_rate = hourly_rate
        else:
            raise ValueError("Hourly rate must be greater than 0.0")

    def earnings(self):
        earns = self._hours * self._hourly_rate
        if self._hours > 40:
            overtime_pay = earns * (1.5 * (self._hourly_rate / 100))
            earns = earns + overtime_pay
        return earns

    def __str__(self):
        return "HourlyEmployee: " + super().__str__() + "\nhours worked: " + str(
            self._hours) + "\nhourly rate: " + f'{self._hourly_rate:,.2f}'


# subclass of a  Commission Employee
class CommissionEmployee(Employee):
    def __init__(self, first_name, last_name, ssn, sales, commission_rate):
        super().__init__(first_name, last_name, ssn)
        if sales > 0:
            self._sales = sales
        else:
            raise ValueError("Sales must be greater than 0")
        if commission_rate in range(4, 6):
            self._commission_rate = commission_rate
        else:
            raise ValueError("Commission rate must be greater than 3.0 and less than 6.0")

    @property
    def sales(self):
        return f'{self._sales}'

    @sales.setter
    def sales(self, sales):
        if sales > 0:
            self._sales = sales
        else:
            raise ValueError("Sales must be greater than 0")

    @property
    def commission_rate(self):
        return f'{self._commission_rate}'

    # commission rates are in range (3%-6%) and the sales amounts property is always non-negative
    @commission_rate.setter
    def commission_rate(self, commission_rate):
        if commission_rate in range(4, 6):
            self._commission_rate = commission_rate
        else:
            raise ValueError("Commission rate must be greater than 3.0 and less than 6.0")

    def earnings(self):
        return self._sales * (self._commission_rate / 100)

    def __str__(self):
        return "CommissionEmployee: " + super().__str__() + "\ngross sales: " + "{:.2f}".format(
            self._sales) + "\ncommission rate: " + f'{self._commission_rate:,.2f}' + "%"


# main function to run the file

if __name__ == '__main__':
    try:
        e1 = HourlyEmployee('Donald', 'Trump', '123-00-0001', 100, 20)
        e2 = CommissionEmployee('Elon', 'Musk', '123-00-0003', 10000000, 5)
        e3 = SalariedEmployee('Taylor', 'Swift', '123-00-0005', 30000000)

        employee_list = [e1, e2, e3]

        for employee in employee_list:
            print(employee)
            print(f'earnings: ${employee.earnings():,.2f}')
            print()

    except ValueError as e:
        print(e)
