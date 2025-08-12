import os
from PIL import Image

def compress_image(input_path, output_path, max_width, max_height, quality=90, format=None):
    with Image.open(input_path) as img:
        img.thumbnail((max_width, max_height))
        save_format = format if format else img.format
        img.save(output_path, format=save_format, quality=quality, optimize=True)

def get_preview(input_path, max_width, max_height, quality=90, format=None):
    with Image.open(input_path) as img:
        img_copy = img.copy()
        img_copy.thumbnail((max_width, max_height))
        save_format = format if format else img.format
        # Save to bytes for preview
        from io import BytesIO
        buf = BytesIO()
        img_copy.save(buf, format=save_format, quality=quality, optimize=True)
        buf.seek(0)
        return buf

def batch_compress(folder_path, output_folder, max_width=1024, max_height=1024, quality=90, format=None):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, filename)
            compress_image(input_path, output_path, max_width, max_height, quality, format)