import pandas as pd

import numpy as np

class encoder():

    def __init__(self):

        self = []

    def oneHotEncode(self, y_to_enc):

        check_arr = []

        encode_val_arr = []

        return_arr = []

        for i in range(0, len(y_to_enc)):

            if (y_to_enc[i] in check_arr):

                return_arr.append(encode_val_arr[check_arr.index(y_to_enc[i])])

            else:

                check_arr.append(y_to_enc[i])

                one_hot = [0] * len(y_to_enc)

                one_hot[i] = 1

                encode_val_arr.append(one_hot)

                return_arr.append(one_hot)

        return return_arr

    def decode(self, array,strings):

        for number in array:

            if number > 0:

                return strings[array.index(number)]