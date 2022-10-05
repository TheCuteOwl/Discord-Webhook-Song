import requests #dependency
import time
url = "Webhook"
count = 0
while True:
    with open ("lyrics.txt") as f:
        Lines = f.readlines()
        for line in Lines:
            count += 1
            print("Line{}: {}".format(count, line.strip()))

            data = {
                "username": "Song Lyrics",
                "avatar_url": "https://images.emojiterra.com/twitter/v13.1/512px/1f3b6.png",
                "content" : line,
            }


            result = requests.post(url, json = data)

            try:
                result.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print(err)
            else:
                print("Payload delivered successfully, code {}.".format(result.status_code))
            time.sleep(3)


