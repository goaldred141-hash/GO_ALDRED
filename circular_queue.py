"""Circular queue with a user-defined capacity."""


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.count = 0

    def is_full(self):
        return self.count == self.capacity

    def is_empty(self):
        return self.count == 0

    def enqueue(self, item):
        if self.is_full():
            print("Queue overflow: the queue is full.")
            return
        rear = (self.front + self.count) % self.capacity
        self.items[rear] = item
        self.count += 1
        print(f"Enqueued '{item}' at slot {rear}.")

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow: the queue is empty.")
            return
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        print(f"Dequeued '{item}'.")

    def display(self):
        print("Slots:", self.items)
        if self.is_empty():
            print("Queue is empty.")
        else:
            order = [self.items[(self.front + i) % self.capacity] for i in range(self.count)]
            print("Order (front -> rear):", order)


while True:
    try:
        cap = int(input("Enter queue capacity: "))
        if cap > 0:
            break
    except ValueError:
        pass
    print("Enter a positive whole number.")

cq = CircularQueue(cap)

while True:
    print("\n=== CIRCULAR QUEUE ===")
    print("1. Enqueue  2. Dequeue  3. Display  4. Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        cq.enqueue(input("Item to enqueue: "))
    elif choice == "2":
        cq.dequeue()
    elif choice == "3":
        cq.display()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
