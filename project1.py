"""
This class handles the sorting and management of data in relation to the CSV file being passed in.
More specifically the data is being parsed with intention of solving for attributes and sorting/searching
based on these attributes.

Author: <Emanuel Tesfa>
Version: <Feb 4, 2022>
Email: <n01058529@unf.edu>
"""

import csv
import math
from States import *
from copy import deepcopy


# coding: utf-8


def quicksort(state, left, right):
    """
    This is an algorithim where names will be the attribute
    that will be sorted by coamparing each other. will pass
    in the lowest index and highest index so the method knows
    where to sort from. Called recursively and uses partition 
    function

    :param: state - object array with States data
    :param: left - the first index of the array to sort from
    :param: right - the last index of the array 
    :return null
    """
    if left < right:
        parIndex = partition(state, left, right)
        quicksort(state, left, parIndex - 1)
        quicksort(state, parIndex + 1, right)


def partition(state, left, right):
    """
    This is an function where a new partion point will
    be returned by passing in the same parameters as
    the recursive quick sort method

    :param: state - object array with States data
    :param: left - the first index of the array to sort from
    :param: right - the last index of the array 
    :return count + 1
    """

    count = (left - 1)
    pivot = state[right]
    for j in range(left, right):
        if state[j].get_state() < pivot.get_state():
            count += 1
            state[count], state[j] = state[j], state[count]
    state[count + 1], state[right] = state[right], state[count + 1]
    return count + 1


def mergesort2(stateArr, attribute):
    """
    This is an algorithim where based on userInput
    can sort based on any attribute of the States 
    class. It does not return anything but sorts
    the passed in array. Attribute will be passed 
    in as a string to be passed into getattr().

    :param: stateArr - object array with States data
    :param: attribute - the string of what will be found
    :return null

    """
    if len(stateArr) > 1:
        mid = len(stateArr) // 2
        leftside = stateArr[:mid]
        rightside = stateArr[mid:]

        mergesort2(leftside, attribute)
        mergesort2(rightside, attribute)
        a = b = c = 0

        while a < len(leftside) and b < len(rightside):
            # if lefthalf[a].temp < righthalf[b].temp:
            if getattr(leftside[a], attribute) < getattr(rightside[b], attribute):
                stateArr[c] = leftside[a]
                a += 1
            else:
                stateArr[c] = rightside[b]
                b += 1
            c += 1
        while a < len(leftside):
            stateArr[c] = leftside[a]
            a += 1
            c += 1
        while b < len(rightside):
            stateArr[c] = rightside[b]
            b += 1
            c += 1


def binarysearch(stateArray, userInput):
    """
    This is an algorithim where the stateArray 
    object will be searched only when the array
    has been sorted by name

    :param: stateArray - object array with States data
    :param: userInput - what is being searched for as 
        a .get_state() attribute attached to it 
    :return mid if the location is found
    :return -1 if not found

    """
    leftS = 0
    rightS = len(stateArray) - 1
    while leftS <= rightS:
        mid = (leftS + rightS) // 2
        if stateArray[mid].get_state().lower() == userInput.lower():
            return mid
        elif userInput.lower() < stateArray[mid].get_state().lower():
            rightS = mid - 1
        elif userInput.lower() > stateArray[mid].get_state().lower():
            leftS = mid + 1
    return -1


def seqsearch(arr, x):
    """
    Simple algorithim where iterates through each index 
    of array to find index where the x is found

    :param: arr - object array with States data
    :param: x - the first index of the array to sort from
    :return count if found 

    """
    s = 0
    count = 0
    r = len(arr) - 1
    while s <= r:
        if arr[count].get_state() == x:
            return count
        else:
            s += 1
        count += 1


