class EmployeeService:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(EmployeeService, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.employees = {}

    def add_employee(self, employee):
        self.employees[employee.employee_id] = employee

    def remove_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]

    def get_employee(self, employee_id):
        return self.employees.get(employee_id)