class Room:
  def __init__(self, name, description, items):
    self.__name = name
    self.__description = description
    self.__items = items

  def getName(self):
    return self.__name

  def getDescription(self):
    return self.__description

  def getItems(self):
    return self.__items

  def setName(self, new_name):
    self.__name = new_name

  def setDescription(self, new_desciption):
    self.__description = new_desciption

  def addItem(self, new_item):
    self.__items.append(new_item)

  def removeItem(self, remove_item):
    self.__items.remove(remove_item)

  def lookAround(self):
    print(f' La {self.__name} {self.__description} e ci sono {self.__items}')

  def takeItem(self, item):
    if item in self.__items:
      self.__items.remove(item)
    else:
      print('The item you choose is not in the room')

if __name__ == '__main__':
    library = Room("library",1, ["sword", "book of shadows", "mouse"])
    #print(Room.helptp())
    print(library.lookAround())
    library.takeItem("mouse")
    print(library.lookAround())
    library.takeItem("book of shadows")
    print(library.lookAround())
    library.takeItem("bazooka")
