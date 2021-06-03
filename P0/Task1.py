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
TASK 1:
How many different telephone numbers are there in the records?
"There are <count> different telephone numbers in the records."
"""

all_non_unique_numbers =  []

## getting all phone records from calls and appending the # in an array
for record in calls:
    all_non_unique_numbers.append(record[0])
    all_non_unique_numbers.append(record[1])

## getting all phone records from texts and appending the # in an array
for record in texts:
    all_non_unique_numbers.append(record[0])
    all_non_unique_numbers.append(record[1])

## function to help remove duplicates from the list of phone numbers
def remove_duplicates(non_unique_list):
    unique_list = []
    unique_list.append(non_unique_list[0])
    for element in non_unique_list:
        counter = 0
        for number in unique_list:
            counter += 1
            if element != number and counter == len(unique_list):
                unique_list.append(element)
            elif element != number:
                continue
            else:
                break
    return unique_list

## solution
count_of_numbers = len(remove_duplicates(all_non_unique_numbers))
print(f'There are {count_of_numbers} different telephone numbers in the records.')
## Big O: At the worst case this solution runs at O(n2) - Quadratic Time,
## because for each element in the input we perform a search operation and a comparison operation

## Test cases
def test_cases():
    assert remove_duplicates([1, 1, 2, 2, 2, 3, 3, 3,]) == [1, 2, 3]
    assert remove_duplicates([2, 2, 2,]) == [2]
    assert remove_duplicates([10]) == [10]
    assert remove_duplicates([190, 190, 190, 1]) == [190, 1]


test_cases()
