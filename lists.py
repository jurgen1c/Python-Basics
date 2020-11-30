class node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class linked_list:
  def __init__(self):
    self.head = node()
  
  