from abc import ABC, abstractmethod

MANAGER_EMPLOYEE = 1
SELLER_EMPLOYEE = 2


class Employee(ABC):

    def __init__(self, name: str, employee_type: int, hour: float):
        self.name = name
        self.employee_type = employee_type
        self.hour = hour

    @abstractmethod
    def calculate_pay(self):
        pass


class AdmManager(Employee):
    def calculate_pay(self):
        return self.hour * 8.25 * 1.3


class Seller(Employee):
    def calculate_pay(self):
        return self.hour * 8.25


class EmployeeFactory:
    @staticmethod
    def makeEmployee(employee) -> Employee:
        raise NotImplemented


class EmployeeFactoryImpl(EmployeeFactory):
    @staticmethod
    def makeEmployee(**employee) -> Employee:
        if employee["employee_type"] == SELLER_EMPLOYEE:
            return Seller(**employee)
        elif employee["employee_type"] == MANAGER_EMPLOYEE:
            return AdmManager(**employee)


seller_empl = EmployeeFactoryImpl.makeEmployee(name="Danilo", employee_type=SELLER_EMPLOYEE, hour=40)
manager_empl = EmployeeFactoryImpl.makeEmployee(name="Deise", employee_type=MANAGER_EMPLOYEE, hour=50)

print("-" * 20)
print(f"\nSalário de {seller_empl.name}: {seller_empl.calculate_pay()}")
print(f"\nSalário de {manager_empl.name}: {manager_empl.calculate_pay()}\n")
print("-" * 20)
