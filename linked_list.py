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
		print("New data:{}".format(str(new_data)))
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

	def delete(self, key):
		print("deleting data: {}".format(str(key)))
		temp = self.head
		if temp:
			if temp.data == key:
				self.head = temp.next
				temp = None
				return

		while temp:
			if temp.data == key:
				break
			prev_node = temp
			temp = temp.next

		if temp == None:
			return

		prev_node.next = temp.next
		temp = None

	def reverse_print(self):
		print("reverse_print")
		if self.head == None:
			return
		temp = self.head
		self.head = self.head.next
		self.reverse_print()
		print(temp.data)

	def reverse(self):
		while self.head:
			temp = self.head
			self.head = self.head.next
			temp.next = None

if __name__ == '__main__':
	llist = LinkedList()
	llist.push(3)
	llist.push(5)
	llist.push(7)
	llist.push(1)
	llist.delete(1)
	llist.traverse()
	llist.reverse_print()