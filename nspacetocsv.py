import re
import argparse
import datetime

parser = argparse.ArgumentParser("Convert a text spreadsheet seperated by an unknown amount of spaces to a csv file.")
parser.add_argument("-o", help="Changes the name of the output file.", type=str, required=False)
args = vars(parser.parse_args())
print(args)

print("Paste your input in: ")

# Loop through pasted input until enter is pressed.
pasted_input = []
while True:
    line = input()
    if line:
        pasted_input.append(line)
    else:
        break

# Combine individual lines.
nspace = '\n'.join(pasted_input)

# Use regex to remove every group of spaces with a single comma.
regex_result = re.sub("[^\S\n]+", ",", nspace)

result = ""

# Remove first character.
# WARNING: This is here for my specific use case. The input you are passing in might not need this.
for line in regex_result.splitlines():
    if line[0] == ',':
        result += line[1:] + '\n'
    else:
        result += line + '\n'

if args["o"] == None:
    output_file = open(f"output-{datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")}.csv", "w+")
else:
    output_file = open(f"{args["o"]}.csv", "w+")
    
output_file.write(result)
output_file.close()