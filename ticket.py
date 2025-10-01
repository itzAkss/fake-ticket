import os
import json
import random
import qrcode
from PIL import Image, ImageDraw, ImageFont

CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

config = load_config()

if "language" not in config:
    print("Сделано с любовью: itzAkss / Made with love: itzAkss")
    print("Выберите язык / Choose language:")
    print("1. Русский")
    print("2. English")
    choice = input("> ").strip()
    config["language"] = "ru" if choice == "1" else "en"
    save_config(config)

lang = config["language"]

T = {
    "ru": {
        "input_number": "Введите номер транспорта (676AB07): ",
        "input_time": "Введите время оплаты (06:07): ",
        "input_route": "Введите маршрут (№ 67): ",
        "input_date": "Введите дату (06.07.2025): ",
        "qr_text": "QR текст:",
        "done": "✅ Готово:"
    },
    "en": {
        "input_number": "Enter vehicle number (676AB07): ",
        "input_time": "Enter payment time (06:07): ",
        "input_route": "Enter route (№ 67): ",
        "input_date": "Enter date (06.07.2025): ",
        "qr_text": "QR text:",
        "done": "✅ Done:"
    }
}[lang]

number = input(T["input_number"])
time   = input(T["input_time"])
route  = input(T["input_route"])
date   = input(T["input_date"])

rand_num = "".join([str(random.randint(0, 9)) for _ in range(7)])
qr_text = f"tba-{rand_num}"
print(T["qr_text"], qr_text)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)
qr.add_data(qr_text)
qr.make(fit=False)
img_qr = qr.make_image(fill_color="black", back_color="white")

ticket = Image.open("ticket_template.png")
draw = ImageDraw.Draw(ticket)

font_big = ImageFont.truetype("minecraftio.ttf", 42)
font_small = ImageFont.truetype("minecraftio.ttf", 28)

draw.text((250, 535), number, font=font_big, fill="black")
draw.text((288, 1018), time,   font=font_big, fill="black")
draw.text((90, 1274), route,  font=font_small, fill="black")
draw.text((370, 1274), date,   font=font_small, fill="black")

qr = img_qr.resize((320, 320))
ticket.paste(qr, (205, 625))

base_name = "ticket_result"
i = 1
while True:
    filename = f"{base_name}{i:03}.png"
    if not os.path.exists(filename):
        break
    i += 1

ticket.save(filename)
print(f"{T['done']} {filename}")
