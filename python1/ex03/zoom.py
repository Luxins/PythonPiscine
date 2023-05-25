import numpy as np
from PIL import Image


def ft_load_and_slice(path: str) -> np.ndarray:
    """Loads an image, and converts it to 3d array (columns, rows, rgb)"""
    try:
        assert isinstance(path, str), "path is not a string"
        img = Image.open(path)
        npArr = np.array(img)
        print(f'The shape of image is: {npArr.shape}')
        print(npArr)

        npArr = 0.2989 * npArr[:, :, 0] + 0.5870 * \
            npArr[:, :, 1] + 0.1140 * npArr[:, :, 2]
        npArr = npArr.astype('uint8')
        npArr = npArr[140:140+400, 440: 440+400]
        return npArr
    except (AssertionError, IOError):
        print('something went wrong')


def main():
    """Loads the racoon"""
    arr: np.ndarray = ft_load_and_slice('animal.jpeg')
    if (arr is not None):
        print(f'shape of my reshaped image: {arr.shape}')
        print(arr)
        img = Image.fromarray(arr)
        img.save('racoon.jpg')
    else:
        print('Something went wrong')


if __name__ == '__main__':
    main()
