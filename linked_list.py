class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def traverse(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def insertafter(self, prev_node, new_data):
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def insertatend(self, new_data):
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
			return	
		last = self.head
		while (last.next):
			last = last.next

		last.next = new_node

if __name__ == '__main__':
	llist = LinkedList()
	llist.head = Node(23)
	second = Node(43)
	third = Node(63)
	llist.head.next = second
	second.next = third
	llist.traverse()
