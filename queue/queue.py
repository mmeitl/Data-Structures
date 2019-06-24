class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = Linked_List()

  def enqueue(self, item):
    if self.storage.head == None:
      value = Node(item)
      self.storage.change_head(value)
 			self.size =+ 1
    else:
      self.storage.change_tail(item)
			self.size += 1
  
  def dequeue(self):
     if self.storage.head == None:
			return None
		else:
			removed_node = Node(self.storage.head.get_value())
			self.storage.change_head()
			self.size -= 1
			return removed_node.get_value()

  def len(self):
    return self.size

  def len(self):
    pass
