from __future__ import annotations


class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self, head: Node = None):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        self.head.preb = new_node
        new_node.next = self.head
        self.head = new_node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data):
        current_node = self.head
        # 先頭を削除する場合
        if current_node and current_node.data == data:
            current_node = None
            self.head = None
            return
        else:
            next_node = current_node.next
            next_node.prev = None
            current_node = None
            self.head = next_node
            return

        # 先頭以外を削除する場合
        while current_node and current_node.data != data:
            current_node = current_node.next
        ## どれにもヒットしなかった場合
        if current_node is None:
            return
        ## 最後のノードを削除する場合
        if current_node.next is None:
            prev = current_node.prev
            prev.next = None
            current_node = None
            return
        else:
            next_node = current_node.next
            prev_node = current_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node = None
            return

    def reverse_iterative(self):
        previous_node = None
        current_node = self.head
        while current_node:
            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node

            current_node = current_node.prev

        if previous_node:
            self.head = previous_node.prev

    def sort(self):
        if self.head is None:
            return

        current_node = self.head
        while current_node.next:
            next_node = current_node.next
            while next_node:
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = next_node.data, current_node.data
                next_node = next_node.next
            current_node = current_node.next



if __name__ == '__main__':
    d = DoublyLinkedList()
    d.append(1)
    d.append(3)
    d.append(9)
    d.append(6)
    d.append(2)
    d.print()
    print("#########")
    d.reverse_iterative()
    d.print()
    print("######### Sort")
    d.sort()
    d.print()