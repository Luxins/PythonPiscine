from sys import argv


def main():
	""" A programm that converts a cli input into morse code,
	asserts if there are errors. """
	NESTED_MORSE = {
		" ": "/ ",
		"A": ".- ",
		"B": "-... ",
		"C": "-.-. ",
		"D": "-.. ",
		"E": ". ",
		"F": "..-. ",
		"G": "--. ",
		"H": ".... ",
		"I": ".. ",
		"J": ".--- ",
		"K": "-.- ",
		"L": ".-.. ",
		"M": "-- ",
		"N": "-. ",
		"O": "--- ",
		"P": ".--. ",
		"Q": "--.- ",
		"R": ".-. ",
		"S": "... ",
		"T": "- ",
		"U": "..- ",
		"V": "...- ",
		"W": ".-- ",
		"X": "-..- ",
		"Y": "-.-- ",
		"Z": "--.. ",
		"1": ".---- ",
		"2": "..--- ",
		"3": "...-- ",
		"4": "....- ",
		"5": "..... ",
		"6": "-.... ",
		"7": "--... ",
		"8": "---.. ",
		"9": "----. ",
		"0": "----- ",
	}

	assert len(argv) == 2, "the arguments are bad"
	upperArg = argv[1].upper()
	assert set(upperArg) - set(NESTED_MORSE.keys()) == set(), \
		"the arguments are bad"
	print(str().join(NESTED_MORSE[char] for char in upperArg))


if __name__ == '__main__':
	main()
