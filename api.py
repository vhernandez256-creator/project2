import requests


def get_quote():
	url = "https://api.quotable.io/random"
	response = requests.get(url, timeout=10)
	data = response.json()
	return data["content"]
