"""Stack (LIFO): push, pop, peek, display, size, is-empty."""

stack = []


def push():
    item = input("Item to push: ")
    stack.append(item)
    print(f"Pushed '{item}'.")


def pop():
    if not stack:
        print("Stack underflow: the stack is empty.")
    else:
        print(f"Popped '{stack.pop()}'.")


def peek():
    print(f"Top item: {stack[-1]}" if stack else "Stack is empty.")


def display():
    if not stack:
        print("Stack is empty.")
        return
    print("TOP")
    for item in reversed(stack):
        print(f"  | {item} |")
    print("BOTTOM")


def size():
    print(f"Size: {len(stack)}")


def is_empty():
    print("Empty." if not stack else "Not empty.")


actions = {"1": push, "2": pop, "3": peek, "4": display, "5": size, "6": is_empty}

while True:
    print("\n=== STACK (LIFO) ===")
    print("1. Push  2. Pop  3. Peek  4. Display  5. Size  6. Is empty?  7. Exit")
    choice = input("Choose: ").strip()
    if choice == "7":
        print("Goodbye!")
        break
    actions.get(choice, lambda: print("Invalid choice."))()
