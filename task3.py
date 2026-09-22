about = "I study Python at college and I enjoy web development"

words = about.split()

print("Кількість слів:", len(words))

longest_word = max(words, key=len)
print("Найдовше слово:", longest_word)

print("Зворотний порядок:", " ".join(words[::-1]))

a_count = about.lower().count("a")
print("Кількість літер 'a':", a_count)

print("З великої літери:", about.title())

print("Заміна пробілів:", about.replace(" ", "_"))


def is_palindrome(text):
    cleaned = "".join(text.lower().split())
    return cleaned == cleaned[::-1]


print("Ім'я є паліндромом:", is_palindrome("Oleksandr"))
print("Never odd or even є паліндромом:", is_palindrome("Never odd or even"))


def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


day = 7
name_to_encrypt = "Oleksandr"

encrypted = caesar_encrypt(name_to_encrypt, day)
decrypted = caesar_decrypt(encrypted, day)

print("День народження:", day)
print("Ім'я:", name_to_encrypt)
print("Зашифроване ім'я:", encrypted)
print("Розшифроване ім'я:", decrypted)