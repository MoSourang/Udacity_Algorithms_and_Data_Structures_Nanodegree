"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

def find_the_longest_time_spent_on_calls(records):
    ## create dictionary with phone # as the keys and time spent on a calls as the value
    time_spent_on_calls  = {}
    for record in records:
      if record[0] in time_spent_on_calls:
          time_spent_on_calls[record[0]] += int(record[3])
      else:
          time_spent_on_calls[record[0]] = int(record[3])
      if  record[1] in time_spent_on_calls:
          time_spent_on_calls[record[1]] += int(record[3])
      else:
           time_spent_on_calls[record[1]] = int(record[3])

    ## finds the longest time spent on call by a phone #
    longest_time_on_phone = 0
    phone_number = ''
    for key , value in time_spent_on_calls.items():
        if value > longest_time_on_phone:
            longest_time_on_phone = value
            phone_number = key

    return phone_number, longest_time_on_phone

results = find_the_longest_time_spent_on_calls(calls)

## solution
print(f'{results[0]} spent the longest time, {results[1]} seconds, on the phone during September 2016.')
## Big O: At the worst case the solution will run at O(2n + n), or simply O(n), because it iterates throught the given records once to create a dictionary 0(n) and
## iterates through the dictionary 2(n) to find the solution

def test_cases():
    assert find_the_longest_time_spent_on_calls([['111', '222', '01-01-1900', 10],
                                                ['111', '333', '01-01-1900', 100],
                                                ['222', '333', '01-01-1900', 20],
                                                ['111', '444', '01-01-1900', 1000]]) == ('111', 1110)

    assert find_the_longest_time_spent_on_calls([['111', '555', '01-01-1900', 10],
                                                ['555', '999', '01-01-1900', 100],
                                                ['999', '333', '01-01-1900', 20],
                                                ['666', '333', '01-01-1900', 1000]]) == ('333', 1020)



test_cases()
