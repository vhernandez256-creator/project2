import sqlite3


def init_db():
	conn = sqlite3.connect("tasks.db")
	cursor = conn.cursor()
	cursor.execute("""
		CREATE TABLE IF NOT EXISTS tasks (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			title TEXT NOT NULL,
			description TEXT,
			completed INTEGER DEFAULT 0
		)
	""")
	conn.commit()
	conn.close()


def add_task(title, description):
	conn = sqlite3.connect("tasks.db")
	cursor = conn.cursor()
	cursor.execute(
		"INSERT INTO tasks (title, description) VALUES (?, ?)",
		(title, description),
	)
	conn.commit()
	conn.close()


def get_tasks():
	conn = sqlite3.connect("tasks.db")
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM tasks")
	rows = cursor.fetchall()
	conn.close()
	return rows
