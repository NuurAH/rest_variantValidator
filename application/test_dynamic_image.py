import requests
from PIL import Image
from io import BytesIO

#Using a direct image from tutorial
image_url = "https://raw.githubusercontent.com/i3hsInnovation/resources/master/images/puss_in_boots.jpg"

#Fetch the image
response = requests.get(image_url)

if response.status_code == 200:
    #Load image directly into memory without saving to disk
    img = Image.open(BytesIO(response.content))
    img.show()
else:
    print(f"Failed to retrieve image. Status code: {response.status_code}")