def rhoCalc(arr, strAtt1, strAtt2):
    """
    To find Rho, this algorithim iterates through the
    states object one time, and in that iteration, 
    uses deepcopy() to make copy and sort based on its
    attribute thats passed and comapred to the second 
    index found of the same state. This returns an index
    that is fed into the summation portion of the equation.
    Once done, are plugged into the overall equation. Then
    returning the p value. 

    :param: arr - object array with States data
    :param: strAttr1 - the string form of what attr is being
        looked for in the merge sort
    :param: strAttr2 - the string form of what attr is being
        looked for in the merge sort
    :return null

    """
    # p1 MHI CCR
    dTotal = 0
    count = 0

    for state in arr:  # loops 50 times Florida
        med = deepcopy(arr)
        mergesort2(med, strAtt1)
        index = seqsearch(med, state.get_state()) + 1
        case = deepcopy(arr)
        mergesort2(case, strAtt2)
        index2 = seqsearch(case, state.get_state()) + 1
        index = (index2 - index)
        dTemp = math.pow(index, 2)
        dTotal += dTemp
        count += 1
    temp = (6 * dTotal)
    final = len(arr) * ((pow(len(arr), 2)) - 1)
    final = 1 - (temp / final)
    return final


def printStates(arr):
    """
    Simply takes in arr of objects and iterates 
    to print the data using getters 

    :param: arr - object array with States data
    :return null

    """
    print(f"{'State':29s}{'MHI':16s}{'VCR':15s}{'CFR':20s}{'Case Rate':20s}{'Death Rate':30s}{'FVR':11s}")
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    for item in arr:
        print(f" {item.get_state():15s}  {item.get_medInc():15d} {item.get_violentcrime():15.1f}  {item.get_CFR():15.6f} {item.get_caseRate():22.2f} {item.get_deathRate():18.2f} \t\t\t {item.get_vacrates():4.3f} ")


if __name__ == '__main__':
    """
        Main function that handles user input and calling 
        all sorting methods. Also parses CSV and handles 
        menu call
        :param: null
        :return null
        """
    stateObj = []

    # From canvas zip src
    try:
        f = open('States.csv', 'r')
    except IOError:
        print('cannot open it')

    i = 0
    lines = csv.reader(f)

    # parse csv into object
    for line in lines:
        if i != 0:
            stateObj.append(States(line[0], line[1], line[2], line[3], line[4], line[5],
                                   line[6], line[7], line[8], line[9]))
        i += 1
    # Print state object

    select = 0
    isSorted = False

    while select != "6":
        select = input("\nEnter a number between 1-6\n1. Print states report\n2. Sort by name\n"
                       "3. Sort by case fatality rate\n4. Find and print a states info give a name\n"
                       "5. Print Spearmnas Rho Matrix\n6. Quit\n\n")
        if select == "1":
            printStates(stateObj)
        elif select == "2":
            quicksort(stateObj, 0, 49)
            isSorted = True
            print("States sorted by Name")

        elif select == "3":
            mergesort2(stateObj, "CFR")
            isSorted = False
            print("States sorted by Case Fatality Rate")

        elif select == "4":
            userState = input("Enter a State name: \n")
            if isSorted:
                print("Binary Search")
                stateInfo = binarysearch(stateObj, userState)

                if stateInfo == -1:
                    print("Not a valid state name")
                else:
                    stateObj[stateInfo].__str__()
            else:
                print("Sequential Search")
                stateInfo = seqsearch(stateObj, userState)
                if isinstance(stateInfo, int) and (stateInfo != -1):
                    stateObj[stateInfo].__str__()
                else:
                    print("Not a valid state name")
                    continue

        elif select == "5":
            a = rhoCalc(stateObj, "medincome", "caseRate")
            b = rhoCalc(stateObj, "medincome", "deathRate")
            c = rhoCalc(stateObj, "violentcrime", "caseRate")
            d = rhoCalc(stateObj, "violentcrime", "deathRate")
            e = rhoCalc(stateObj, "vacrates", "caseRate")
            f = rhoCalc(stateObj, "vacrates", "deathRate")

            print("--------------------------------------------------\n"
                  "  \t      |  MHI  |   VCR   |  FVR  |\t\t\t  \n"
                  "--------------------------------------------------\n"
                  f"| Case Rate   |{a:5.3f} |  {c:5.3f}  | {e:5.3f}|\n"
                  "--------------------------------------------------\n"
                  f"| Death Rate  |{b:5.3f} |  {d:5.3f}  | {f:5.3f}|\n"
                  "--------------------------------------------------\n")

            continue
        elif select == "6":
            print("Thank you for using my application")
            break
        else:
            print("Please try again, that is an invalid input")
            continue

f.close()
