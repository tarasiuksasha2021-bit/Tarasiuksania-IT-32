import qrcode

print("Oleksandr Tarasiuk, IT-32")

text = "Oleksandr Tarasiuk, IT-32, oleksandr.tarasiuk@example.com"

image = qrcode.make(text)
image.save("contact.png")

print("saved: contact.png")