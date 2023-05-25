import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Printing the shape, and returning first and last"""
    try:
        assert isinstance(family, list), "List is not a list"
        assert isinstance(start, int), "Number is not a number"
        assert isinstance(end, int), "Number is not a number"

        npFamily = np.array(family)
        print(f'My shape is : {npFamily.shape}')
        reshaped = npFamily[:end][start:]
        print(f'My new shape is : {reshaped.shape}')
        return reshaped.tolist()
    except AssertionError as err:
        print(f'{err.args}')
