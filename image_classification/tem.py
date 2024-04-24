# Open the image using PIL
from PIL import Image
from io import BytesIO
import base64

def classify_image(image_data):
    # Decode the base64 encoded image data
    image_data = image_data.split(',')[1]
    image_bytes = BytesIO(base64.b64decode(image_data))
    
    # Open the image using PIL
    image = Image.open(image_bytes)
    class_name = "class-1"  # classify_image(image)

    # Return the class name in JSON format
    return class_name