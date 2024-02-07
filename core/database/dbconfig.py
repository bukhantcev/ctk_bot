import sqlite3



PATH = 'workers.db'
connect = sqlite3.connect(PATH)
cursor = connect.cursor()


# PROCEDURI

# СОЗДАНИЕ ТАБЛИЦЫ Работники
def create_table():
    cursor.execute('DROP TABLE IF EXISTS worker')
    cursor.execute('''CREATE TABLE IF NOT EXISTS worker (worker_id INTEGER PRIMARY KEY AUTOINCREMENT, family VARCHAR, name VARCHAR,
     name2 VARCHAR, date_rogdeniya VARCHAR, phone_number VARCHAR, tg_id INTEGER)''')
    connect.commit()


# ДОБАВИТЬ РЯДЫ
def add_new_worker(new_worker: tuple):
    cursor.execute('''INSERT INTO worker (worker_id, family, name, name2, date_rogdeniya, phone_number, tg_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                   new_worker)
    connect.commit()










# ИЗМЕНЕНИЕ КОМАНДЫ ПО id
def update_procedura(new_data: tuple):
    cursor.execute('''UPDATE proceduri SET command=? WHERE proceduri_id=?''', new_data)
    connect.commit()


# ПОЛУЧИТЬ ПРОЦЕДУРУ ПО ИМЕНИ
def find_procedura(proceduri_id: tuple):
    procedura = cursor.execute('''SELECT * FROM proceduri WHERE proceduri_id=?''', proceduri_id).fetchall()
    return procedura


def find_name_procedure(name: tuple):
    procedura = cursor.execute('''SELECT last_procedure FROM klients WHERE tg_id=?''', name).fetchall()
    return procedura


# ПОЛУЧИТЬ id ПРОЦЕДУРЫ ПО КОМАНДЕ
def find_idproceduri(command: tuple):
    id_proc = cursor.execute('''SELECT proceduri_id  FROM proceduri WHERE command=?''', command).fetchall()
    return id_proc


# УДАЛЕНИЕ ПРОЦЕДУРЫ ПО id

def delete_procedura(proceduri_id: tuple):
    cursor.execute('''DELETE FROM proceduri WHERE proceduri_id=?''', proceduri_id)
    connect.commit()


# ИЗМЕНЕНИЕ КОЛОНКИ ПО tg_id
def update_klient(new_data: tuple, column_name):
    cursor.execute(f'UPDATE klients SET {column_name}=? WHERE tg_id=?', new_data)
    connect.commit()


def update_photo_sertificate(new_data: tuple, column_name):
    cursor.execute(f'UPDATE photo_sertificate SET {column_name}=? WHERE photo_id=?', new_data)
    connect.commit()


# ДОБАВИТЬ ОПИСАНИЕ ПРОЦЕДУРЫ /add_description Описание$ id
def add_description(new_description: tuple):
    cursor.execute('''UPDATE proceduri SET uslugi=? WHERE proceduri_id=?''', new_description)
    connect.commit()


def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


def add_photo(new_foto: tuple):
    cursor.execute('''UPDATE proceduri SET foto=? WHERE proceduri_id=?''', new_foto)
    connect.commit()
