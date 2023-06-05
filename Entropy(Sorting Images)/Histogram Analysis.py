import cv2
import numpy as np
from pathlib import Path
from scipy.stats import entropy

def get_entropy_of_hue(image):
    """
    Calculates the entropy of the hue values of an image.

    Args:
        image: A NumPy array representing an image.

    Returns:
        The entropy of the hue values of the image.
    """

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue_values = hsv_image[:, :, 0]
    entropy_of_hue = entropy(hue_values, base=2)
    return entropy_of_hue

def get_best_image_by_histogram(images):
    best_image = None
    best_entropy = -1

    for image in images:
        entropy = get_entropy_of_hue(image)

        if entropy > best_entropy:
            best_entropy = entropy
            best_image = image

    return best_image

def main():
    # Get the path to the folder containing the images.
    folder_path = Path('C:/Users/USER/Downloads/Youghurt and granola')

    # Get all the images in the folder.
    images = [cv2.imread(str(file)) for file in folder_path.glob("*.jpg")]

    # Find the image with the best entropy using histogram analysis.
    best_image = get_best_image_by_histogram(images)

    # Display the best image.
    cv2.imshow("Best Image", best_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
