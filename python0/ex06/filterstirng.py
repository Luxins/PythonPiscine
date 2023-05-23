from ft_filter import ft_filter
from sys import argv
from math import isnan


def main():
	""" A programm that filters the words of a string by their length. """

	assert len(argv) == 3, "Invalid number of arguments"
	numberOfChars = None
	try:
		numberOfChars = int(argv[2])
	except ValueError:
		assert False, "bad arguments"
	assert not isnan(numberOfChars), "Second argument is not a number"
	assert numberOfChars is not None and numberOfChars >= 0, \
		"Second argument may not be negative"

	print(ft_filter(lambda obj: len(obj) > numberOfChars,
		[word for word in argv[1].split()]))


if __name__ == '__main__':
	main()
