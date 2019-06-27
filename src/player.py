# Write a class to hold player information. 
# Example: What room they are in currently.

class Player:
  def __init__(self, name, current_room, items = []):
    self.name = name
    self.current_room = current_room
    self.items = items
  
  def getItems(self):
    if len(self.items) > 0:
      print('\nYou have the following item(s):')
      
      for num in range(len(self.items)):
        item = self.items[num]
        print(f'\n{num + 1}. {item.name} - {item.description}')
    else:
      print('\nYou do not have any items.')
  
  def addItem(self, item):
    self.items.append(item)
    print(f'\nThe following item was added to your inventory: {item.name}')
  
  def removeItem(self, room, item):
    for num in range(len(self.items)):
      i = self.items[num]
      if i.name.lower() == item:
        room.addItem(i)
        self.items.pop(num)
        return
    
    print(f'\nYou do not have the following item: {item}')