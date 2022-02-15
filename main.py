from fastapi import FastAPI
from serializers import SQL

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
