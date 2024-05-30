import re
import sys
import datetime

unique_output = True
try:
    unique_output = bool(sys.argv[1])
except:
    pass

print("Paste your input in: ")

pasted_input = []
while True:
    line = input()
    if line:
        pasted_input.append(line)
    else:
        break

nspace = '\n'.join(pasted_input)

regex_result = re.sub("[^\S\n]+", ",", nspace)

result = ""

for line in regex_result.splitlines():
    result += line[1:] + '\n'

if unique_output:
    output_file = open(f"output-{datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")}.csv", "w+")
else:
    output_file = open("output.csv", "w+")
output_file.write(result)
output_file.close()