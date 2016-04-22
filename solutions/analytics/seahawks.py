# sentiment analysis of tweets

# import packages (may have to install numpy and pattern using pip)
# pip install numpy
# pip install pattern
import csv
import numpy
from pattern.en import sentiment

# create a list to store our data
all_data = []

# open the seahawks csv and send it to the csv reader,
# then go through each line and add it to all_data
with open('seahawks.csv') as seahawks_file:
  data = csv.reader(seahawks_file)
  for entry in data:
    # print entry
    all_data.append(float(entry[1]))

all_data = [s for s in all_data if s != 0.0]
print(all_data)

# print all_data
# print the mean, median, max, and min of the sentiments
print('Mean: {}'.format(numpy.mean(all_data)))
print('Median: {}'.format(numpy.median(all_data)))
print('Max: {}'.format(numpy.amax(all_data)))
print('Min {}'.format(numpy.amin(all_data)))
