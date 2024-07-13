import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


def lightness_method(img):
    gray_img = (np.max(img, axis=2) + np.min(img, axis=2)) / 2
    return gray_img


def average(img):
    gray_img = np.mean(img, axis=2)
    return gray_img


def luminosity(img):
    gray_img = 0.21 * img[:, :, 0] + 0.72 * img[:, :, 1] + 0.07 * img[:, :, 2]
    return gray_img


img = mpimg.imread('./img/dog.jpeg')
gray_img = luminosity(img)
print(gray_img[0, 0])
