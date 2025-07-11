import random
numbers = set()
while len(numbers) < 10:
    rand_num = random.randint(1, 100)
    numbers.add(rand_num)
print("Original set of 10 unique numbers:", numbers)
smallest = min(numbers)
largest = max(numbers)
numbers.remove(smallest)
numbers.remove(largest)
print(f"Removed smallest ({smallest}) and largest ({largest})")
print("Final set:", numbers)