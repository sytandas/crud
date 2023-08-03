import psycopg2 

#connection conn = psycopg2.connect("dbname=testdb user=postgres password=password")
conn=psycopg2.connect(
  database="mydb",
  user="sayantandas",
  host="/tmp/",
  password="123"
)
#creating a cursor object using the cursor() method - what communicate with db
cur = conn.cursor()

#executing an MYSQL function using the execute() method
cur.execute("SELECT version();")

record = cur.fetchone()
print("connected to- ", record,"\n")

cur.close()
conn.close()
print("Postgres connection is closed")

number = int(input("1.create, 2.read, 3.update, 4.delete/modify\nchoose:: "))

def create():
    return "create"

def read():
    return "read"

def update():
    return "update"

def delete():
    return "delete"

def default():
    return "choose right one"

switcher = {
        1: create,
        2: read,
        3: update,
        4: delete
        }

def selectFunction(num):
    return switcher.get(num, default)()

print(selectFunction(number))

