import cv2
import numpy as np
import os

# Function to calculate the entropy of an image
def calculate_entropy(image):
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])#calculates the histogram of the image
    histogram /= histogram.sum()
    non_zero_bins = histogram[histogram > 0]
    entropy = -np.sum(non_zero_bins * np.log2(non_zero_bins))#Calculates the entropy of the image
    return entropy

# Function to calculate detail scores for images in a directory
def calculate_detail_scores(image_dir):
    image_files = os.listdir(image_dir)
    detail_scores = []

    for file_name in image_files:
        file_path = os.path.join(image_dir, file_name)
        image = cv2.imread(file_path, 0)  # Load image in grayscale
        entropy = calculate_entropy(image)
        detail_scores.append((file_name, entropy))

    detail_scores.sort(key=lambda x: x[1], reverse=True)
    return detail_scores

# Usage
image_directory = 'C:/Users/USER/Downloads/Youghurt and granola'  # Replace with the directory containing your images
scores = calculate_detail_scores(image_directory)

# Check if any images are present
if len(scores) > 0:
    file_name, score = scores[0]  # Retrieve the image with highest detail score
    print(f"Highest detail score: {score} - Image: {file_name}")
else:
    print("No images found in the directory.")