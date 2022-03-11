import psycopg2

# connect postgres container
conn = psycopg2.connect(database="example_db", user = "admin", password = "password", host = "db-service", port = "5432")

def dbCreate():
    # create database when first run
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Users
        (userName TEXT NOT NULL, firstName TEXT, lastName TEXT, age INT)""")
    conn.commit()
    conn.close()

def addUser(userInfo):
    # dict tags
    userName = userInfo['userName']
    firstName = userInfo['firstName']
    lastName = userInfo['lastName']
    age = userInfo['age']

    # save db
    cur = conn.cursor()
    cur.execute("INSERT INTO Users VALUES (?,?,?,?)",(userName,firstName,lastName,age))
    conn.commit()
    conn.close()

