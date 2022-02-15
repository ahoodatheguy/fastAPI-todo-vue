from fastapi import FastAPI
from serializers import SQL

app = FastAPI()
database = SQL.DataBase('tasks.sqlite3')


@app.get('/')
def task_index():
	'''Returns a list of dictionaries containing information about all tasks.'''
	return database.all_tasks()
