"""
Intro to Python Lab 1, Task 4

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
telemarketers = set()

for call in calls:
    if str(call[0]).startswith("140"):
        telemarketers.add(call[0])
for call in calls:
    if call[1] in telemarketers:
        telemarketers.remove(call[1])
for text in texts:
    if text[0] in telemarketers :
        telemarketers.remove(text[0])
    elif text[1] in telemarketers:
        telemarketers.remove(text[1])
print("These numbers could be telemarketers: {}{}".format("\n","\n".join(sorted(set(telemarketers)))))


