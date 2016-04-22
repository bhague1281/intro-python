# import csv package
import csv
import numpy

data = []

with open('titanic.csv') as titanic_file:
    reader = csv.reader(titanic_file, delimiter=',')
    for row in reader:
        data.append(row)

survived = 0
perished = 0

# print(data[1][2])
for row in data[1:]:
    # print row[2]
    if int(row[2]) == 0:
        perished += 1
    else:
        survived += 1

print(perished)
print(survived)



# print('{} people died on the Titanic').format(perished)
percentage = perished / float(perished+survived)
print('{}% died on the Titanic').format(percentage)

ages = []
for row in data[1:]:
    if row[4] != 'NA':
        ages.append(float(row[4]))
# print ages

print(numpy.mean(ages))
print(numpy.amin(ages))
