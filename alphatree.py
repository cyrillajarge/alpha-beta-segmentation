# /usr/bin/python3

import helpers
import images

import numpy as np
import matplotlib.pyplot as plt
import heapq
import queue as Q


class Datum(object):
    def __init__(self, prio, p):
        self.prio = prio
        self.p = p

    def __lt__(self, other):
        return self.prio < other.prio


def main():
    test_image = images.test1
    labeled_image = alpha_omega(test_image, 2, 2)
    colouredCCs = helpers.convert_to_color(labeled_image)
    helpers.display_two(test_image, colouredCCs)


def alpha_omega(gray_image, alpha, omega):

    # Initialisation
    # first index = line (height), second index = column(width)
    height = gray_image.shape[0]
    width = gray_image.shape[1]

    lbl = np.full((height, width), 0)
    rl = np.full((height, width), np.inf)

    pq = Q.PriorityQueue()
    st = []

    # l. 1
    lblval = 1
    rcrt = 0
    # l. 2
    for i in range(height):
        for j in range(width):
            # l. 3
            if lbl[i, j] == 0:
                # l. 4
                lbl[i, j] = lblval
                # l. 5
                mincc = maxcc = gray_image[i, j]
                # l. 6
                rlcrt = alpha
                # l. 7
                neighbours = helpers.get_neighbours(gray_image, i, j)
                for k in range(len(neighbours)):
                    # l. 8
                    neighbour_i = neighbours[k][0]
                    neighbour_j = neighbours[k][1]
                    rlval = helpers.computeR(
                        gray_image[i, j], gray_image[neighbour_i, neighbour_j])
                    # l. 9
                    if lbl[neighbour_i, neighbour_j] > 0:
                        # l. 10
                        if rlcrt >= rlval:
                            # l. 11
                            rlcrt = rlval - 1
                        # l. 12 end if
                        # l. 13
                        continue
                    # l. 14 end if
                    # l. 15
                    if rlval < rlcrt:
                        # l. 16
                        rl[neighbour_i, neighbour_j] = rlval
                        # l. 17
                        pq.put(Datum(rlval, (neighbour_i, neighbour_j)))
                    # l 18. enf if
                # l. 19 endfor
                # l. 20
                try:
                    tmp = pq.get(block=False)
                    rcrt = tmp.prio
                    pq.put(tmp)
                except Q.Empty:
                    pass
                # rcrt = pq_get_highest_priority()
                # l. 21
                while not pq.empty():
                    # l. 22
                    datum = pq.get()
                    # datum = pq_retrieve()
                    # l. 23
                    if lbl[datum.p[0], datum.p[1]] > 0:
                        # l. 24
                        continue
                    # l. 25
                    # l. 26
                    if datum.prio > rcrt:
                        # l. 27
                        while len(st) > 0:
                            # l.28
                            pixel = st.pop()
                            pixel_i = pixel[0]
                            pixel_j = pixel[1]
                            lbl[pixel_i, pixel_j] = lblval
                        # l. 29 end while
                        # l. 30
                        rcrt = datum.prio
                        # l. 31
                        if lbl[datum.p[0], datum.p[1]] > 0:
                            # l. 32
                            continue
                        # l. 33 end if
                    # l. 34 end if
                    # l. 35
                    st.append(datum.p)
                    # l. 36
                    if gray_image[datum.p[0], datum.p[1]] < mincc:
                        # l. 37
                        mincc = gray_image[datum.p[0], datum.p[1]]
                    # l. 38 end if
                    # l. 39
                    if gray_image[datum.p[0], datum.p[1]] > maxcc:
                        # l. 40
                        maxcc = gray_image[datum.p[0], datum.p[1]]
                    # l. 41 end if
                    # l. 42
                    if (omega < (maxcc - mincc)) or (rcrt > rlcrt):
                        # l. 43
                        # retrieve pixels from priority queue and stack and reset them to infinity in rl
                        rl = helpers.set_values(rl, st, pq, np.inf)
                        pq.queue.clear()
                        st = []
                        # l. 44
                        break
                    # l. 45 end if
                    # l. 46
                    datum_neighbors = helpers.get_neighbours(
                        gray_image, datum.p[0], datum.p[1])
                    for k in range(len(datum_neighbors)):
                        q = datum_neighbors[k]
                        # l. 47
                        rlval = abs(
                            gray_image[datum.p[0], datum.p[1]] - gray_image[q[0], q[1]])
                        # l. 48
                        if (lbl[q[0], q[1]] > 0) and (lbl[q[0], q[1]] != lblval) and (rlcrt >= rlval):
                            # l. 49
                            rlcrt = rlval
                            # l. 50
                            if rcrt > rlcrt:
                                # l. 51
                                # retrieve pixels from priority queue and stack and reset them to infinity in rl
                                rl = helpers.set_values(rl, st, pq, np.inf)
                                pq.queue.clear()
                                st = []
                                # l. 52
                                break
                            # l. 53 end if
                            # l. 54
                            continue
                        # l. 55 end if
                        # l. 56
                        if (rlval > rlcrt) or (rlval >= rl[q[0], q[1]]):
                            # l. 57
                            continue
                        # l. 58
                        elif rlval < rl[q[0], q[1]]:
                            # l. 59
                            rl[q[0], q[1]] = rlval
                            # l. 60
                            pq.put(Datum(rlval, q))
                            # pq_insert(q at priority rlval)
                        # l. 61 end if
                    # l. 62 end for
                # l. 63 end while
                # l. 64
                while len(st) > 0:
                    # l. 65
                    pixel = st.pop()
                    pixel_i = pixel[0]
                    pixel_j = pixel[1]
                    lbl[pixel_i, pixel_j] = lblval
                # l. 66 end while
                # l. 67
                lblval = lblval+1
            # l. 68 end if
    # l. 69 end for
    return lbl


if __name__ == "__main__":
    main()
