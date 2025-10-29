from random import randint
order = [
    "first",
    "second",
    "third"
]

for a in range(3):
    print("Enter your", order[a], "word:")
    word = input()

    if "a" in word:
        word = word.replace("a", chr(randint(33, 37)))
    if "e" in word:
        word = word.replace("e", chr(randint(38, 42)))
    if "i" in word:
        word = word.replace("i", chr(randint(43, 47)))
    if "o" in word:
        word = word.replace("o", chr(randint(58, 61)))
    if "u" in word:
        word = word.replace("u", chr(randint(91, 94)))

    order[a] = word

print("\nEncrypted:")
for b in order:
    print(b)
# type: ignore
