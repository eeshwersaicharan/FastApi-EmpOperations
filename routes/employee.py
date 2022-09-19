from fastapi import APIRouter
from config.db import conn
from models.employee import employees
from schemas.employee import Employee


employee=APIRouter()


@employee.get("/getallemployees")
# args:No arguments
# result:Returns All employees
async def get_all_employees():
    try:
        return conn.execute(employees.select()).fetchall()
    except:
        raise Exception("Error:No employee Available")


@employee.post("/addemployee")
async def add_employee(employee:Employee):
    # args: It takes the arguments of Employee model
    # Result: returns the all employees after adding an employee
    conn.execute(employees.insert().values(
        emp_id=employee.emp_id,
        emp_name=employee.emp_name,
        Dept_name=employee.Dept_name,
        email=employee.email,
        passwrd=employee.passwrd
    ))
    return conn.execute(employees.select()).fetchall()


@employee.get("/GetEmployeeById/{emp_id}")
#Args: emp_id:int
#Result: returns employee based on Id
async def get_employee_By_id(emp_id:int):
    try:
        return conn.execute(employees.select().where(employees.c.emp_id==emp_id)).fetchall()
    except:
        raise Exception("Error:Employee not Found Excepetion")

@employee.put("/UpdateEmployeeById")
async def update_employee_by_id(emp_id:int,employee:Employee):
    # args: It takes the arguments of emp_id and Employee mmodel
    # Result: returns the all employees after updating an employee
    try:
        conn.execute(employees.update(
            emp_name=employee.emp_name,
            Dept_name=employee.Dept_name,
            email=employee.email,
            passwrd=employee.passwrd
        ).where(employees.c.emp_id==emp_id))
        return conn.execute(employees.select()).fetchall()
    except:
       raise Exception("Error:Employee not found with Id given")

@employee.get("/employeeCountByDept/{Dept_name}")
async def employeeCountByDept(Dept_name:str):
    # args: It takes the arguments of Dept Name
    # Result: returns the count of employees belongs to same Dept
    try:
        employeeslist= conn.execute(employees.select().where(employees.c.Dept_name==Dept_name)).fetchall()
        return len(employeeslist)
    except:
        raise Exception("Error:DeptName is not available")

@employee.get("/findEmployeeByCondition/{empName}/{condition}")
async def findEmp(empName:str, condition:str) :
    #Args: Employee name :str and Condition :str
    #returns: List of filtered Employees details 
    try:
        empout=[]
        if condition=='startWith':
            employee=conn.execute(employees.select().where(employees.c.emp_name.startswith(empName))).fetchall()
            #employee=conn.execute(employees.select().where(employees.c.emp_name==empName).fetchall()
            empout=employee
        elif condition=='endsWith':
            employee=conn.execute(employees.select().where(employees.c.emp_name.endswith(empName))).fetchall()
            empout=employee

        elif condition=='Like':
            emps=conn.execute(employees.select()).fetchall()
            emps_dict = [record._mapping for record in emps]
            for emp in emps_dict:
                if (emp["emp_name"].__contains__(empName)):
                    empout.append(emp)

        elif condition=='Case Sensitive':
            employee=conn.execute(employees.select().where(employees.c.emp_name==empName)).fetchall()
            empout=employee

        elif condition=='Case InSensitive':
            emps=conn.execute(employees.select()).fetchall()
            emps_dict = [record._mapping for record in emps]
            for emp in emps_dict:
                if (emp["emp_name"].upper()==empName.upper()):
                    empout.append(emp)

        return empout
    except:
        raise Exception("Error:Employee not Found")