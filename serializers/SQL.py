"""Manage data coming from SQL database."""
import sqlite3

from anyio import TASK_STATUS_IGNORED


class DataBase:
	def __init__(self, DATABASE_URL) -> None:
		self.conn = sqlite3.connect(DATABASE_URL, check_same_thread=False)
		self.curs = self.conn.cursor()

	def all_tasks(self) -> dict:
		self.curs.execute('SELECT * FROM tasks;')
		results = self.curs.fetchall()
		tasks = []
		for result in results:
			tasks.append(
				{
					'id': result[0],
					'name': result[1],
					'desc': result[2]
				}
			)
		return tasks

	def get_task(self, task_id: int) -> dict:
		self.curs.execute('SELECT * FROM TASKS WHERE id=?', (str(task_id)))
		result = self.curs.fetchone()
		serialized_result = {
			'id': result[0],
			'name': result[1],
			'desc': result[2]
		}
		return serialized_result

	def delete_task(self, task_id: int) -> dict:
		self.curs.execute('DELETE FROM TASKS WHERE id=?', (str(task_id)))
		self.conn.commit()
		return self.all_tasks()

	def create_task(self, task_data: dict) -> dict:
		self.curs.execute(
			'INSERT INTO tasks (name, desc) VALUES (?, ?);', (task_data['name'], task_data['desc']))
		self.conn.commit()
		return task_data
