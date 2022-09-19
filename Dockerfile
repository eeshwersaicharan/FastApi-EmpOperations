FROM python:3.10.6-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip3 install fastapi uvicorn sqlalchemy 

COPY . .
COPY  . /main 
EXPOSE 8000

CMD [ "uvicorn","sqlalchemy","app.main:app","--host","0.0.0.0","--port","8000" ]
#CMD ["uvicorn", "main:app","--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
