from load_image import ft_black_and_white, ft_slice, ft_convert
import numpy as np
from PIL import Image


def main():
    """A programm that changes an image"""
    try:
        imageArr: np.ndarray = ft_convert('animal.jpeg')
        blackNwhiteArr: np.ndarray = ft_black_and_white(imageArr)
        imagePartArr: np.ndarray = ft_slice(blackNwhiteArr)

        transposedArr: np.ndarray = imagePartArr.T
        # height, width = imagePartArr.shape
        # transposedArr = np.zeros((height, width), dtype=imagePartArr.dtype)

        # for row in range(height):
        #     for pixel in range(width):
        #         transposedArr[row, pixel] = imagePartArr[pixel, row]
        transposedImg: Image = Image.fromarray(transposedArr)
        transposedImg.save('transposed_racoon.jpg')
    except (IOError, AssertionError, Exception) as err:
        print(err.args)
        return


if __name__ == '__main__':
    main()
