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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""

## calls a records of all the phone # calls by fixed line in bangalore
def find_calls_from_fixed_bangalore():
    bangalore_prefix = '(080)'
    numbers_called_by_bangalore = []
    for record in calls:
        if record[0][0:5] == bangalore_prefix:
            numbers_called_by_bangalore.append(record[1])

    return numbers_called_by_bangalore

def find_prefix_of_all_numbers_called_by_bangalore():
    unique_prefixes = []
    all_numbers = find_calls_from_fixed_bangalore()
    for number in all_numbers:
        fixed_prefix = number.split(')')[0]+')'
        ## check for calls to Telemarketers
        if number[0:4] == '140'and number[0:4] not in unique_prefixes:
            unique_prefixes.append(number[0:4])
        ## check for calls to mobile phone number
        if number[5] == ' ' and number[0:4] not in unique_prefixes:
            unique_prefixes.append(number[0:4])
        ## check for calls to fixed lines
        if number[0:2] == '(0' and fixed_prefix not in unique_prefixes:
            unique_prefixes.append(fixed_prefix)

    ## sort and print out result
    unique_prefixes.sort()
    for prefix in unique_prefixes:
        print(prefix)


## Solution Part A
print('The numbers called by people in Bangalore have codes:')
find_prefix_of_all_numbers_called_by_bangalore()
## Big O: The solution leverages two different functions to accomplish the task, find_calls_from_fixed_bangalore(), runs at O(n) since  we are iterating through the input once.
## find_prefix_of_all_numbers_called_by_bangalore() runs at O(n^2+ n log n + c), since we are iterating through input and for each iteration
## we looping through the list again by using not in O(n^2), then sorting the results (n log n) and finally printing out the result O(c),
## therefore this solution will run at O(n^2 + n log n + c) or simply O(n^2))


"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def percentage_of_calls_to_fixed_in_bangalore():
    calls_from_fixed_in_bangalore = find_calls_from_fixed_bangalore()
    call_from_fixed_to_fixed_in_bangalore = 0
    for number in calls_from_fixed_in_bangalore:
        if number[0:5] == '(080)':
            call_from_fixed_to_fixed_in_bangalore += 1

    return round((call_from_fixed_to_fixed_in_bangalore/len(calls_from_fixed_in_bangalore)) * 100, 2)


#Solution: Part B:
print(f"{percentage_of_calls_to_fixed_in_bangalore()} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
##  Big O: This solution leverage two different functions to accomplish the task, find_calls_from_fixed_bangalore() runs at O(n) since we are iterating through the input once
## and percentage_of_calls_to_fixed_in_bangalore also runs at O(n) since we are also interating through the input array once, therefore in the worst case this solution will run at
# O(2n) or more simply (n)
