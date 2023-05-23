from ft_filter import ft_filter


def main():
	""" A programm that filters some examples. """
	print(ft_filter(lambda obj: obj is None, [True, None, True]))
	print(ft_filter(None, [True, None, True]))


if __name__ == '__main__':
	main()
