from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

def resize_image(image_file, max_size=(300, 300)):
    img = Image.open(image_file)
    img.thumbnail(max_size, Image.ANTIALIAS)
    output_buffer = BytesIO()
    img.save(output_buffer, format='JPEG')  
    resized_image = InMemoryUploadedFile(output_buffer, None, 'resized_image.jpg', 'image/jpeg',  output_buffer.tell(), None)
    return resized_image
