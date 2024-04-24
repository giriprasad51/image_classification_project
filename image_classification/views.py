
# image_classification/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from io import BytesIO
import base64
from ..inference import classify_image


def classification_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        # Handle saving the image file here
        # For simplicity, we'll just save it to the media directory
        with open('media/uploaded_image.jpg', 'wb') as f:
            for chunk in image_file.chunks():
                f.write(chunk)
        image_url = '/media/uploaded_image.jpg'
        return render(request, 'image_upload/upload_image.html', {'image_url': image_url})
    return render(request, 'image_upload/upload_image.html')



@csrf_exempt
def get_class_name_view(request):
    if request.method == 'POST':
        # Get the image data from the POST request
        image_data = request.POST.get('image_data')

        # Process the image data and obtain the class name
        # Replace this with your actual logic to classify the image
        image_data = image_data.split(',')[1]
        image_data = BytesIO(base64.b64decode(image_data))
        class_name = classify_image(image_data)

        # Return the class name in JSON format
        return JsonResponse({'class_name': class_name, 'image_data': image_data})

    # Return an error response if the request method is not POST
    return JsonResponse({'error': 'Invalid request'})