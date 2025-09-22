import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='Rosh003@#',
    database='company')


cur=conn.cursor()
#sql="create table emp(id int primary key,name varchar(20))"
#sql="insert into emp values(1,'Rosh')"
#sql="insert into emp values(2,'Josh')"
#sql="insert into emp values(3,'Mosh')"
#sql="insert into emp values(4,'Tosh')"
#sql="insert into emp values(5,'Roni')"
#sql="insert into emp values(6,'Rani')"
#sql="insert into emp values(7,'soma')"
#sql="insert into emp values(8,'Soni')"  

sql="select * from emp"
cur.execute(sql)
#row=cur.fetchall()#for printing all rows in a nested tuple format 
#row=cur.fetchone()#for printing one row in a tuple format
row=cur.fetchmany(3)#for printing specified number of rows in a nested tuple format
print(row)


#for i in row:
 #   print(i)

conn.commit()
conn.close()