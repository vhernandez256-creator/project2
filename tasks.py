from database import add_task, get_tasks
from api import get_quote

def create_task(title, description):
	add_task(title, description)
	quote = get_quote()
	return f"Task created! Motivational quote: {quote}"

def list_tasks():
	return get_tasks()
