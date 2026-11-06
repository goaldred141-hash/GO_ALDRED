"""Singly linked list: insert (head/tail/position), delete, search, display, reverse."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_head(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    def insert_tail(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self.length += 1

    def insert_at(self, data, pos):
        if pos < 0 or pos > self.length:
            print("Invalid position.")
            return
        if pos == 0:
            self.insert_head(data)
            return
        cur = self.head
        for _ in range(pos - 1):
            cur = cur.next
        node = Node(data)
        node.next = cur.next
        cur.next = node
        self.length += 1
        print(f"Inserted '{data}' at position {pos}.")

    def delete_value(self, data):
        cur, prev = self.head, None
        while cur and cur.data != data:
            prev, cur = cur, cur.next
        if not cur:
            print(f"'{data}' not found.")
            return
        if prev:
            prev.next = cur.next
        else:
            self.head = cur.next
        self.length -= 1
        print(f"Deleted '{data}'.")

    def search(self, data):
        cur, i = self.head, 0
        while cur:
            if cur.data == data:
                print(f"'{data}' found at position {i}.")
                return
            cur, i = cur.next, i + 1
        print(f"'{data}' not found.")

    def reverse(self):
        prev, cur = None, self.head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        self.head = prev
        print("List reversed.")

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        parts, cur = [], self.head
        while cur:
            parts.append(str(cur.data))
            cur = cur.next
        print(" -> ".join(parts) + " -> None")


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


ll = LinkedList()

while True:
    print("\n=== SINGLY LINKED LIST ===")
    print("1. Insert at head  2. Insert at tail  3. Insert at position")
    print("4. Delete by value  5. Search  6. Reverse  7. Display  8. Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        ll.insert_head(input("Value: "))
    elif choice == "2":
        ll.insert_tail(input("Value: "))
    elif choice == "3":
        ll.insert_at(input("Value: "), read_int(f"Position (0 to {ll.length}): "))
    elif choice == "4":
        ll.delete_value(input("Value to delete: "))
    elif choice == "5":
        ll.search(input("Value to search: "))
    elif choice == "6":
        ll.reverse()
    elif choice == "7":
        ll.display()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
