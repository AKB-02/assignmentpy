master = set(input("Enter all student roll numbers (space-separated): ").split())
cricket = set(input("Enter roll numbers of students who play cricket: ").split())

football = set(input("Enter roll numbers of students who play football: ").split())

both = cricket & football
print("\n(a) Students who play both sports:", both if both else "None")
only_one = cricket ^ football
print("(b) Students who play only one sport:", only_one if only_one else "None")

neither = master - (cricket | football)
print("(c) Students who play neither sport:", neither if neither else "None")