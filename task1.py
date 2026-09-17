name = "Oleksandr"
surname = "Tarasiuk"
group = "IT-32"
city = "Tsuman"
birth_year = 2009
hobbies = ["programming", "gaming", "music"]

me = {
    "name": name,
    "surname": surname,
    "group": group,
    "city": city,
    "birth_year": birth_year,
    "hobbies": hobbies
}

print("My information:")

for key, value in me.items():
    print(f"{key}: {value}")

print("\nKeys:", list(me.keys()))
print("Number of pairs:", len(me))

print("\nGroup:", me["group"])
print("Email:", me.get("email", "unknown"))

me["email"] = "2024.tarasiuk.oleksandr@ktbp.net.ua"

me["city"] = "Lutsk"

removed_year = me.pop("birth_year")

print("\nRemoved birth year:", removed_year)

print("\nDictionary after changes:")

for key, value in me.items():
    print(f"{key}: {value}")

print("\nIs phone in dictionary?", "phone" in me)