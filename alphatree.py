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

'''
def alpha_omega(gray_image,alpha,omega):
    
    #Initialisation
    width = gray_image.shape[0]
    height = gray_image.shape[1]

    lbl = np.full((width, height), 0)
    rl = np.full((width, height), np.inf)

    # l. 1
    lblval = 1;
    # l. 2
    for i in range(width):
        for j in range(height):
            # l. 3
            if lbl[i, j] == 0:
                # l. 4
                lbl[i, j] = lblval
                # l. 5
                mincc, maxcc = gray_image[i, j]
                # l. 6
                rlcrt = alpha
                # l. 7
                neighbors = helpers.get_neighbours(gray_image, i, j)
                for k in range(len(neighbors)):
                    # l. 8
                    rlval = 
                    # l. 9
                    if lbl[neighbors[i,0],neighbors[i,1]] > 0:
                        # l. 10
                        if rlcrt >= rlval:
                            # l. 11
                            rlcrt = rlval - 1
                        # l. 12 end if
                        # l. 13
                        continue
                    # l. 14 end if
                    # l. 15
                    if rlval < rlcrt :
                        # l. 16
                        rl[neighbors[i,0],neighbors[i,1]] = rlval
                        # l. 17
                        pq_insert(q at priority rlval)
                    # l 18. enf if
                # l. 19 endfor
                # l. 20
                rcrt = pq_get_highest_priority()
                # l. 21 
                while is_pq_empty() == False :
                    # l. 22
                    datum = pq_retrieve()
                    # l. 23
                    if lbl[datum.p] > 0 :
                        # l. 24
                        continue
                    # l. 25
                    # l. 26
                    if datum.prio > rcrt :
                        # l. 27
                        while len(stack) > 0:
                            # l.28
                            lbl[stack[0,0],stack[0,1]] = lblval
                            stack.pop(0)
                        # l. 29 end while
                        # l. 30
                        rcrt = datum.prio
                        # l. 31
                        if lbl[datum.p] > 0 :
                            # l. 32
                            continue
                        # l. 33 end if
                    # l. 34 end if
                    # l. 35
                    stack.append(datum.p);
                    # l. 36
                    if gray_image[datum.p] < mincc:
                        # l. 37
                        mincc = gray_image[datum.p]
                    # l. 38 end if
                    # l. 39
                    if gray_image[datum.p] > maxcc:
                        # l. 40
                        maxcc = gray_image[datum.p]
                    # l. 41 end if
                    # l. 42
                    if omega < (maxcc - mincc) or rcrt > rlcrt:
                        # l. 43
                        # retrieve pixels from priority queue stack and reset them to infinity in rl
                        # l. 44
                        break
                    # l. 45 end if
                    # l. 46
                    datum_neighbors = helpers.get_neighbours(gray_image, datum.p[0], datum.p[1])
                    for k in range(len(datum_neighbors)):
                        q = datum_neighbors[k]
                        # l. 47
                        rlval = abs(gray_image[datum.p] - gray_image[q])
                        # l. 48
                        if lbl[q] > 0 and lbl[q] != lblval and rlcrt >= rlval :
                            # l. 49
                            rlcrt = rlval
                            # l. 50
                            if rcrt > rlcrt
                                # l. 51
                                # retrieve pixels from priority queue stack and reset them to infinity in rl
                                # l. 52
                                break
                            # l. 53 end if
                            # l. 54
                            continue
                        # l. 55 end if
                        # l. 56
                        if rlval > rlcrt or rlval >= rl[q]:
                            # l. 57
                            continue
                        # l. 58
                        elif rlval < rl[q] :
                            # l. 59
                            rl[q] = rlval
                            # l. 60
                            pq_insert( q at priority rlval)
                        # l. 61 end if
                    # l. 62 end for
                # l. 63 end while
                # l. 64
                while len(stack) > 0:
                    # l. 65
                    lbl[stack[0,0],stack[0,1]] = lblval
                    stack.pop(0)
                # l. 66 end while
                # l. 67
                lblval = lblval+1
            # l. 68 end if
    # l. 69 end for
'''

if __name__ == "__main__":
    main()
