import pymysql.cursors

class Database:
    def __init__(self, host, user, password, database):
        self.connection = pymysql.connect(host=host, user=user, password=password, database=database, cursorclass=pymysql.cursors.DictCursor)

    def insert_user(self, login, password):
        cursor = self.connection.cursor()
        sql = "INSERT INTO user (email, password) VALUES (%s, %s)"
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (login, password))
            self.connection.commit()

    def select_user(self, login):
        cursor = self.connection.cursor()
        sql = "SELECT * FROM user WHERE email = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(sql, login)

    def insert_classes(self, place1, place2):
        cursor = self.connection.cursor()
        sql = 'INSERT INTO classes (place1, place2) VALUES (%s, %s)'
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (place1, place2))
            self.connection.commit()

    def select_classes(self):
        cursor = self.connection.cursor()
        sql = 'SELECT * FROM classes'
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            classes = cursor.fetchall()
            for row in classes:
                print(row)

'''connection = pymysql.connect(
    user='root',
    host='localhost',
    password='',
    database='academy',
    cursorclass=pymysql.cursors.DictCursor)

data = ("red 404", "21")

cursor = connection.cursor()

sql = ('INSERT INTO academy.classes(class_name, places) VALUES (%s, %s)')
with connection.cursor() as cursor:
    cursor.execute(sql)
    connection.commit()
result = cursor.fetchone()

cursor.close()
connection.close()
print(result)'''