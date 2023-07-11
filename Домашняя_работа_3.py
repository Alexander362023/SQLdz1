import psycopg2


'''Обьект подключения'''
conn = psycopg2.connect(database='DS1', user='postgres', password='sfdr34wrtyiuyt')
'''Помогает выполнять запросы и получать ответы обратно от базы'''
with conn.cursor() as cur:
    def DS1():
        '''запрос SQL'''
        cur.execute(
            'CREATE TABLE if not exists Клиенты(id SERIAL PRIMARY KEY, \
            Имя VARCHAR(50) UNIQUE NOT null, \
            Фамилия VARCHAR(50) UNIQUE NOT null);')
    
        cur.execute(
            'CREATE TABLE if not exists email(id SERIAL PRIMARY KEY, \
            email VARCHAR(50) UNIQUE NOT null, \
            Клиенты integer references Клиенты(id));')
    
        cur.execute(
            'CREATE TABLE if not exists телефон(id SERIAL PRIMARY KEY, \
            телефон integer UNIQUE NOT null, \
            Клиенты integer references Клиенты(id));')

        conn.commit()
DS1()  
        # cur.close('')
'''закрывает подключение'''

conn.close()

def DS2():
        cur.execute(             
            'INSERT INTO Клиенты(Имя, Фамилия) VALUES('', '');')
        conn.commit()
DS2()

def DS3():
    cur.execute(             
        'INSERT INTO телефон(телефон) VALUES('');')
    conn.commit() 
DS3()

def DS4():
    cur.execute('UPDATE Клиенты SET Имя=%s, Фамилия=%s WHERE id=%s;', ('', '', id))
    cur.execute('SELECT * FROM Клиенты;')
    print(cur.fetchall())  # запрос данных автоматически зафиксирует изменения    
DS4()

