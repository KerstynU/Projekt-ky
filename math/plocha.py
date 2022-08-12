import math
 
wall_h = int(input("Výška stěny v m: "))
wall_w = int(input("Šířka stěny v m: "))
coverage = 5
 
def paint_calculator(width, height, cover):
    area = width * height
    number_can = math.ceil(area / 5)
    print(f"Budete potřebovat {number_can} plechovek")
 
paint_calculator(width=wall_w, height=wall_h, cover=coverage)