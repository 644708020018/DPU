from employee import Employee

class EmpIT(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name, salary)
        self.skill = None
        self.experience = None
        self.department = 'IT'

    def add_skill(self,skill):
        self.skill = skill

    def add_experience(self,exp:str):
        self.experience = exp

    def emp_detail(self):
        return super().emp_detail()
        print(f'Skill: {self.skill}')
        print(f'Experience: {self.experience}')


    def it_salary(self):
        self._emp_selary()


