from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/wa", methods=["POST"])
def bot():
    user_msg = request.values.get('Body', '').lower()
 
    # creating object of MessagingResponse
    resp = MessagingResponse()
    msg = resp.message()

    msg.body("ChatGPT response")

    # msg.media() for adding media

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)