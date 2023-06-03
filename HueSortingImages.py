import os
import numpy as np
from PIL import Image
import math

class ImageData:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.hue = 0.0
        self.mean_hue = 0.0
        self.median_hue = 0.0
        self.std_deviation_hue = 0.0
        self.entropy_hue = 0.0
    
    def calculate_hue_statistics(self):
        image_data = np.array(self.image.convert("RGBA"))
        red, green, blue, alpha = image_data[:, :, 0], image_data[:, :, 1], image_data[:, :, 2], image_data[:, :, 3]
        
        # Normalize color channels
        red = red / 255.0
        green = green / 255.0
        blue = blue / 255.0
        
        # Calculate hue values
        hue_values = np.zeros_like(red)
        mask = (alpha > 0)
        np.putmask(hue_values, mask, np.arctan2(np.sqrt(3) * (green - blue), 2 * red - green - blue) / (2 * math.pi) % 1)
        
        # Calculate statistics
        self.hue = np.mean(hue_values)
        self.mean_hue = np.mean(np.sort(hue_values, axis=None))
        self.median_hue = np.median(np.sort(hue_values, axis=None))
        self.std_deviation_hue = np.std(np.sort(hue_values, axis=None))
        self.entropy_hue = self.calculate_entropy(hue_values)
    
    def calculate_entropy(self, values):
        values_flat = values.flatten()
        hist, _ = np.histogram(values_flat, bins=256, range=(0, 1))
        hist = hist / values_flat.size
        entropy = -np.sum(hist * np.log2(hist + np.finfo(float).eps))
        return entropy

# Folder path containing the images
folder_path = 'C:/Users/USER/Downloads/Youghurt and granola'

# Get all image files from the folder
image_files = [file for file in os.listdir(folder_path) if file.lower().endswith((".png", ".jpg", ".jpeg"))]

# Create ImageData instances for each image
images = [ImageData(os.path.join(folder_path, image_file)) for image_file in image_files]

# Calculate hue statistics for each image
for image in images:
    image.calculate_hue_statistics()

# Find the image with the best hue using a specific test
best_image = max(images, key=lambda img: img.mean_hue)
best_image_path = os.path.join(folder_path, image_files[images.index(best_image)])
print("Best Image Found:", best_image_path)