import requests
import io
import matplotlib.pyplot as plt
from PIL import Image
from google.colab import files

DEEPAI_API_KEY = '2725e670-4d96-43d7-93ba-77760ea5f225'

# Step 3: Function to apply colorization effect
def apply_colorization_effect(image_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()

    response = requests.post(
        'https://api.deepai.org/api/colorizer',  # Using colorization model for testing
        files={'image': image_data},
        headers={'api-key': DEEPAI_API_KEY}
    )

    if response.status_code == 200:
        return response.json()['output_url']
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

  ploaded = files.upload()

# Step 5: Apply the cartoon effect
image_path = list(uploaded.keys())[0]  # Get the name of the uploaded file
cartoon_url = apply_cartoon_effect(image_path)

if cartoon_url:
    print("Cartoonified Image URL:", cartoon_url)
    plt.imshow(Image.open(io.BytesIO(requests.get(cartoon_url).content)))
    plt.axis('off')  # Turn off axis labels
    plt.show()

# Step 1: Install OpenCV
!pip install opencv-python
!pip install opencv-python-headless  # Needed for Google Colab

# Step 2: Upload an image
from google.colab import files

uploaded = files.upload()
image_path = list(uploaded.keys())[0]  # Get the name of the uploaded file

# Step 3: Import OpenCV and apply the cartoon effect
import cv2
import numpy as np
import matplotlib.pyplot as plt

def cartoonize_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur
    gray = cv2.medianBlur(gray, 5)

    # Detect edges
    edges = cv2.adaptiveThreshold(gray, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, blockSize=9,
                                  C=2)

    # Apply bilateral filter to reduce color palette
    color = cv2.bilateralFilter(img, d=9, sigmaColor=300, sigmaSpace=300)

    # Combine edges with color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

# Apply the cartoon effect
cartoon_image = cartoonize_image(image_path)

# Display the result
plt.imshow(cv2.cvtColor(cartoon_image, cv2.COLOR_BGR2RGB))
plt.axis('off')  # Turn off axes
plt.show()

import requests

# Replace 'your_api_key' with your actual DeepAI API key
api_key = 'fd3c5526-0dc9-42e0-a00e-1efe9615869f'

# Upload an image
uploaded = files.upload()
image_path = list(uploaded.keys())[0]  # Get the uploaded file's name

# Make a POST request to the DeepAI Cartoonizer API
response = requests.post(
    "https://api.deepai.org/api/toonify",
    files={
        'image': open(image_path, 'rb'),
    },
    headers={'api-key': api_key}
)

# Check for response
if response.status_code == 200:
    # Get image URL
    output_url = response.json().get('output_url')
    print(f'Cartoonized Image URL: {output_url}')
else:
    print(f"Error: {response.status_code}, {response.text}")


import cv2

def create_avatar(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (200, 200))
    # Circular mask
    mask = np.zeros((200, 200), dtype=np.uint8)
    cv2.circle(mask, (100, 100), 100, 255, -1)
    img = cv2.bitwise_and(img, img, mask=mask)
    cv2.imwrite('avatar.png', img)
