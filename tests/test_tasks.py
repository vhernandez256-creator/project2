from tasks import create_task


def test_create_task():
	result = create_task("Test", "Description")
	assert "Task created!" in result
