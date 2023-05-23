from typing import Iterable, TypeVar

T = TypeVar('T')


def count_in_list(list: Iterable[T], obj: T) -> int:
	""" Counts how often obj occurs in list """
	return sum(1 for iobj in list if iobj == obj)
