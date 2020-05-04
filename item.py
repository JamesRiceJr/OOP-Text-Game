class Item():
  
  def __init__(self, item_name):
    self.name = item_name
    self.description = None
    self.owner = False
    
  def set_name(self, new_item_name):
    self.name = new_item_name
  
  def set_description(self, new_description):
    self.description = new_description
    
  def get_name(self):
    return self.name
      
  def get_description(self):
    return self.description
      
  def pickup(self):
    self.owner = True
  