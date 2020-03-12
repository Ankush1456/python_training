from flask import Flask, request

from pymessenger.bot import Bot


app = Flask("hello")

VERIFY_TOKEN = "1234567890"
ACCESS_TOKEN = "EAAC1SZAZAxj5wBAFqaZCVEXzqvLzvMW1q7KF8gFbUSrXWe36fixXcU9OzmJZAZAyvd3qyt8PZBsZAUMWAthoS2UjGu2gEyHJHf0ZBC6l7UwIT6ddNGmuACBvIydzr3NeHnaLey51L9PVVliuZCol9OZBHaz9qZC5fGXrUb0pnzIwalZBAYnR0gHVGbriBgihnvkCS48ZD"

pybot= Bot(ACCESS_TOKEN)

@app.route("/check/", methods=["GET"])
def sayhi():
    return "working"


@app.route("/callback/", methods=["GET"])
def get_callback():
    if VERIFY_TOKEN == request.args.get("hub.verify_token"):
        return request.args.get("hub.challenge")
    else:
        return "not working"


@app.route("/callback/", methods=["POST"])
def post_callback():
    output = request.get_json()

    for entry in output.get("entry"):
        if "messaging" in entry:
            for messaging in entry.get("messaging"):
                sender = messaging.get("sender").get("id")
                recipient = messaging.get("recipient").get("id")

                text = "You sent an attachment"

                if "text" in messaging.get("message"):
                    text = messaging.get("message").get("text")

                print(sender, recipient, text)

                pybot.send_text_message(sender, text)
                pybot.send_image_url(sender,r"https://images.pexels.com/photos/1328545/pexels-photo-1328545.jpeg")


    return "done"

app.run()