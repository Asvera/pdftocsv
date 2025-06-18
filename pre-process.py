import csv

# Input and output file names
input_file = 'file1.csv'
output_file = 'output.csv'

with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    for row in reader:
        # Assume the third field (index 2) is the one with the newline
        if len(row) > 2 and '\n' in row[2]:
            names = row[2].split('\n')
            new_row = row[:2] + names + row[3:]
            writer.writerow(new_row)
        else:
            writer.writerow(row)

