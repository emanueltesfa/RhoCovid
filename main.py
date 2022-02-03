import csv
from States import *


def quicksort(state, low, high):
    if low < high:
        partition_index = partition(state, low, high)
        quicksort(state, low, partition_index - 1)
        quicksort(state, partition_index + 1, high)


def partition(state, low, high):
    count = (low - 1)
    pivot = state[high]
    for j in range(low, high):
        if state[j].get_state() < pivot.get_state():
            count += 1
            state[count], state[j] = state[j], state[count]
    state[count + 1], state[high] = state[high], state[count + 1]
    return count+1


def mergeSort(nlist):
    if len(nlist) > 1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        a = b = c = 0

        while a < len(lefthalf) and b < len(righthalf):
            if lefthalf[a].getCFR() < righthalf[b].getCFR():
                nlist[c] = lefthalf[a]
                a += 1
            else:
                nlist[c] = righthalf[b]
                b += 1
            c += 1
        while a < len(lefthalf):
            nlist[c] = lefthalf[a]
            a += 1
            c += 1
        while b < len(righthalf):
            nlist[c] = righthalf[b]
            b += 1
            c += 1


def binarySearch(arr, x):
    x.lower()
    s = 0
    r = len(arr) - 1
    while s <= r:
        mid = (s + r) // 2
        if arr[mid].get_state().lower() == x:
            return mid
        elif x < arr[mid].get_state().lower():
            r = mid - 1
        elif x > arr[mid].get_state().lower():
            s = mid + 1
    return -1


def seqSearch(arr, x):
    s = 0
    count = 0
    r = len(arr) - 1
    while s <= r:
        if arr[count].get_state().lower() == x.lower():
            return count
        else:
            s += 1
        count += 1


if __name__ == '__main__':

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
    """
    for item in stateObj:
        # print(item.get_pop())
        # quicksort(stateObj, 0, 49)
        print(f' State: {item.get_state()}, Capitol: {item.get_capitol()}, Region: {item.get_region()},'
              f' House Seats: {item.get_houseseat()}, Population: {item.pop}, Covid Cases: {item.get_covcases()},'
              f' Covid Deaths: {item.get_covdeaths()}, Vaccine Rates: {item.get_vacrates()},'
              f'Median Income: {item.medincome}, Violent Crime: {item.get_violentcrime() }')
    """

    select = 0
    isSorted = False

    while select != "6":
        select = input("Select an option 1-6\n"
                       "1. Print a state report \n"
                       "2. Sort by name\n"
                       "3. Sort by case fatality rate \n"
                       "4. Find and print a State for a given name \n"
                       "5. Print Spearman’s rho matrix \n"
                       "6. Quit\n")

        if select == "1":

            for item in stateObj:
                print(f' State: {item.get_state()}, Capitol: {item.get_capitol()}, Region: {item.get_region()},'
                      f' House Seats: {item.get_houseseat()}, Population: {item.pop}, Covid Cases: {item.get_covcases()},'
                      f' Covid Deaths: {item.get_covdeaths()}, Vaccine Rates: {item.get_vacrates()},'
                      f'Median Income: {item.medincome}, Violent Crime: {item.get_violentcrime()}')

        elif select == "2":
            quicksort(stateObj, 0, 49)
            isSorted = True

        elif select == "3":
            mergeSort(stateObj)
            isSorted = False

        elif select == "4":
            userState = input("Enter a State name: \n")
            if isSorted:
                stateInfo = binarySearch(stateObj, userState)
                if stateInfo == -1:
                    print("Not a valid state name")
                else:
                    print(stateObj[stateInfo].get_capitol())
            else:
                stateInfo = seqSearch(stateObj, userState)
                if stateInfo == -1:
                    print("Not a valid state name")
                else:
                    print(stateObj[stateInfo].get_capitol())
        elif select == "5":
            continue
        elif select == "6":
            print("Thank you for using my application")
            break
        else:
            break

    """ 
        # test str call
        stateObj[1].__str__()
        
        # test gt call
        stateObj[1].__gt__(stateObj[2])

        # test > operator with attributes
        if stateObj[2].get_state() > stateObj[3].get_state():
            print("2")
        else:
            print("3")
            
        print(States.__dict__)
"""


    f.close()





