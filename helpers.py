import numpy as np
import matplotlib.pyplot as plt
import random


def display(image):
    plt.imshow(image, cmap='gray')
    plt.show()


def display_two(image1, image2):
    plt.subplot(1, 2, 1)
    plt.imshow(image1, cmap='gray')
    plt.subplot(1, 2, 2)
    plt.imshow(image2, cmap='gray')

    #plt.show()
    plt.savefig("figure.png");


def convert_to_color(image):
    width = image.shape[0]
    height = image.shape[1]
    colored_image = np.zeros((width, height, 3))
    for i in range(width):
        for j in range(height):
            np.random.seed(image[i, j])
            colored_image[i, j] = np.random.rand(3)
    return colored_image


def get_neighbours(image, i, j):
    height = image.shape[0]
    width = image.shape[1]
    neigbours = []
    if((i+1) < height):
        neigbours.append([i+1, j])
    if((i-1) >= 0):
        neigbours.append([i-1, j])
    if((j+1) < width):
        neigbours.append([i, j+1])
    if((j-1) >= 0):
        neigbours.append([i, j-1])
    return neigbours


def computeR(val1, val2):
    return abs(val2-val1)


def set_values(image, stack, heap, value):
    for k in range(len(stack)):
        i = stack[k][0]
        j = stack[k][1]
        image[i, j] = value
    while not heap.empty():
        next_item = heap.get()
        i = next_item.p[0]
        j = next_item.p[1]
        image[i, j] = value

    return image
