#!/usr/bin/env python
import matplotlib.pyplot as plt
import time as time
import numpy as np
import pandas as pd
import string
import random

def wills_permuts(s1, s2):
    def isPermutation(string1, string2):
        if len(string1) != len(string2):
            return False

        indicesDict = {}  # key: char; value: list of indices
        for i in range(0, len(string1)):
            if string1[i] not in indicesDict:
                index = string2.find(string1[i])
                if index == -1:
                    return False
                else:
                    indicesDict[string1[i]] = [index]
                    # indicesDict[string1[i]].append(index)
            else:
                lastIndex = indicesDict[string1[i]][-1]
                nextIndex = string2[lastIndex + 1:].find(string1[i])
                if nextIndex == -1:
                    return False
                else:
                    indicesDict[string1[i]].append(nextIndex)
        return True

    total = 0
    for i in range(0, len(s2) - len(s1) + 1):
        if isPermutation(s1, s2[i:i + len(s1)]):
            # print(i, " ")
            total += 1
    return total


def wens_permuts(s1, s2):
    def isPermutation(string1, string2):
        dict = {}
        for index in range(0, len(string1)):
            if string1[index] not in dict:
                dict[string1[index]] = 1
            else:
                dict[string1[index]] += 1
        for index in range(0, len(string2)):
            if string2[index] not in dict:
                return False
            else:
                dict[string2[index]] -= 1
        for key in dict.keys():
            if dict[key] != 0:
                return False
        return True

    total = 0
    for i in range(0, len(s2) - len(s1) + 1):
        if isPermutation(s1, s2[i:i + len(s1)]):
            # print(i, " ")
            total += 1
    return total


def tylers_permuts(s1, s2):
    # setup dictionary of s1
    s1dict = {}
    for index in range(0, len(s1)):
        if s1[index] not in s1dict:
            s1dict[s1[index]] = 1
        else:
            s1dict[s1[index]] += 1
    # setup dictionary of s2
    s2dict = {}
    for index in range(0, len(s1)):
        if s2[index] not in s2dict:
            s2dict[s2[index]] = 1
        else:
            s2dict[s2[index]] += 1
    # calculate total number of permutations of smaller string in bigger string
    total = 0
    if all(key in s2dict and s1dict[key] == s2dict[key] for key in s1dict.keys()):
        total += 1
    for i in range(1, len(s2) - len(s1) + 1):
        if s2dict[s2[i - 1]] > 0:
            s2dict[s2[i - 1]] -= 1
        else:
            del s2dict[s2[i - 1]]

        if s2[i + len(s1) - 1] in s2dict:
            s2dict[s2[i + len(s1) - 1]] += 1
        else:
            s2dict[s2[i + len(s1) - 1]] = 1

        if all(key in s2dict and s1dict[key] == s2dict[key] for key in s1dict.keys()):
            total += 1
    return total


def plot_permut_func_times(funcs, names, colors):
    abcd = "abcd"
    my_list = list(abcd)
    comparisons = []
    x_axis_nums = []
    max_x = 2000
    for i in range(50, max_x, 50):
        bigListOfStrings = []
        for k in range(0, i):# get a string of len i
            bigListOfStrings.append(abcd[random.randint(0, len(abcd) - 1)])
        x_axis_nums.append(i)
        comparisons.append("".join(bigListOfStrings))
    #x_axis_nums = [x for x in range(3, n + 1)]
    list_of_times = []  # list of lists for times of each function
    for i in range(len(funcs)):  # iterate through functions
        times = []
        for compStr in comparisons:
            before = time.time()
            funcs[i](abcd, compStr)
            after = time.time()
            difference = after - before
            times.append(difference)
        assert(len(x_axis_nums) == len(times))
        list_of_times.append(times)
    my_x = np.array(x_axis_nums)
    df = pd.DataFrame({
        "n": my_x
    })
    for index in range(len(funcs)):
        df[names[index]] = np.array(list_of_times[index])
    print(df.head())
    # scatterplots
    plt.xlabel("size of comparison string", fontsize=20)
    plt.ylabel("times", fontsize=20)
    plt.suptitle("times to solve number of permutations\nof smaller string in larger string", fontsize=20)
    max_y = 0
    for index in range(len(names)):  # cycle through names to graph func times
        max_y = max(max_y, max(df[names[index]]))
        plt.scatter(x="n", y=names[index], data=df, c=colors[index], marker="o", label=names[index])
    plt.legend(loc='upper left', fontsize="xx-large")
    plt.xlim([0, max_x])
    plt.ylim([0, max_y])
    plt.gca().grid(True)
    plt.show()
    plt.clf()

def test():
    abcd = "abcd"
    my_list = list(abcd)
    comparisons = []
    for i in range(50, 500, 50):
        bigListOfStrings = []
        for k in range(0, i):# get a string of len i
            bigListOfStrings.append(abcd[random.randint(0, len(abcd) - 1)])
        comparisons.append("".join(bigListOfStrings))
    for comparisonString in comparisons:
        print(len(comparisonString))
        will = wills_permuts(abcd, comparisonString)
        wen = wens_permuts(abcd, comparisonString)
        tyler = tylers_permuts(abcd, comparisonString)
        if not will == wen == tyler:
            print("not equal")


def main():
    str1 = "abbc"
    str2 = "bcababbcacabbaccbcbbcbbabcbacbcabbcbacbacbcbacbbcbcabacbacbacbacbcbaabbccbab"
    #test()
    plot_permut_func_times([wills_permuts, wens_permuts, tylers_permuts],
                           ["Will", "Wen", "Tyler"], ["r", "g", "b"])

if __name__ == "__main__":
    main()