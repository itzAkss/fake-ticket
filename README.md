# fake-ticket
Faking AvtoBys tickets.
# How To Use:
1.Install Termux on [Fdroid](https://f-droid.org/en/packages/com.termux/) or [Play Store](https://play.google.com/store/apps/details?id=com.termux).
2. Copy and Paste in Termux: 
`pkg install git && git clone https://github.com/itzAkss/fake-ticket.git &&
cd fake-ticket && chmod +x setup.sh
./setup.sh`
3. Wait.
4. Open with `python3 ticket.py`, Enter info.
5. Done, now you can open it with File manager or with termux-open.
# Fonts
Only minecraftio.ttf font is supported. If you want to change it, download other font and move it to ~/ticket/ and then rename the font name in ticket.py (9-10-th line)
Also you need to change screenshot "ticket_template.png" to yours
# How to screenshot Ticket in Avtobys:
1. Download a copy of Avtobys (avtobys.apk)
2. Pay your fare and take a screenshot of your ticket.
3. Delete Bus number, route, time and date (brush in white)
4. Move and rename to ticket_template.png
