import cv2
import numpy as np
import os

# function to calculate clearness of the image
def calculate_entropy(image):
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    histogram /= histogram.sum()
    non_zero_bins = histogram[histogram > 0]
    entropy = -np.sum(non_zero_bins * np.log2(non_zero_bins))
    return entropy

# function to calculate 
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

# Example usage
image_directory = 'C:/Users/USER/Downloads/Youghurt and granola'  # Replace with the directory containing your images
scores = calculate_detail_scores(image_directory)

for file_name, score in scores:
    print(f"{file_name}: {score}")