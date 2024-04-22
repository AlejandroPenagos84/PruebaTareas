from database.Conecction import get_connection
import json

CREATE_TASK_QUERY = """
    INSERT INTO Tasks (title, description, completed)
    VALUES (%s, %s, %s)
    RETURNING id;
"""
GET_TASK_QUERY = "SELECT * FROM tasks WHERE id = %s;"
GET_ALL_TASKS_QUERY = "SELECT * FROM tasks;"
DELETE_TASK = "DELETE FROM tasks WHERE id = %s"
UPDATE_TASK = """
    UPDATE tasks 
    SET title=%s, description=%s, completed=%s 
    WHERE id = %s 
    RETURNING id
"""

def defineData(response):
    data = {
        "id": response[0],
        "title": response[1],
        "description": response[2],
        "completed": response[3]
    }
    return data

#Agregar una tarea a la base de datos
def create_task(task):
    with get_connection() as con:
        with con.cursor() as cur:
            tupla = (task["title"], task["description"], task["completed"])
            cur.execute(CREATE_TASK_QUERY, tupla)
            new_id = cur.fetchone()[0]
            cur.execute(GET_TASK_QUERY, (new_id,))
            created_task = cur.fetchone()
        con.commit()
    return defineData(created_task)

#Obtener todas las tareas
def get_all_tasks():
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(GET_ALL_TASKS_QUERY)
            resultados = cur.fetchall()
        con.commit()
    tasks = []
    for task in resultados:
        tasks.append(defineData(task))
    return tasks

#Obtener una tarea en especifico
def get_task(id):
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(GET_TASK_QUERY, (id,))
            task = cur.fetchone()
        con.commit()
    return defineData(task)

#Eliminar una tara en especifico
def delete_task(id):
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(DELETE_TASK,(id,))
        con.commit()
    return True

#Actualizar una tarea
def update_task(id,task):
    with get_connection() as con:
        with con.cursor() as cur:
            tupla = (task["title"], task["description"], task["completed"],id)
            cur.execute(UPDATE_TASK,tupla)
            new_id = cur.fetchone()[0]
            cur.execute(GET_TASK_QUERY, (new_id,))
            updated_task = cur.fetchone()
        con.commit()
    return defineData(updated_task)
