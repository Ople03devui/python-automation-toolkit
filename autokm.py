import pyautogui
import time

# เลื่อนเมาส์ไปยังตำแหน่ง (100, 100)
pyautogui.moveTo(100, 100, duration=1)

# คลิกเมาส์
pyautogui.click()

# พิมพ์ข้อความ
pyautogui.typewrite("Hello, world!")

# กดปุ่ม Enter
pyautogui.press("enter")

# รอ 2 วินาที
time.sleep(2)

# ดับเบิ้ลคลิก
pyautogui.doubleClick()
