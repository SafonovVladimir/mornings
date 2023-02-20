def rgb_to_hex(r: int, g: int, b: int) -> str:
    hex_r = hex(min(255, max(r, 0)))[2:]
    hex_g = hex(min(255, max(g, 0)))[2:]
    hex_b = hex(min(255, max(b, 0)))[2:]

    return "".join((hex_r.zfill(2), hex_g.zfill(2), hex_b.zfill(2))).upper()

print(rgb_to_hex(255, 255, 255))  # # повертає "FFFFFF"
print(rgb_to_hex(255, 255, 300))  # # повертає "FFFFFF"
print(rgb_to_hex(1, 2, 3))  # # повертає "000000"
print(rgb_to_hex(-20, 275, 125))  # повертає "00FF7D"
