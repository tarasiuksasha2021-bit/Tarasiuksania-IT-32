birth_year = 2009
height_m = 1.76
full_name = "Oleksandr Tarasiuk"
has_scholarship = True

print(f"birth_year = {birth_year}, type = {type(birth_year)}")
print(f"height_m = {height_m}, type = {type(height_m)}")
print(f"full_name = {full_name}, type = {type(full_name)}")
print(f"has_scholarship = {has_scholarship}, type = {type(has_scholarship)}")

print("\nBefore type changes:")
print(f"birth_year = {birth_year}, type = {type(birth_year)}")
print(f"has_scholarship = {has_scholarship}, type = {type(has_scholarship)}")

birth_year = str(birth_year)
has_scholarship = float(has_scholarship)

print("\nAfter type changes:")
print(f"birth_year = {birth_year}, type = {type(birth_year)}")
print(f"has_scholarship = {has_scholarship}, type = {type(has_scholarship)}")

print("\nTrying birth_year + 1:")
print(birth_year + 1)