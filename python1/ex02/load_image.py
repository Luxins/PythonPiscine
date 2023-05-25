import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Loads an image, and converts it to 3d array (columns, rows, rgb)"""
    try:
        assert isinstance(path, str), "path is not a string"
        img = Image.open(path)
        npArr = np.array(img)
        print(f'The shape of image is: {npArr.shape}')

        return npArr
    except (AssertionError, IOError):
        print('something went wrong')
