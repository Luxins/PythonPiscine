from typing import Callable, Iterable, Optional, TypeVar


T = TypeVar('T')


def ft_filter(predicate: Optional[Callable[[T], bool]],
			iterable: Iterable[T]) -> Iterable[T]:
	""" filter(function or None, iterable) --> filter object

	Return an iterator yielding those items of iterable for which function(item)
	is true. If function is None, return the items that are true. """

	if (predicate):
		return [obj for obj in iterable if predicate(obj)]
	else:
		return [obj for obj in iterable if obj]
