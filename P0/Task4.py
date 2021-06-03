"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
## create a list of all numbers that sends texts, receive text or receive calls
all_unique_numbers = []
all_active_numbers = []

def find_all_active_numbers():
    ## all nunbers receiving calls
    for number in calls:
        if number[1] not in all_active_numbers:
            all_active_numbers.append(number[1])
    ## all numbers sending text messages
    for number in texts:
        if number[0] not in all_active_numbers:
            all_active_numbers.append(number[0])
    ## all numbers receiving text messages
    for numbers in texts:
        if number[1] not in all_active_numbers:
            all_active_numbers.append(number[1])

    return all_active_numbers


def find_all_unique_numbers():
    for number in calls:
            ## all numbers making calls
        if number[0] not in all_unique_numbers:
            all_unique_numbers.append(number[0])
            ## all bnumbers receiving calls
        if number[1] not in all_unique_numbers:
            all_unique_numbers.append(number[1])
        ## all numbers sending text messages
    for number in texts:
        if number[0] not in all_unique_numbers:
            all_unique_numbers.append(number[0])
        ## all numbers receiving text messages
        if number[1] not in all_unique_numbers:
                all_unique_numbers.append(number[1])

    return all_unique_numbers


telemarketers_numbers = set()
unique_numbers = set(find_all_unique_numbers())
activte_number = set(find_all_active_numbers())


def find_telemarketers_numbers():
    telemarketers_numbers = list(unique_numbers.difference(activte_number))
    telemarketers_numbers.sort()
    for number in telemarketers_numbers:
        print(number)

## Solution
print("These numbers could be telemarketers:")
find_telemarketers_numbers()
##Big O: This solution leverages 3 different functions to accomplish the task, find_all_active_numbers() runs at O(n^2)
## since we are iterating through the given input once and for each iteration searching the list for that input.
## find_all_unique_numbers(), also runs at O(n^2) since we are iterating through the input and for each iteration
## searching for that input on the list. Finally find_telemarketers_numbers runs at O(n log n + 2n)
## since we are using a set method to finds differences between ##our two input O(n), sorting that result (n log n) and
## finally iterating through the result to print out each value O(n). Therefore, in the worst case this solution will run at  O(n^4 + n log n + 2n)  or more simply O(n^4). 
