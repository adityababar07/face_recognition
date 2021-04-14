# load the image that is to be detected
name_of_person = input("enter name of the person :-\t")

# mysql connection

def create_db_connection(host_name, user_name, password, database):
    try:
        global mysqldb
        mysqldb = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=password,
            db=database
        )
        print("Database connection succesfull.")
    except Error as err:
        print(f"Error :\t'{err}'")
    return create_db_connection


# def create_db(connection, query0):
#     cur = mysqldb.cursor()
#     try:
#         cur.execute(query0)
#         mysqldb.commit()
#         print("Database created successfully.")
#     except Error as err:
#         print(f"Error : '{err}")


def execute_query(connection, query1):
    global cursor
    cursor = mysqldb.cursor()
    try:
        cursor.execute(query1)
        mysqldb.commit()
        print("Table created successfully.")
    except Error as err:
        print(f"Error : '{err}")


def enterUser(id_of_stu):
    
    cursor.execute(
        f"SELECT name FROM opencv.face_data")
    row = cursor.fetchall()
    print(row)
    if name_of_person == "laura":
        query = f'''
            create database if not exists opencv;

            create table if not exists face_data(
                id int auto_increment primary key,
                name varchar(50) not null
            );

            insert into opencv.face_data (name) values('{name_of_person}');
            '''
        cursor = mysqldb.cursor()
        cursor.execute(query)
        mysqldb.commit()
        cursor.close()
cursor.execute(f"select id from opencv.face_data where name = '{name_of_person}';")
face_id = cursor.fetch()
print(face_id)