text = input("Enter some text: ")
frequency = {}
for char in text:
    if char.isalnum():
        char = char.lower()
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
print("\nCharacter Frequencies:")
for char in frequency:
    print(f"{char} : {frequency[char]}")