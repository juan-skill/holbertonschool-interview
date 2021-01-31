#!/usr/bin/python3
""" This is the lockboxes module """


def canUnlockAll(boxes):
    """  determines if all the boxes can be opened """

    setKeys = {0: 0}

    for i_th_box in range(len(boxes)):

        if setKeys.get(i_th_box) != i_th_box:
            return False

        box_n = boxes[i_th_box]

        for key in box_n:

            if key < len(boxes) and setKeys.get(key) != key:
                setKeys[key] = key

                for box in boxes[key]:

                    if box < len(boxes) and setKeys.get(box) != box:
                        setKeys[box] = box

    return True
