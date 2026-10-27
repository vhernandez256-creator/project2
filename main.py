from tasks import create_task, list_tasks
from database import init_db
from logger import setup_logger


def main():
	logger = setup_logger()
	init_db()

	print("Secure Task Manager")
	print("1. Add Task")
	print("2. View Tasks")

	choice = input("Choose an option: ")

	if choice == "1":
		title = input("Task title: ")
		description = input("Task description: ")
		result = create_task(title, description)
		logger.info(f"Created task: {title}")
		print(result)

	elif choice == "2":
		tasks = list_tasks()
		for task in tasks:
			print(task)


if __name__ == "__main__":
	main()
