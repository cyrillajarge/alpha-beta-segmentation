# /usr/bin/python3

import helpers
import images

import numpy as np
import matplotlib.pyplot as plt


def main():
    test_image = images.test1
    #labeled_image = alpha_omegaCC(test_image, 2, 2)
    #colouredCCs = helpers.convert_to_color(labeled_image)
    #helpers.display_two(test_image, colouredCCs)

    print(helpers.get_neigbours(test_image, 4, 4))


'''
def alpha_omegaCC(image, alpha, omega):
    width = image.shape[0]
    height = image.shape[1]
    lbl = np.full((width, height), 0)
    rl = np.full((width, height), np.inf)

    lblval = 1
    for i in range(width):
        for j in range(height):
            if(lbl[i, j] == 0):
                lbl[i, j] = lblval
                mincc, maxcc = image[i, j]
                rlcrt = alpha
                neighbors = helpers.get_neighbours(image, i, j)
'''

if __name__ == "__main__":
    main()
