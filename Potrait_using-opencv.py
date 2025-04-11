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

