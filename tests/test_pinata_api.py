import sys 
import os
# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import necessary functions from pinata_api
from pinata.pinata_api import *

# Example JSON data
scientist_data = {
    "name": "Example Scientist",
    "expertise": "Physics, Quantum Mechanics",
    "personal_bio": "A renowned physicist known for her work in quantum mechanics.",
    "list_of_publications": ["Publication 1", "Publication 2"],
    "institutions_affiliated_with": ["University A", "Institute B"],
    "keywords": ["Physics", "Quantum Mechanics"],
    "link_to_latest_institution_website": "http://example.com",
    "link_to_image": "ipfs_link_to_image"
}

# Pin JSON data
def test_pin_json_to_ipfs():
    json_response = pin_json_to_ipfs(scientist_data, "test_pinata_api")
    print("Pinned JSON:", json_response)
    assert json_response['IpfsHash'] == "QmbCBEQVVJmRLGVmn718yQ8gau3g2dr23TDjJv8vosq7Fo"
    assert json_response['PinSize'] == 416

# Pin JSON file
def test_pin_json_file_to_ipfs():
    file_path = os.path.join(os.path.dirname(__file__), 'HarvardMath.json')
    with open(file_path, 'r') as file:
        json_content = json.load(file)
    json_response = pin_json_to_ipfs(json_content, "math.harvard.edu")
    print("Pinned JSON:", json_response)
    assert json_response['IpfsHash'] == "QmRJjgFkSgoBZGuRnkNybgYS7mAcVTv1fQp4qe3amojSJZ"
    assert json_response['PinSize'] == 3148
# Pin image
def test_pin_image_to_ipfs():
    image_path = os.path.join(os.path.dirname(__file__), 'ada.png')
    image_response = pin_image_to_ipfs(image_path)
    print("Pinned Image:", image_response) 
    assert image_response['IpfsHash'] == "QmboziK1ndCVP6DSpJ4t6CYNLaFXxu8jP9AjZuc6kQewR1"
    assert image_response['PinSize'] == 15259587