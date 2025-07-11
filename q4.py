stack = []
queue = []

while True:
    print("\n=== Main Menu ===")
    print("1. Stack Operations")
    print("2. Queue Operations")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        while True:
            print("\n--- Stack Operations ---")
            print("1. Push")
            print("2. Pop")
            print("3. Display Stack")
            print("4. Return to Main Menu")

            stack_choice = input("Enter your choice: ")

            if stack_choice == '1':
                item = input("Enter item to push onto stack: ")
                stack.append(item)
                print(f"{item} pushed onto stack.")
            elif stack_choice == '2':
                if stack:
                    item = stack.pop()
                    print(f"{item} popped from stack.")
                else:
                    print("Stack is empty!")
            elif stack_choice == '3':
                print("Current Stack (top -> bottom):", list(reversed(stack)))
            elif stack_choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == '2':
        while True:
            print("\n--- Queue Operations ---")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Display Queue")
            print("4. Return to Main Menu")

            queue_choice = input("Enter your choice: ")

            if queue_choice == '1':
                item = input("Enter item to enqueue: ")
                queue.append(item)
                print(f"{item} enqueued into queue.")
            elif queue_choice == '2':
                if queue:
                    item = queue.pop(0)
                    print(f"{item} dequeued from queue.")
                else:
                    print("Queue is empty!")
            elif queue_choice == '3':
                print("Current Queue (front -> rear):", queue)
            elif queue_choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == '3':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")