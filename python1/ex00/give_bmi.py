import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """Calculates the bmi"""
    try:
        assert type(height) == list, "Func called with wrong types"
        assert type(weight) == list, "Func called with wrong types"
        assert len(height) == len(
            weight), "Weight and Height lists unequal lenght"

        npHeight = np.array(height)
        npWeight = np.array(weight)

        assert all(map(lambda npArr: np.issubdtype(npArr.dtype, np.number), [
                   npHeight, npWeight])), "Lists not numeric"

        npBmi = npWeight / (npHeight ** 2)

        return npBmi.tolist()
    except AssertionError as err:
        print(f'Assertion error {err.args}')


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Returns a mapped array of booleans"""
    try:
        assert type(bmi) == list, "Func called with wrong types"

        npBmi = np.array(bmi)

        assert np.issubdtype(npBmi.dtype, np.number)

        return (npBmi > limit).tolist()
    except AssertionError as err:
        print(f'Assertion error {err.args}')
