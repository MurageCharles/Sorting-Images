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
    entropy_of_hue = entropy(hue_values.flatten(), base=2)
    return entropy_of_hue




    divided_images = {
        'entropy': [],
        # Add more divisions based on other hue characteristics
    }

    for image in images:
        entropy_value = get_entropy_of_hue(image)
        divided_images['entropy'].append((entropy_value, image))
        # Add more divisions based on other hue characteristics

    return divided_images


def get_best_image_entropy(images):
    """
    Determines the image with the best hue using the entropy.

    Args:
        images: A list of tuples containing entropy value and corresponding images.

    Returns:
        The image with the best hue based on entropy.
    """

    best_image = None
    best_entropy = -1

    for entropy_value, image in images:
        if entropy_value > best_entropy:
            best_entropy = entropy_value
            best_image = image

    return best_image


def main():
    # Get the path to the folder containing the images.
    folder_path = Path('C:/Users/USER/Downloads/Youghurt and granola')

    # Get all the images in the folder.
    images = [cv2.imread(str(file)) for file in folder_path.glob("*.jpg")]

    # Divide the images based on entropy
    divided_images = divide_images(images)

    # Find the image with the best hue based on entropy
    best_image_entropy = get_best_image_entropy(divided_images['entropy'])

    # Display the best image based on entropy
    cv2.imshow("Best Image (Entropy)", best_image_entropy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
