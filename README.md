# PirateLoot
![Pirate Loot](https://cdn.discordapp.com/attachments/1393114345206190111/1414272755460739235/IMG_20250907_223214.jpg?ex=68bef7a4&is=68bda624&hm=717b81197285a1756fc144cafe3413780c352e274caf7ae0de962a1d74246e63&)


# PirateLoot 🏴‍☠️  # Version 2.0
**PirateLoot** เป็นสคริปต์ Python (web scraping) — ดึงข้อความ, ลิงก์ และรูปภาพ จากหน้าเว็บเป้าหมายแล้วเซฟลงโฟลเดอร์ `Output/`

---

## 🇬🇧 Quick summary (English)
PirateLoot is a small Python web-scraper that extracts page text, links, and images from a target URL, saves them under `Output/<domain>/` and optionally downloads images to `Output/<domain>/Img`.

---

## 🧭 ฟีเจอร์ / Features
| Option                         | Description                                   | Default        |
|--------------------------------|-----------------------------------------------|----------------|
| `-help`, `--help-menu`         | Show this help menu    โชว้เมนูช่วยเหลือ             |                |
| `-v`, `--version`              | Show Version   โชว์เวอร์ชั่น                        |                |
| `-u`                           | URL   ลิ้งเว็บ                                    |                |
| `-to`, `--time-out`            | Time out                                      |     10         |
| `-f`, `--fast`                 | Fast Mode   โหมดเร็ว                            | Normal         |
| Mode  โหมด                     |                                               |                |
| `--save-img`                   | Save img as a file  บันทึกรูปเป็นไฟล์               |                |


---

## 🛠️ ความต้องการระบบ / Requirements
- โมดูล Python (รายชื่อใน `requirements.txt` ด้านล่าง)

---

## การใช้งาน
`python pirateloot.py -u "https://example.com"`

## Done!
