PROGRESS_LEN = 97


def ft_tqdm(lst: range) -> None:
	""" generator that corresponds to the list
		plus a loading bar to stdout"""
	totalLength = len(lst)
	for i, obj in enumerate(lst):
		percentage = (i + 1) / totalLength * 100
		if (percentage.is_integer()):
			percentage_str = f'{percentage: 3.0f}%'
		else:
			percentage_str = f'{percentage: 3.1f}%'
		fill = '=' * (int(((i + 1) / totalLength) * PROGRESS_LEN))
		if (len(fill) > 0):
			fill = fill[:-1] + '>'
		print(f'\r{percentage_str}|{fill: <{PROGRESS_LEN}s}| ',
				f'{i + 1}/{totalLength}',
				end="")
		yield obj
