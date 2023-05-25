from load_image import ft_black_and_white
import numpy as np
from PIL import Image


def save(array: np.ndarray, name: str) -> None:
    """Saves the array as img with name 'name' """
    img = Image.fromarray(array)
    img.save(name)


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Invertes the colors of the image"""
    copy = 255 - array[...]
    save(copy, 'inverted.jpg')


def ft_red(array: np.ndarray) -> np.ndarray:
    """Takes out blue and green colors"""
    copy = array.copy()
    copy[:, :, 1:] = 0
    save(copy, 'red.jpg')


def ft_green(array: np.ndarray) -> np.ndarray:
    """Takes out red and blue colors"""
    copy = array.copy()
    copy[:, :, 0] = 0
    copy[:, :, 2] = 0
    save(copy, 'green.jpg')


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Takes out red and green colors"""
    copy = array.copy()
    copy[:, :, :2] = 0
    save(copy, 'blue.jpg')


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Makes the image greyscale"""
    save(ft_black_and_white(array), 'grey.jpg')
