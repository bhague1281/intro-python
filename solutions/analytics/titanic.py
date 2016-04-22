# import data about the titanic passengers, and get data!

import csv

# create list to store data
data = []

# open titanic.csv and store data in titanic
with open('titanic.csv') as t_file:
  # include delimiter because there are multiple fields
  reader = csv.reader(t_file, delimiter=',')
  for row in reader:
    data.append(row)

# if we print the first row, it's not really data. It's a header
# that shows what each row represents
print data[0]

# for example, the 3rd element of the first row returns whether
# or not the passenger survived
print data[0][2]

# let's iterate through data and get how many people survived and perished
# Note: the 3rd element should be '1' if the passenger survived, '0' if perished
survived = 0
perished = 0

# another note: we use data[1:] in order to exclude the first element, which is a header
for passenger in data[1:]:
  if passenger[2] == '1':
    survived += 1
  else:
    perished += 1

print '{} people survived on the Titanic.'.format(survived)
print '{} people perished on the Titanic.'.format(perished)

# so what percentage survived? we can divide the surived by the total, then multiply
# by 100 to get the percentage
fract_survived = survived / float(survived + perished)
percent_survived = fract_survived * 100

print 'On the Titanic, only {}% of the passengers survived.'.format(percent_survived)