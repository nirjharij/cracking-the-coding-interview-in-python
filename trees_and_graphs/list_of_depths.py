import sys
sys.path.append('..')
from binary_tree import BinarySearchTree
from linked_list.linked_list_operations import LinkedList


class ListDepth:
    def __init__(self):
        self.list = []

    def depth_first(self, node, level):
        if not node:
            return
        if len(self.list) == level:
            linked_list_obj = LinkedList()
            self.list.append(linked_list_obj)
            ll_obj = self.list[level]
        else:
            ll_obj = self.list[level]
        ll_obj.push(node.data)
        self.depth_first(node.left_child, level+1)
        self.depth_first(node.right_child, level+1)

    def breadth_first(self, node):
        # import pdb; pdb.set_trace()
        if node:
            linked_list_obj = LinkedList()
            linked_list_obj.push(node)
            self.list.append(linked_list_obj)
        else:
            return
        # while self.list:

        # while linked_list_obj.head:
        #     self.list.append(linked_list_obj)
        #     parent = linked_list_obj.pop()
        #     linked_list_obj = LinkedList()
        #     while parent and parent.data:
        #         if parent.data.left_child:
        #             print("Left child")
        #             print(parent.data.left_child.data)
        #             linked_list_obj.push(parent.data.left_child)
        #         if parent.data.right_child:
        #             print("Right child")
        #             print(parent.data.right_child.data)
        #             linked_list_obj.push(parent.data.right_child)
        #         parent = parent.next

    def print_list(self):
        for i in range(len(self.list)):
            ll_obj = self.list[i]
            ll_obj.traverse()
            print("\n")

    # def print_list_bfs(self):
    #     for i in range(len(self.list)):
    #         ll_obj = self.list[i]
    #         temp = ll_obj.head
    #         while temp:
    #             # print(temp.data, end=" -> ")
    #             print(temp.data.left_child.data)
    #             print(temp.data.right_child.data)
    #             temp = temp.next
    #         print("\n")


if __name__ == '__main__':
    bst_obj = BinarySearchTree()
    bst_obj.insert(20)
    bst_obj.insert(30)
    bst_obj.insert(10)
    bst_obj.insert(15)
    bst_obj.insert(12)
    bst_obj.insert(6)
    bst_obj.insert(2)
    bst_obj.in_order(bst_obj.root)
    list_depth = ListDepth()
    # list_depth.depth_first(bst_obj.root, 0)
    list_depth.breadth_first(bst_obj.root)
    # list_depth.print_list_bfs()

