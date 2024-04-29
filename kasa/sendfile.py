import requests

# Define the URL of the Flask API endpoint
url = 'https://8205-79-98-115-6.ngrok-free.app'

# Specify the file path of the SQLite database
file_path = r'C:\Users\User\store_manager\db.sqlite3'

# Create a dictionary containing the file to be sent
files = {'file': open(file_path, 'rb')}

# Send a POST request with the file to the Flask API
response = requests.post(url, files=files)


