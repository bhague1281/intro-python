# until the user types 'EXIT', ask the user for a todo item. Then append the
# item to the todos list.

todos = []

while True:
  item = raw_input("Enter your todo (EXIT to quit): ")
  if item == 'EXIT':
    break

  todos.append(item)

  print item
  print todos