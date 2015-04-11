import csv

reader = csv.reader(open('wunder-data.txt', 'r'), delimiter=",")
writer = open('wunder-data.json', 'w')

writer.writelines('{ "observations": [')
rows_so_far = 0
for row in reader:
    rows_so_far += 1

    writer.write("{")
    writer.write('"date": "' + row[0] + '", ')
    writer.write('"temperature": ' + row[1])

    if rows_so_far < 365:
        writer.write(" },\n")
    else:
        writer.write(" }\n")

writer.write("] }")