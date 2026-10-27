from database import add_task, get_tasks


def test_database():
	add_task("Test", "Desc")
	tasks = get_tasks()
	assert len(tasks) > 0
