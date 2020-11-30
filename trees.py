class node:
  def __init__(self, value = None):
    self.value = value
    self.left_child = None
    self.right_child = None

class binary_search_tree:
  def __init__(self)::
    self.root = None
  
  def insert(self, value):
    if self.root == None:
      self.root = node(value)
    else:
      self._insert(value, self.root)
  
  def _insert(self, value, current_node):
    if value < current_node.value:
      if current_node.left_child = None:
        current_node.left_child = node(value)
      else:
        self._insert(value, current_node.left_child)
    elif value < current_node.value:
      if current_node.right_child = None:
        current_node.right_child = node(value)
      else:
        self._insert(value, current_node.right_child)
    else:
      print("Value already in tree!")
  
  def print_tree(self):
    if self.root != None:
      self._print_tree(self.root)
  
  def _print_tree(self, current_node):
    if current_node != None:
      self._print_tree(current_node.left_child)
      print(str(current_node.value))
      self._print_tree(current_node.right_child)