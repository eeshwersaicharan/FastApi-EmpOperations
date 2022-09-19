from sqlalchemy.sql.sqltypes import Integer,String
from sqlalchemy import Table,Column
from config.db import meta


employees=Table(
        'employees',meta,
        Column('emp_id',Integer,primary_key=True),
        Column('emp_name', String(255)),
        Column('Dept_name',String(30)),
        Column('email',String(30)),
        Column('passwrd',String(30))  

)