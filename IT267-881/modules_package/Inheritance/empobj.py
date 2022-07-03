from os import mkdir
from empIT import EmpIT
from empMKT import EmpMKT

mike = EmpIT('001','Nike',60000)
mike.add_skill('Python,JavaScript')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()



jess = EmpMKT('002','jess',45000)
jess.add_location('Chian Mai')
jess.add_comision(35)
jess.emp_detail()
jess.mkt_salary()