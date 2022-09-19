from pydantic import BaseModel

class Employee(BaseModel):
    emp_id:int 
    emp_name:str 
    Dept_name:str 
    email:str 
    passwrd:str 