from Node import Node

class PriorityQueue:
	__head = None
	__tail = None
	__size = 0


	def __init__(self):
		self.__head = None
		self.__tail = None
		self.__size = 0


	def push(self, value, priority = 0):
		if not typeof(priority) is int:
			raise Exceptoin("Priority should be an interger value.")
		node = Node(value, int(priority))
		itr = self.__head
		while itr != None and itr.priority >= node.priority:
			itr = itr.next_ptr

		if itr = None:
			self.__tail = node
		else:
			itr.prev_ptr.next_ptr = node
			node.prev_ptr = itr.prev_ptr
			node.next_ptr = itr
			itr.prev_ptr = node

		if self.__head = None:
			self.__head = self.__tail

