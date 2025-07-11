sentence = input("Enter a sentence: ")
vowels = "aeiou"
unique_vowels = set()
for char in sentence.lower():
    if char in vowels:
        unique_vowels.add(char)
print("Unique vowels used:", unique_vowels)