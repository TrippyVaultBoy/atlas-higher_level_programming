#!/usr/bin/python3

def common_elements(set_1, set_2):
    common = []
    for i in range(len(set_1)):
        for j in range(len(set_2)):
            if set_1[i] == set_2[j]:
                common.append(set_1[i])
    return common
