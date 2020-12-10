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

    plt.show()


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
    width = image.shape[0]
    height = image.shape[1]
    if(i < 0 or i > width-1 or j < 0 or j > height-1):
        raise Exception(
            'index out of range')
    neighbors = []
    if(i > 0 and i < width-1 and j > 0 and j < height-1):
        neighbors.append([i, j+1])
        neighbors.append([i+1, j])
        neighbors.append([i, j-1])
        neighbors.append([i-1, j])
        return neighbors
    if(i == 0):
        if(j == 0):
            neighbors.append([i+1, j])
            neighbors.append([i, j+1])
        elif(j == height-1):
            neighbors.append([i+1, j])
            neighbors.append([i, j-1])
        else:
            neighbors.append([i, j+1])
            neighbors.append([i+1, j])
            neighbors.append([i, j-1])
        return neighbors
    if(i == width-1):
        if(j == 0):
            neighbors.append([i-1, j])
            neighbors.append([i, j+1])
        elif(j == height-1):
            neighbors.append([i-1, j])
            neighbors.append([i, j-1])
        else:
            neighbors.append([i, j+1])
            neighbors.append([i-1, j])
            neighbors.append([i, j-1])
        return neighbors
    else:
        if(j == 0):
            neighbors.append([i-1, j])
            neighbors.append([i+1, j])
            neighbors.append([i, j+1])
        else:
            neighbors.append([i-1, j])
            neighbors.append([i+1, j])
            neighbors.append([i, j-1])
        return neighbors


def computeR(val1, val2):
    return abs(val2-val1)


def set_values(image, stack, heap, value):
    for k in range(len(stack)):
        i = stack[k][0]
        j = stack[k][1]
        image[i, j] = value
    for k in range(len(heap)):
        i = heap[k].p[0]
        j = heap[k].p[1]
        image[i, j] = value
    return image
