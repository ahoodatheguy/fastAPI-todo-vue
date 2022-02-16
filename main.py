from fastapi import FastAPI
from serializers import SQL, post_bodies
import json

app = FastAPI()
database = SQL.DataBase('tasks.sqlite3')


@app.get('/')
def task_index():
	'''Returns a list of dictionaries containing information about all tasks.'''
	return database.all_tasks()


@app.get('/view/{task_id}')
def get_task(task_id: int):
	'''Return data about a specific task'''
	return database.get_task(task_id=task_id)


@app.delete('/delete/{task_id}')
def delete_task(task_id: int):
	'''Delete specific task *(irreversible!)*'''
	database.delete_task(task_id=task_id)
	return database.all_tasks()


@app.post('/create-task')
def create_task(task: post_bodies.NewTask):
	'''Convert POST data into a new task'''
	json_tasks = json.loads(task.json())
	return database.create_task(task_data=json_tasks)


@app.put('/edit-task/{task_id}')
def edit_task(task_id: int, task: post_bodies.NewTask):
	'''Edit the data of a specific task.'''
	task_data = json.loads(task.json())
	return database.edit_task(task_id=task_id, task_data=task_data)
