
class Employee:
    def __init__(self, name: str, employee_type: str, hour: float):
        self.name = name
        self.employee_type = employee_type
        self.hour = hour

    def calculatePay(self):
        if self.employee_type == "seller":
            return self.calculate_seller_payment()
        elif self.employee_type == "manager":
            return self.calculate_manager_payment()

    def calculate_seller_payment(self):
        return self.hour * 8.25

    def calculate_manager_payment(self):
        return self.hour * 8.25 * 1.3


seller_empl = Employee("Danilo", "seller", 40)
manager_empl = Employee("Deise", "manager", 50)

print("-"*20)
print(f"\nSalário de {seller_empl.name}: {seller_empl.calculatePay()}")
print(f"\nSalário de {manager_empl.name}: {manager_empl.calculatePay()}\n")
print("-"*20)