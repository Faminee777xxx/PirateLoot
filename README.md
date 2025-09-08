# PirateLoot
![Pirate Loot](https://cdn.discordapp.com/attachments/1393114345206190111/1414272755460739235/IMG_20250907_223214.jpg?ex=68bef7a4&is=68bda624&hm=717b81197285a1756fc144cafe3413780c352e274caf7ae0de962a1d74246e63&)


# PirateLoot 🏴‍☠️  # Version 2.0
**PirateLoot** เป็นสคริปต์ Python (web scraping) — ดึงข้อความ, ลิงก์ และรูปภาพ จากหน้าเว็บเป้าหมายแล้วเซฟลงโฟลเดอร์ `Output/`

---

## 🇬🇧 Quick summary (English)
PirateLoot is a small Python web-scraper that extracts page text, links, and images from a target URL, saves them under `Output/<domain>/` and optionally downloads images to `Output/<domain>/Img`.

---

## 🧭 ฟีเจอร์ / Features
- ดึงข้อความ (text) ทั้งหมดจากหน้าเว็บและบันทึกเป็นไฟล์ .txt  
- ดึงลิงก์ (`<a href="">`) ทั้งหมด  
- ดึง `<img src="">` ทั้งหมด และแปลง relative path → absolute URL (ด้วย `urljoin`)  
- ตัวเลือก `--save-img` เพื่อบันทึกรูปภาพลงเครื่อง  
- โฟลเดอร์ผลลัพธ์: `Output/<domain>/` และรูปอยู่ใน `Output/<domain>/Img`  
- แสดง banner, ข้อความสี และ log สไตล์ Pirate

---

## 🛠️ ความต้องการระบบ / Requirements
- โมดูล Python (รายชื่อใน `requirements.txt` ด้านล่าง)

---

## 📦 requirements.txt
