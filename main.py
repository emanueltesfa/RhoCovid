import csv
from States import *


def quicksort(input_list, low, high):
    if low < high:
        partition_index = partition(input_list, low, high)
        quicksort(input_list, low, partition_index - 1)
        quicksort(input_list, partition_index + 1, high)


def partition(input_list, low, high):
    i = (low - 1)
    pivot = input_list[high].get_state
    for j in range(low, high):
        if j <= pivot:
            i = i + 1
            input_list[i].get_state, input_list[j].get_state = input_list[j].get_state, input_list[i].get_state
    input_list[i+1].get_state, input_list[high].get_state = input_list[high].get_state, input_list[i+1].get_state
    return i+1


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
            stateObj.append(States(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9]))
        i += 1
    # Print state object
    for item in stateObj:
        # print(item.get_pop())
        # quicksort(stateObj, 0, 49)
        print(f' State: {item.get_state()}, Capitol: {item.get_capitol()}, Region: {item.get_capitol()},'
              f' House Seats: {item.get_houseseat()}, Population: {item.pop}, Covid Cases: {item.get_covcases()},'
              f' Covid Deaths: {item.get_covdeaths()}, Vaccine Rates: {item.get_vacrates()},'
              f'Median Income: {item.medincome}, Violent Crime: {item.get_violentcrime() }')
        if stateObj[2].get_state() > stateObj[3].get_state():
            print("2")
        else:
            print("3")

    """
     # print(States.get_pop(States))
        # list[i] = States().set
        # States.set_state(line[0])
        # list[i] = States.set_state(line[0])
        # list.writeHeader();
        stateName = line[0]
        list[i].set_state(stateName)
        list[i].set_capitol(line[1])
        list[i].set_region(line[2])
        list[i].set_houseseat(line[3])
        list[i].set_pop(line[4])
        list[i].set_covcases(line[5])
        list[i].set_covdeaths(line[6])
        list[i].set_vacrates(line[7])
        list[i].set_medincome(line[8])
        list[i].set_violentcrime(line[9])
"""

    # print(States.__dict__)
    f.close()





