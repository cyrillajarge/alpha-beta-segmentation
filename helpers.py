import numpy as np
import matplotlib.pyplot as plt


def display(image):
    plt.imshow(image, cmap='gray')
    plt.show()


def display_two(image1, image2):
    plt.subplot(1, 2, 1)
    plt.imshow(image1, cmap='gray')
    plt.subplot(1, 2, 2)
    plt.imshow(image2, cmap='gray')

    plt.show()
