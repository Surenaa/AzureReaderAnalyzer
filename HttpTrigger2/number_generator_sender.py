import requests
import random

url = "https://azureanalyzer.azurewebsites.net"

def send_random_number():
    random_number = random.randint(1, 100)
    data = {"number": random_number}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f"Random number {random_number} sent successfully!")
    else:
        print("Failed to send the random number.")

# Number of random numbers to send
num_numbers = 10

for _ in range(num_numbers):
    send_random_number()