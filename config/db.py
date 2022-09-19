from sqlalchemy import create_engine, MetaData


engine=create_engine("mysql://root:seeshwar21@localhost/mytemp")
meta=MetaData()
# conn=mysql.connector.connect(host='localhost',
#                                          database='tempdb',
#                                          user='root',
#                                          password='Escp@38825')

conn=engine.connect()