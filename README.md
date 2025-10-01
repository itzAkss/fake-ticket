# ChangeLog (EN)
- Added a random QR generator with random numbers (tba-XXXXXXX)
- Deleted ticket.py and replaced it by ticketqr.py (Now with name ticket.py)
- Added language selection (ru/en)
# How To Use:
1. Install Termux on [Fdroid](https://f-droid.org/en/packages/com.termux/) or [Play Store](https://play.google.com/store/apps/details?id=com.termux).
2. Copy and Paste in Termux: 
`pkg install git && git clone https://github.com/itzAkss/fake-ticket.git &&
cd fake-ticket && chmod +x setup.sh && ./setup.sh`
3. Wait.
4. Open with `python3 ticket.py`, Select Language, enter info.
5. Done, now you can open it with File manager or with termux-open.
# How to change language
1. Goto config.json
2. Change "language": "ru" to yours (Only 2 languages available)
# Fonts
Only minecraftio.ttf font is supported. If you want to change it, download other font and move it to ~/ticket/ and then rename the font name in ticket.py (9-10-th line)
Also you need to change screenshot "ticket_template.png" to yours
# How to screenshot Ticket in Avtobys:
1. Download a copy of Avtobys (avtobys.apk)
2. Pay your fare and take a screenshot of your ticket.
3. Delete Bus number, route, time and date (brush in white)
4. Move and rename to ticket_template.png

# Изменения (RU)
- Добавлен генератор случайного QR с рандомными числами (tba-XXXXXXX)  
- Удалён `ticket.py`, заменён на `ticketqr.py` (теперь под именем `ticket.py`)  
- Добавлен выбор языка (ru/en)  

# Как использовать
1. Установите Termux на [Fdroid](https://f-droid.org/en/packages/com.termux/) или [Play Store](https://play.google.com/store/apps/details?id=com.termux).  
2. Скопируйте и вставьте в Termux:  
   `pkg install git && git clone https://github.com/itzAkss/fake-ticket.git &&
   cd fake-ticket && chmod +x setup.sh && ./setup.sh`
3. Дождитесь окончания установки.
4. Запустите python3 ticket.py, выберите язык и введите данные.
5. Готово. Теперь вы можете открыть файл через файловый менеджер или командой termux-open.

# Как изменить язык
1. Откройте config.json
2. Измените "language": "ru" на нужный вам (доступно только 2 языка).
# Шрифты
Доступен только шрифт minecraftio.ttf.
Если хотите заменить его:
1. Скачайте другой шрифт и переместите его в ~/ticket/.
2. Переименуйте его в ticket.py (9–10-я строка указывает путь к шрифту).
Также необходимо заменить шаблон скриншота ticket_template.png на свой.
# Как подготовить скриншот билета из Avtobys
1. Скачайте копию Avtobys (avtobys.apk).
2. Оплатите проезд и сделайте скриншот билета.
3. Удалите номер автобуса, маршрут, время и дату (закрасьте белым).
4. Переместите и переименуйте файл в ticket_template.png.
