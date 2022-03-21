import psycopg2

# connect postgres container
conn = psycopg2.connect(database="example_db", user = "admin", password = "password", host = "db-service", port = "5432")

def dbCreate():
    # create database when first run
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Users
        (id INT NOT NULL, firstName TEXT, lastName TEXT, eMail TEXT, gender TEXT, IP TEXT, userName TEXT, agent TEXT, country TEXT)""")
    conn.commit()
    conn.close()

def addUser(userInfo):
    # dict tags
    userId = userInfo['id']
    firstName = userInfo['first_name']
    lastName = userInfo['last_name']
    eMail = userInfo['email']
    gender = userInfo['gender']
    ip = userInfo['ip_adress']
    userName = userInfo['user_name']
    userAgent = userInfo['agent']
    country = userInfo['country']

    # save db
    cur = conn.cursor()
    cur.execute("INSERT INTO Users VALUES (?,?,?,?,?,?,?,?,?)",(userId,firstName,lastName,eMail,gender,ip,userName,userAgent,country))
    conn.commit()
    conn.close()

