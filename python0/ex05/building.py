from sys import argv, stdin
import string


def count_chars(text: str):
	"""Printing the different types of chars in a string"""
	characters = sum(1 for c in text)
	uppercase = sum(1 for c in text if c.isupper())
	lowercase = sum(1 for c in text if c.islower())
	spaces = sum(1 for c in text if c.isspace())
	digits = sum(1 for c in text if c.isdigit())
	punctuation = sum(1 for c in text if c in string.punctuation)

	print(f'The text contains {characters} characters:')
	print(f'{uppercase} upper letters')
	print(f'{lowercase} lower letters')
	print(f'{punctuation} punctuation marks')
	print(f'{spaces} spaces')
	print(f'{digits} digits')


def main():
	"""The entry point of the programm"""
	assert len(argv) <= 2, "You provided more then one string"
	if (len(argv) == 2):
		count_chars(argv[1])
	else:
		repeat = True
		while (repeat):
			try:
				count_chars(stdin.read())
				repeat = False
			except (KeyboardInterrupt, EOFError):
				repeat = True


if __name__ == "__main__":
	main()
