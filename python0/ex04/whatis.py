from sys import argv

if __name__ == "__main__":
	assert len(argv) == 2, "more then one argument are provided"
	assert isinstance(int(argv[1]), int), "argument is not an integer"
	if (int(argv[1]) % 2 == 0):
		print("I'm Even.")
	else:
		print("I'm Odd.")