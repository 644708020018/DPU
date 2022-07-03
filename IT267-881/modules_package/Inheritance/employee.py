from symtable import SymbolTableFactory
from unicodedata import name


class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self._salary = salary

    def emp_detail(self):
        print (f'id: {self.id}')
        print (f'name: {self.name}')

    def _emp_selary(self):
        print(f'salary: {self._salary}')

