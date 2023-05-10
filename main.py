import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import time

# Add your values for the Twilio account
account_sid = "your_account_sid"
auth_token = "your_auth_token"
twilio_phone_number = "+1234567890"
my_phone_number = "+1234567890"

# URL for the US passport appointment scheduling
url = "https://waitwhile.com/locations/lakeforestparkp/bookings/add/date"

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the first available slot and extract it
    slot = soup.find("div", class_="step-content").find("div", class_="booking-dates").find("a")
    date = slot.find("div", class_="day").get_text(strip=True)
    time = slot.find("div", class_="time").get_text(strip=True)

    # Create a Twilio client
    client = Client(account_sid, auth_token)

    # Send an SMS notification
    message = f"First available slot is on {date} at {time}"
    client.messages.create(to=my_phone_number, from_=twilio_phone_number, body=message)








