# /usr/bin/python3

import helpers
import images
import sys
import os

import numpy as np
import matplotlib.pyplot as plt
import queue as Q


class Datum(object):
    def __init__(self, prio, p):
        self.prio = prio
        self.p = p

    def __lt__(self, other):
        return self.prio < other.prio


def main():
    input_file = ""
    alpha = 1
    omega = 1
    if(len(sys.argv) == 1):
        print(
            "Usage: python alphatree.py [input_image](optional) [alpha] [omega]")
    elif(len(sys.argv) == 3):
        try:
            alpha = int(sys.argv[1])
            omega = int(sys.argv[2])
            print("Runnning program with default image and alpha=" +
                  str(alpha)+", omega="+str(omega)+".")
            input_file = "__test"
        except ValueError:
            sys.exit("Alpha and omega should be integers.")
    elif(len(sys.argv) == 4):
        try:
            alpha = int(sys.argv[2])
            omega = int(sys.argv[3])
            print("Runnning program with image: "+sys.argv[1]+" and alpha=" +
                  str(alpha)+", omega="+str(omega)+".")
            input_file = sys.argv[1]
        except ValueError:
            sys.exit("Alpha and omega should be integers.")
    else:
        print("Incorrect number of arguments.")
        print(
            "Usage: python alphatree.py [input_image](optional) [alpha] [omega]")
        sys.exit()

    input_image = None
    if(input_file == "__test"):
        input_image = images.test1
    else:
        try:
            input_image = plt.imread(input_file)
        except FileNotFoundError as fnf_error:
            sys.exit(fnf_error)

    # Keeping only one channel
    if(len(input_image.shape) == 3):
        input_image = input_image[:, :, 0]

    # Converting to [0,255] if necessary
    if(input_image[0][0] < 1):
        input_image = input_image * 255
        input_image = input_image.astype(int)

    # Converting to float
    input_image = input_image + 0.

    labeled_image = alpha_omega(input_image, alpha, omega)
    colouredCCs = helpers.convert_to_color(labeled_image)
    export_file_name = "./outputs/"+os.path.splitext(os.path.basename(input_file))[0] + \
        "_"+str(alpha)+"_"+str(omega)+"_CC.png"
    helpers.display_two(input_image, colouredCCs, export_file_name)


def alpha_omega(gray_image, alpha, omega):

    # Initialisation
    # first index = line (height), second index = column(width)
    height = gray_image.shape[0]
    width = gray_image.shape[1]

    lbl = np.full((height, width), 0)
    rl = np.full((height, width), np.inf)

    pq = Q.PriorityQueue()
    st = []

    lblval = 1
    rcrt = 0
    for i in range(height):
        for j in range(width):
            if lbl[i, j] == 0:
                lbl[i, j] = lblval
                mincc = maxcc = gray_image[i, j]
                rlcrt = alpha
                neighbours = helpers.get_neighbours(gray_image, i, j)
                for k in range(len(neighbours)):
                    neighbour_i = neighbours[k][0]
                    neighbour_j = neighbours[k][1]
                    rlval = helpers.computeR(
                        gray_image[i, j], gray_image[neighbour_i, neighbour_j])
                    if lbl[neighbour_i, neighbour_j] > 0:
                        if rlcrt >= rlval:
                            rlcrt = rlval - 1
                        continue
                    if rlval <= rlcrt:
                        rl[neighbour_i, neighbour_j] = rlval
                        pq.put(Datum(rlval, (neighbour_i, neighbour_j)))
                try:
                    tmp = pq.get(block=False)
                    rcrt = tmp.prio
                    pq.put(tmp)
                except Q.Empty:
                    pass
                while not pq.empty():
                    datum = pq.get()
                    if lbl[datum.p[0], datum.p[1]] > 0:
                        continue
                    if datum.prio > rcrt:
                        while len(st) > 0:
                            pixel = st.pop()
                            pixel_i = pixel[0]
                            pixel_j = pixel[1]
                            lbl[pixel_i, pixel_j] = lblval
                        rcrt = datum.prio
                        if lbl[datum.p[0], datum.p[1]] > 0:
                            continue
                    st.append(datum.p)
                    if gray_image[datum.p[0], datum.p[1]] < mincc:
                        mincc = gray_image[datum.p[0], datum.p[1]]
                    if gray_image[datum.p[0], datum.p[1]] > maxcc:
                        maxcc = gray_image[datum.p[0], datum.p[1]]
                    if (omega < (maxcc - mincc)) or (rcrt > rlcrt):
                        rl = helpers.set_values(rl, st, pq, np.inf)
                        pq.queue.clear()
                        st = []
                        break
                    datum_neighbors = helpers.get_neighbours(
                        gray_image, datum.p[0], datum.p[1])
                    for k in range(len(datum_neighbors)):
                        q = datum_neighbors[k]
                        rlval = abs(
                            gray_image[datum.p[0], datum.p[1]] - gray_image[q[0], q[1]])
                        if (lbl[q[0], q[1]] > 0) and (lbl[q[0], q[1]] != lblval) and (rlcrt >= rlval):
                            rlcrt = rlval
                            if rcrt >= rlcrt:
                                rl = helpers.set_values(rl, st, pq, np.inf)
                                pq.queue.clear()
                                st = []
                                break
                            continue
                        if (rlval > rlcrt) or (rlval >= rl[q[0], q[1]]):
                            continue
                        elif rlval < rl[q[0], q[1]]:
                            rl[q[0], q[1]] = rlval
                            pq.put(Datum(rlval, q))
                while len(st) > 0:
                    pixel = st.pop()
                    pixel_i = pixel[0]
                    pixel_j = pixel[1]
                    lbl[pixel_i, pixel_j] = lblval
                lblval = lblval+1
    return lbl


if __name__ == "__main__":
    main()
