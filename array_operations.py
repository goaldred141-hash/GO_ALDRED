"""Array (Python list) operations: traverse, insert, delete, search, update, sort."""

data = []


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def traverse():
    if not data:
        print("Array is empty.")
        return
    for i, v in enumerate(data):
        print(f"  index {i}: {v}")


def insert():
    value = input("Value to insert: ")
    pos = read_int(f"Position (0 to {len(data)}): ")
    if 0 <= pos <= len(data):
        data.insert(pos, value)
        print(f"Inserted '{value}' at index {pos}.")
    else:
        print("Invalid position.")


def delete():
    if not data:
        print("Array is empty.")
        return
    pos = read_int(f"Position to delete (0 to {len(data) - 1}): ")
    if 0 <= pos < len(data):
        print(f"Deleted '{data.pop(pos)}'.")
    else:
        print("Invalid position.")


def search():
    value = input("Value to search: ")
    found = [i for i, v in enumerate(data) if v == value]
    if found:
        print(f"'{value}' found at index/indices: {found}")
    else:
        print(f"'{value}' not found.")


def update():
    if not data:
        print("Array is empty.")
        return
    pos = read_int(f"Position to update (0 to {len(data) - 1}): ")
    if 0 <= pos < len(data):
        data[pos] = input("New value: ")
        print("Updated.")
    else:
        print("Invalid position.")


def sort():
    try:
        data.sort(key=float)
        print("Sorted numerically.")
    except ValueError:
        data.sort()
        print("Sorted alphabetically.")


actions = {"1": traverse, "2": insert, "3": delete, "4": search, "5": update, "6": sort}

while True:
    print("\n=== ARRAY OPERATIONS ===")
    print("1. Traverse  2. Insert  3. Delete  4. Search  5. Update  6. Sort  7. Exit")
    choice = input("Choose: ").strip()
    if choice == "7":
        print("Goodbye!")
        break
    actions.get(choice, lambda: print("Invalid choice."))()
