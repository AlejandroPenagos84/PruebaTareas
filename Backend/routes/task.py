from Models.Task import Task
from database import CRUD
from fastapi import APIRouter, HTTPException

task = APIRouter()

#Metodo para crear una tarea
@task.post('/api/tasks')
def save_task(task:Task):
    response = CRUD.create_task(task.dict())
    if response:
        return response
    raise HTTPException

#Metodo para obtener todas las tareas
@task.get('/api/tasks')
def get_all():
    response = CRUD.get_all_tasks()
    if response:
        return response
    raise HTTPException

#Metodo para obtener una tarea en especifico
@task.get('/api/tasks/{id}')
def get_task(id:str):
    task = CRUD.get_task(id)
    if task:
        return task
    raise HTTPException


#Metodo para eliminar una tarea
@task.delete('/api/tasks/{id}')
def delete_task(id:str):
    if CRUD.get_task(id) != "null":
        response = CRUD.delete_task(id)
        if response:
            return 'Eliminado correctamente'
    else:
        return 'No existe'
    raise HTTPException


#Metodo para modificar una tarea
@task.put('/api/tasks/{id}')
def update_task(id:str,task:Task):
    if CRUD.get_task(id) != "null":
        response = CRUD.update_task(id,task.dict())
        if response:
            return response
    else:
        return 'No existe'
    raise HTTPException