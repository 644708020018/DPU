from employee import Employee

class EmpMKT(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name, salary)
        self.location = 'Bangkok'
        self.comision = 30
        self.department = 'Marketing'

    def add_location(self,location:str):
        self.location = location
    
    def add_comision(self,comision:int):
        self.comision = comision
        

    def emp_detail(self):
        super().emp_detail()
        print(f'location : {self.location}')
        print(f'comision : {self.comision} %')

    def mkt_salary(self):
        self._emp_selary()
