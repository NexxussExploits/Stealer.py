import requests

def get_user_info(user_id, webhook_url):
    url = f"https://discord.com/api/v9/users/{user_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        send_data_to_webhook(user_data, webhook_url)
    else:
        print("Failed to retrieve user information.")

def send_data_to_webhook(user_data, webhook_url):
    response = requests.post(webhook_url, json=user_data)
    
    if response.status_code == 200:
        print("User information sent successfully to the webhook!")
    else:
        print("Failed to send user information to the webhook.")

# Replace WEBHOOK_HERE with the actual webhook URL
webhook_url = "WEBHOOK_HERE"

# Prompt for the user ID to retrieve their information
user_id = input("Enter the user ID: ")

# Call the function to get and send the user information
get_user_info(user_id, webhook_url)
