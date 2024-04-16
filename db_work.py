import sqlite3


def db_do(sql) -> None:

    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()


def user_register(name) -> None:
    command = f"""INSERT INTO tb_Usuários
    (Nome)
    VALUES({name})
    """
    db_do(command)


def event_register(date, user_id=1, title='Event', desc='Something will happens', tags='Other') -> None:
    command = f"""INSERT INTO tb_Eventos
    (User_id, Title, Desc, Tags, Date)
    VALUES({user_id}, {title}, {desc}, {tags}, {date})
    """
    db_do(command)


def delete_db(tb, id) -> None:
    command = f"DELETE FROM {tb} WHERE Id={id}"
    db_do(command)


def update_db(tb, col, new_value, id) -> None:
    command = f'UPDATE {tb}, SET {col}={new_value} WHERE Id={id}'
    db_do(command)


def select_db(tb, col=None, value=None) -> tuple:
    command = f'SELECT * FROM {tb}' 
    if not (col == None or value == None):
        command += f" WHERE {col} LIKE '%{value}%'"
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    cursor.execute()
    resul = cursor.fetchall()
    db.close()
    return resul

