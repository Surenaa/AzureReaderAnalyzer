import random
import requests

url = "https://azureanalyzer.azurewebsites.net"

def send_random_number():
    random_number = random.randint(1, 100)
    payload = {'number': random_number}

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(f"Successfully sent random number: {random_number}")
        else:
            print("Failed to send random number.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")

# Send 10 random numbers
for _ in range(10):
    send_random_number()