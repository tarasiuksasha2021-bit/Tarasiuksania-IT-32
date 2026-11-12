
import math
import sys

print("Oleksandr Tarasiuk, ІТ-32")

# Розміри кімнати
LENGTH = 4.0
WIDTH = 3.0
HEIGHT = 2.7

# Двері та вікно
DOOR_WIDTH = 0.9
DOOR_HEIGHT = 2.0
WINDOW_WIDTH = 1.4
WINDOW_HEIGHT = 1.5

# Плитка
TILE_LENGTH = 0.3
TILE_WIDTH = 0.3
TILE_PRICE = 42.30

floor_area = LENGTH * WIDTH
wall_area = 2 * (LENGTH + WIDTH) * HEIGHT
wall_area -= DOOR_WIDTH * DOOR_HEIGHT
wall_area -= WINDOW_WIDTH * WINDOW_HEIGHT

floor_diagonal = math.hypot(LENGTH, WIDTH)
room_diagonal = math.dist(
    (0, 0, 0),
    (LENGTH, WIDTH, HEIGHT)
)

tile_area = TILE_LENGTH * TILE_WIDTH
tiles_exact = floor_area / tile_area

print(f"room: {LENGTH} x {WIDTH} x {HEIGHT} m")
print(f"floor area: {floor_area:.2f} m2")
print(f"wall area: {wall_area:.2f} m2")
print(f"floor diag: {floor_diagonal:.2f} m")
print(f"room diag: {room_diagonal:.2f} m")

print(f"\ntiles exact: {tiles_exact:.2f}")
print(f"round: {round(tiles_exact)}")
print(f"floor: {math.floor(tiles_exact)}")
print(f"ceil: {math.ceil(tiles_exact)}")

tiles_to_buy = math.ceil(tiles_exact * 1.10)
print(f"tiles to buy: {tiles_to_buy}")

paint = wall_area * 2 / 10
cans = math.ceil(paint / 2.5)

print(f"paint: {paint:.2f} l")
print(f"paint cans: {cans}")

cost_mul = tiles_to_buy * TILE_PRICE
cost_sum = math.fsum(TILE_PRICE for _ in range(tiles_to_buy))

print(f"\ntiles cost: {cost_mul:.2f} UAH")
print(f"sum == mul: {cost_sum == cost_mul}")
print(f"isclose: {math.isclose(cost_sum, cost_mul)}")
print(f"difference: {abs(cost_sum - cost_mul)}")
