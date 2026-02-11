import requests
from bs4 import BeautifulSoup

url = "https://www.skru.ac.th/th/" # แทนที่ด้วย URL ของเว็บไซต์ที่ต้องการ
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    #print(soup.prettify()) # แสดงผล HTML ที่จัดรูปแบบแล้ว
    title = soup.find("h1").text
    print("Title:", title)
    links = soup.find_all("a")
    for link in links:
        print(link.get("href"))


else:
    print("Error:", response.status_code)
