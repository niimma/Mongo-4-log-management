import requests
import random
import time

# Function to generate random logs
def generate_log():
    # Randomly select an endpoint and action
    endpoints = ['/api/log/', '/api/register/', '/api/login/']
    actions = ['create_log', 'register_user', 'login_user']
    endpoint = random.choice(endpoints)
    action = random.choice(actions)
    
    # Headers (replace 'your_token' with a valid token if needed)
    headers = {
        'Authorization': 'Bearer your_token'  # Only needed for endpoints requiring authentication
    }

    # Data for requests
    data = {
        'action': action,
        'username': f'user_{random.randint(1, 100)}',
        'password': 'password123'
    }

    # Make the request
    try:
        response = requests.post(f'http://127.0.0.1:8000{endpoint}', json=data, headers=headers)
        print(f"{action} -> Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Generate logs continuously
while True:
    generate_log()
    time.sleep(random.uniform(0.5, 2))  # Wait a random time between 0.5 and 2 seconds
