from fastapi import FastAPI
from routes.employee import employee
app=FastAPI()

app.include_router(employee)