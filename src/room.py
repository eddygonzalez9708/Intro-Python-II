# Implement a class to hold room information.
# This should have name and description attributes.

class Room:
  def __init__(self, name, description, items):
    self.name = name
    self.description = description
    self.items = items

  def getItems(self):
    if len(self.items) > 0:
      print('\nThe following item(s) is(are) in this room:')

      for num in range(len(self.items)):
        item = self.items[num]
        print(f'\n{num + 1}. {item.name} - {item.description}')
    else:
      print('\nThis room does not have any items.')
  
  def addItem(self, item):
    self.items.append(item)
    print(f'\nThe following item was added to this room: {item.name}')
  
  def removeItem(self, player, item):
    for num in range(len(self.items)):
      i = self.items[num]
      if i.name.lower() == item:
        player.addItem(i)
        self.items.pop(num)
        return
    
    print(f'\nThe following item is not in this room: {item}')