import cv2
import numpy as np

def calculate_rise_distance(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform edge detection using the Canny edge detector
    edges = cv2.Canny(gray, 100, 200)

    # Find contours in the edge image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    max_rise_distance = 0

    # Iterate over the contours
    for contour in contours:
        # Calculate the rise distance for each contour
        contour_area = cv2.contourArea(contour)
        if contour_area > 100:  # Consider only larger contours to avoid noise
            _, _, _, max_loc = cv2.minMaxLoc(gray, mask=np.uint8(edges == 255))
            _, _, _, min_loc = cv2.minMaxLoc(gray, mask=np.uint8(edges == 255), reverse=True)

            rise_distance = abs(max_loc[1] - min_loc[1])  # Calculate the rise distance

            if rise_distance > max_rise_distance:
                max_rise_distance = rise_distance

    return max_rise_distance

# Example usage
image_path = 'path/to/your/image.jpg'

# Load the image
image = cv2.imread(image_path)

# Calculate the rising distance of edges in the image
rising_distance = calculate_rise_distance(image)

print("Max Rise Distance:", rising_distance)
