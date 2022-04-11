from bs4 import BeautifulSoup
import requests
import shutil

if __name__ == "__main__":

    reddit_url = "https://www.reddit.com/r/shittyHDR/new/"
    user_agent =  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0"
    download_path = "/Users/breakthealgo/Downloads/"

    headers = {
        'User-agent':
            user_agent
    }

    page =  requests.get(reddit_url, headers=headers)

    soup = BeautifulSoup(page.text, "html.parser")

    images  = soup.find_all("img", {"alt"  : "Post image"})

    image_url = images[0]['src']

    filename = download_path + "my_image.jpg"

    image_request = requests.get(image_url, stream=True)

    if image_request.status_code == 200:
        image_request.raw.decode_content = True

    with open(filename, 'wb') as file:
        shutil.copyfileobj(image_request.raw, file)

    print("Finished downloading image")
