name = "Sasha"
surname = "Tarasiuk"
group = "IT-32"

print(f"{name} {surname}")

text = name + surname

vowels = "aeiouy"
vowels_count = 0
consonants_count = 0

for char in text:
    if char.lower() in vowels:
        vowels_count += 1
    else:
        consonants_count += 1

print(f"Vowels: {vowels_count}, consonants: {consonants_count}")
print(f"Total letters: {len(text)}")

if vowels_count + consonants_count == len(text):
    print("Check: correct")