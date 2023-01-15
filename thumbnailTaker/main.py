import os
import requests
from bs4 import BeautifulSoup
import time
#------------------------------------

url = input("Enter the URL of the video: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# locate the thumbnail
thumbnail_url = soup.find("meta", property="og:image")["content"]

# bild herunterladen und im ordner speichern
if not os.path.exists("thumbnails"):
    os.mkdir("thumbnails")
i=1
#Ordner speichern
while True:
    if not os.path.exists(f"thumbnails/thumbnail{i}.jpg"):
        response = requests.get(thumbnail_url)
        open(f"thumbnails/thumbnail{i}.jpg", "wb").write(response.content)
        break
    i+=1

print("Image Runtergeladen")
input("Press Enter to exit...")


