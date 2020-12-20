from Node import Node

class PriorityQueue:
	__head = None
	__tail = None
	__size = 0


	def __init__(self):
		self.__head = None
		self.__tail = None
		self.__size = 0

	# push item by the priority order
	def push(self, value, priority = 0):
		if not type(priority) is int:
			raise Exceptoin("Priority should be an interger value.")
		node = Node(value, int(priority))

		# handel the empty queue
		if self.__tail == None:
			self.__tail = node
			self.__head = node
		else:
			# handel None empty queue
			itr = self.__head
			while itr !=None and itr.priority >= node.priority:
				itr = itr.next_ptr

			# if there is no lower priority
			if itr == None:
				self.__tail.next_ptr = node
				node.prev_ptr = self.__tail
				self.__tail = node
			else:
				# if the iterator node was the head
				if itr.prev_ptr != None:
					itr.prev_ptr.next_ptr = node
				else:
					self.__head = node
				node.prev_ptr = itr.prev_ptr
				node.next_ptr = itr
				itr.prev_ptr = node

	def pop(self):
		if self.__head == self.__tail:
			self.__head = None
			self.__tail = None
		else:
			self.__head = self.__head.next_ptr
			self.__head.prev_ptr = None


	def show(self):
		print("=================================")
		itr = self.__head
		while itr != None:
			print(itr.value)
			itr = itr.next_ptr
		print("=================================")