import os
import random
import qrcode
from PIL import Image, ImageDraw, ImageFont

# === 1. Ввод данных ===
number = input("Введите номер транспорта: ")   # например 837BE04
time   = input("Введите время оплаты: ")       # например 15:30
route  = input("Введите маршрут: ")            # например №15
date   = input("Введите дату: ")               # например 21.09.2025

# === 2. Генерация текста для QR ===
rand_num = "".join([str(random.randint(0, 9)) for _ in range(7)])
qr_text = f"tba-{rand_num}"
print("QR текст:", qr_text)

# === 3. Генерация QR ===
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=8,
    border=2,
)
qr.add_data(qr_text)
qr.make(fit=True)
img_qr = qr.make_image(fill_color="black", back_color="white")

# === 4. Загружаем шаблон ===
ticket = Image.open("ticket_template.png")
draw = ImageDraw.Draw(ticket)

# === 5. Шрифты ===
font_big = ImageFont.truetype("minecraftio.ttf", 42)
font_small = ImageFont.truetype("minecraftio.ttf", 28)

# === 6. Подстановка текста ===
# (подбери координаты под свой шаблон!)
draw.text((250, 535), number, font=font_big, fill="black")
draw.text((288, 1018), time,   font=font_big, fill="black")
draw.text((90, 1274), route,  font=font_small, fill="black")
draw.text((375, 1274), date,   font=font_small, fill="black")

# === 7. Вставка QR на картинку ===
qr = img_qr.resize((320, 320))  # подгони размер
ticket.paste(qr, (210, 625))    # координаты центра QR

# === 8. Автоматическое имя файла ===
base_name = "ticket_result"
i = 1
while True:
    filename = f"{base_name}{i:03}.png"
    if not os.path.exists(filename):
        break
    i += 1

# === 9. Сохраняем ===
ticket.save(filename)
print(f"✅ Готово: {filename}")
