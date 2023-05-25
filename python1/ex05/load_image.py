import numpy as np
from PIL import Image


def ft_black_and_white(coloredImage: np.ndarray) -> np.ndarray:
    """Converts colored image into black and white.
    Takes a three dimensional array and return a two dimensional one."""

    assert isinstance(
        coloredImage, np.ndarray), "arg to ft_black_and_white is not np array"
    coloredImageCpy = 0.2989 * coloredImage[:, :, 0] + 0.5870 * \
        coloredImage[:, :, 1] + 0.1140 * coloredImage[:, :, 2]
    coloredImageCpy = coloredImageCpy.astype('uint8')
    return coloredImageCpy


def ft_slice(fullImage: np.ndarray) -> np.ndarray:
    """Slices the image to a subimage of size 400 * 400 px"""

    assert isinstance(fullImage, np.ndarray), "arg to ft_slice not np array"
    fullImage = fullImage[140:140+400, 440: 440+400]
    return fullImage


def ft_convert(path: str) -> np.ndarray:
    """Loads an image, and converts it to 3d array (columns, rows, rgb)"""

    assert isinstance(path, str), "path is not a string"
    img = Image.open(path)
    npArr = np.array(img)
    print(f'The shape of image is: {npArr.shape}')
    print(npArr)

    return npArr
