import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

# Pinata API credentials
PINATA_JWT_TOKEN = os.getenv("PINATA_JWT_TOKEN")

# IPFS is immutable, the IpfsHash is calculated based on the content of the file
# Thus, the Pin will return 200 but with 'isDuplicate': True
# The object on IPFS will not be updated even if we attempt to change the file name 
# The new object will be created once the content of the file changes
# By the time the new file name will take effect.
# Include the timestamp in the file name to distinguish between different versions of the same file

# Function to pin JSON object to IPFS
def pin_json_to_ipfs(json_content, file_name):
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    headers = {
        "Authorization": f"Bearer {PINATA_JWT_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "pinataOptions": {"cidVersion": 0},
        "pinataMetadata": {"name": f"{file_name}_{now}.json"},
        "pinataContent": json_content
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# Function to pin image to IPFS
def pin_image_to_ipfs(image_path):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    headers = {
        "Authorization": f"Bearer {PINATA_JWT_TOKEN}"
    }
    with open(image_path, 'rb') as file:
        files = {
            "file": file
        }
        filename = os.path.basename(file.name)
        filename_with_timestamp = f"{os.path.splitext(filename)[0]}_{now}{os.path.splitext(filename)[1]}"
        metadata = {
            "name": filename_with_timestamp,
            "pinataOptions": {"cidVersion": 0},
            "pinataMetadata": {"name": filename_with_timestamp},
        }
        data = {
            "pinataMetadata": json.dumps(metadata),
        }
        response = requests.post(url, headers=headers, data=data, files=files)
    return response.json()
