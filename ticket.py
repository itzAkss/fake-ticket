from PIL import Image, ImageDraw, ImageFont
import os
#
img = Image.open("ticket_template.png")
draw = ImageDraw.Draw(img)

#
font_big = ImageFont.truetype("minecraftio.ttf", 42)
font_small = ImageFont.truetype("minecraftio.ttf", 30)
#
print("Made by itzAkss")
print(" ")
print(img.size)
print(" ")
number = input("Номер транспорта (123AC04): ")   # 837BE04
time   = input("Время оплаты (12:55): ")       # 15:30
route  = input("Маршрут (№ 56): ")            # №15
date   = input("Дата (22.09.2025): ")               # 21.09.2025

base_name = "ticket_result"

i = 1
while True:
    filename = f"{base_name}{i:03}.png"  # ticket_result001.png
    if not os.path.exists(filename):
        break
    i += 1

#
draw.text((250, 535), number, font=font_big, fill="black")
draw.text((288, 1018), time,   font=font_big, fill="black")
draw.text((90, 1274), route,  font=font_small, fill="black")
draw.text((375, 1274), date,   font=font_small, fill="black")

#
img.save(filename)
print(f"✅ Готово: {filename}")
print(f"Открыть с помощью termux-open ~/ticket/{filename}")
