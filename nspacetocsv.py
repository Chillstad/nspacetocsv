import re

input_file = open("input.txt")
nspace = input_file.read()
input_file.close()

regex_result = re.sub("[^\S\n]+", ",", nspace)

result = ""

for line in regex_result.splitlines():
    result += line[1:] + '\n'

output_file = open("output.csv", "w+")
output_file.write(result)
output_file.close()