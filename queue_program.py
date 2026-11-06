"""Queue (FIFO): enqueue, dequeue, front, rear, display, size."""

queue = []


def enqueue():
    item = input("Item to enqueue: ")
    queue.append(item)
    print(f"Enqueued '{item}'.")


def dequeue():
    if not queue:
        print("Queue underflow: the queue is empty.")
    else:
        print(f"Dequeued '{queue.pop(0)}'.")


def front():
    print(f"Front: {queue[0]}" if queue else "Queue is empty.")


def rear():
    print(f"Rear: {queue[-1]}" if queue else "Queue is empty.")


def display():
    if not queue:
        print("Queue is empty.")
    else:
        print("FRONT -> " + " <- ".join(queue) + " <- REAR")


def size():
    print(f"Size: {len(queue)}")


actions = {"1": enqueue, "2": dequeue, "3": front, "4": rear, "5": display, "6": size}

while True:
    print("\n=== QUEUE (FIFO) ===")
    print("1. Enqueue  2. Dequeue  3. Front  4. Rear  5. Display  6. Size  7. Exit")
    choice = input("Choose: ").strip()
    if choice == "7":
        print("Goodbye!")
        break
    actions.get(choice, lambda: print("Invalid choice."))()
