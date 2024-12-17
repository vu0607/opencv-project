import requests

def download_image(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)
