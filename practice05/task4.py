a = 7
b = 2
c = len("Tarasiuk")

result_1 = a > b
result_2 = b < c
result_3 = a >= c
result_4 = b >= a
result_5 = a == c
result_6 = 1 <= b <= 12

print(f"a > b = {result_1}, type = {type(result_1)}")
print(f"b < c = {result_2}, type = {type(result_2)}")
print(f"a >= c = {result_3}, type = {type(result_3)}")
print(f"b >= a = {result_4}, type = {type(result_4)}")
print(f"a == c = {result_5}, type = {type(result_5)}")
print(f"1 <= b <= 12 = {result_6}, type = {type(result_6)}")