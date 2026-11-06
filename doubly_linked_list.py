"""Doubly linked list: insert head/tail, delete by value, display forward/backward."""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        print(f"Inserted '{data}' at head.")

    def insert_tail(self, data):
        node = Node(data)
        if not self.tail:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        print(f"Inserted '{data}' at tail.")

    def delete_value(self, data):
        cur = self.head
        while cur and cur.data != data:
            cur = cur.next
        if not cur:
            print(f"'{data}' not found.")
            return
        if cur.prev:
            cur.prev.next = cur.next
        else:
            self.head = cur.next
        if cur.next:
            cur.next.prev = cur.prev
        else:
            self.tail = cur.prev
        print(f"Deleted '{data}'.")

    def display_forward(self):
        if not self.head:
            print("List is empty.")
            return
        parts, cur = [], self.head
        while cur:
            parts.append(str(cur.data))
            cur = cur.next
        print("None <-> " + " <-> ".join(parts) + " <-> None")

    def display_backward(self):
        if not self.tail:
            print("List is empty.")
            return
        parts, cur = [], self.tail
        while cur:
            parts.append(str(cur.data))
            cur = cur.prev
        print("None <-> " + " <-> ".join(parts) + " <-> None")


dll = DoublyLinkedList()

while True:
    print("\n=== DOUBLY LINKED LIST ===")
    print("1. Insert at head  2. Insert at tail  3. Delete by value")
    print("4. Display forward  5. Display backward  6. Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        dll.insert_head(input("Value: "))
    elif choice == "2":
        dll.insert_tail(input("Value: "))
    elif choice == "3":
        dll.delete_value(input("Value to delete: "))
    elif choice == "4":
        dll.display_forward()
    elif choice == "5":
        dll.display_backward()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
