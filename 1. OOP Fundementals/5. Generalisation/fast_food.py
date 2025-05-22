class Employee:
    def __init__(self, name, employee_id, hourly_wage, shift_hours, enter, exit):
        self.name = name
        self.employee_id = employee_id
        self.hourly_wage = hourly_wage
        self.shift_hours = shift_hours
        self.enter = enter
        self.exit = exit

    def clock_in(self):
        print(f"{self.name} clock in at {self.enter} ")

    def clock_out(self):
        print(f"{self.name} Clock in at {self.exit}")

    def get_pay(self):
        
        return