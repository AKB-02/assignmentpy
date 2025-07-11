students = {
    "Alice": [85, 90, 92],
    "Bob": [78, 88, 84],
    "Charlie": [95, 93, 91]
}
def display_averages():
    print("\nAverage marks of each student:")
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        print(f"{name}: {avg:.2f}")
def find_topper():
    highest_avg = 0
    topper = ""
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        if avg > highest_avg:
            highest_avg = avg
            topper = name
    print(f"\nTopper: {topper} with average {highest_avg:.2f}")
def update_marks():
    name = input("\nEnter student name to update marks: ")
    if name in students:
        new_marks = []
        for i in range(1, 4):
            mark = int(input(f"Enter new mark for subject {i}: "))
            new_marks.append(mark)
        students[name] = new_marks
        print(f"Marks updated for {name}.")
    else:
        print("Student not found.")
while True:
    print("\n--- Student Marks Menu ---")
    print("1. Display average marks")
    print("2. Find topper")
    print("3. Update student marks")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_averages()
    elif choice == "2":
        find_topper()
    elif choice == "3":
        update_marks()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")