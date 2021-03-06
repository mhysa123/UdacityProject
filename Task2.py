"""
Intro to Python Lab 1, Task 2

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Lab Preparation page.
"""

"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
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

HINT: Build a dictionary with telephone numbers as keys, and their
total time spent on the phone as the values. You might find it useful
to write a function that takes a key and a value and modifies a 
dictionary. If the key is already in the dictionary, add the value to
the key's existing value. If the key does not already appear in the
dictionary, add it and set its value to be the given value.
"""
#create a dictionary for store telephone numbers and total time
conn_dictionary = {}
spend_time = 0
"""for call in calls:
    conn_dictionary[call[0]] = call[3]"""
def check_dictionary(calls_table):
    for call in calls_table:
        if call[0] not in conn_dictionary:
            conn_dictionary[call[0]] = int(call[3])
        else:
            spend_time = conn_dictionary[call[0]]
            conn_dictionary[call[0]] =spend_time + int(call[3])
        if call[1] not in conn_dictionary:
            conn_dictionary[call[1]] = int(call[3])
        else:
            spend_time = int(conn_dictionary[call[1]])
            conn_dictionary[call[1]] = spend_time + int(call[3])
    """sort the dictionary by the value an then get the fist item"""
    #print(sorted(conn_dictionary.items(), key=lambda e:e[1], reverse=True))
    return sorted(conn_dictionary.items(), key=lambda e:e[1], reverse=True)[0]
longget_time = check_dictionary(calls)
code = longget_time[0]
seconds = longget_time[1]
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(code,seconds))