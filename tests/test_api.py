from api import get_quote


def test_get_quote():
	quote = get_quote()
	assert isinstance(quote, str)
