class Node:
	value = None
	next_ptr = None
	prev_ptr = None
	priority = 0	
	def __init__(self, value = None, priority = 0):
		self.value = value
		self.next_ptr = None
		self.perv_ptr = None
		self.priority = priority
