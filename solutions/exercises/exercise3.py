# uncomment the sections you want to run

# loop 5 times and print 'hi'. But print 'first hi!' during the first iteration
counter = 0
while counter < 5:
  if counter == 0:
    print "first hi!"
  else:
    print "hi"
  counter = counter + 1

# # loop 5 times and print 'hi'. But exit the loop early on the third iteration.
# counter2 = 0
# while counter2 < 5:
#   print "hi"
#   if counter2 == 2:
#     break
#   counter2 = counter2 + 1

# # ask user for a list item until they enter 'EXIT'
# while True:
#   my_list_item = raw_input("Enter a list item (type EXIT to quit): ")
#   if my_list_item == 'EXIT':
#     break
#   print my_list_item


# # ask the user how many items they want, then loop that many times. For each loop,
# # ask the user the name of their item.
# number_of_loops = raw_input("How many items do you want? ")
# number_of_loops = int(number_of_loops)

# counter3 = 0

# while counter3 < number_of_loops:
#   a = raw_input("Name your item: ")
#   print a
#   counter3 = counter3 + 1