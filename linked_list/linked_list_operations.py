class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def traverse(self):
		temp = self.head
		while temp:
			print(temp.data, end=" -> ")
			temp = temp.next

	def push(self, new_data):
		print("New data:{}".format(str(new_data)))
		new_node = Node(new_data)
		new_node.next = self.head
		if self.head is None:
			self.tail = new_node
		self.head = new_node

	def pop(self):
		if self.head:
			temp = self.head
			self.head = self.head.next
			return temp
		else:
			return None

	def insertafter(self, prev_node, new_data):
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def insertatend(self, new_data):
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
			return	
		last = self.head
		while (last.next):
			last = last.next

		last.next = new_node
		self.tail = new_node

	def delete(self, key):
		print("deleting data: {}".format(str(key)))
		temp = self.head
		if temp:
			if temp.data == key:
				self.head = temp.next
				temp = None
				return
		prev_node = temp
		while temp:
			if temp.data == key:
				break
			prev_node = temp
			temp = temp.next

		if temp is None:
			return

		prev_node.next = temp.next

	def reverse_print(self):
		print("reverse_print")
		if self.head is None:
			return
		temp = self.head
		self.head = self.head.next
		self.reverse_print()
		print(temp.data)

	def reverse(self):
		print("inside reverse")
		prev_node = None
		while self.head.next:
			next_node = self.head.next
			self.head.next = prev_node
			prev_node = self.head
			self.head = next_node
		
		self.head.next = prev_node

	def remove_duplicates(self):
		temp_dict = dict()
		temp = self.head
		prev_node = temp
		while temp:
			if temp.data in temp_dict:
				prev_node.next = temp.next
				temp = temp.next
			else:
				temp_dict[temp.data] = 1
				prev_node = temp
				temp = temp.next

	def remove_duplicates_without_buffer(self):
		p1_ptr = self.head
		p2_ptr = self.head.next
		while p1_ptr:
			data = p1_ptr.data
			prev_node = p1_ptr
			while p2_ptr:
				if p2_ptr.data == data:
					prev_node.next = p2_ptr.next
				else:
					prev_node = p2_ptr
				p2_ptr = p2_ptr.next
			p1_ptr = p1_ptr.next
			if p1_ptr:
				p2_ptr = p1_ptr.next
			else:
				break


if __name__ == '__main__':
	llist = LinkedList()
	llist.push(4)
	llist.push(7)
	llist.push(1)
	llist.push(2)
	llist.push(2)
	llist.push(7)
	# llist.reverse()
	llist.remove_duplicates_without_buffer()
	llist.traverse()
