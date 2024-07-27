import cloudinary
import cloudinary.uploader
import cloudinary.api
import os

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET_KEY')
)

def upload_photo_to_cloudinary(file):
    """Завантаження фото до Cloudinary"""
    result = cloudinary.uploader.upload(file.file)
    return result['url']

def delete_photo_from_cloudinary(photo_url):
    """Видалення фото з Cloudinary"""
    public_id = photo_url.split('/')[-1].split('.')[0]
    cloudinary.uploader.destroy(public_id)


