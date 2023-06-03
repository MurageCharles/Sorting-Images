import cv2
import numpy as np
from pathlib import Path

def get_standard_deviation_of_hue(image):
    """
    Calculates the standard deviation of the hue values of an image.

    Args:
        image: A NumPy array representing an image.

    Returns:
        The standard deviation of the hue values of the image.
    """

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue_values = hsv_image[:, :, 0]
    standard_deviation_of_hue = np.std(hue_values)
    return standard_deviation_of_hue


def divide_images(images):
    """
    Divides the images based on different hue characteristics.

    Args:
        images: A list of NumPy arrays representing images.

    Returns:
        A dictionary containing the divided images based on different hue characteristics.
    """

    divided_images = {
        'standard_deviation': [],
        # Add more divisions based on other hue characteristics
    }

    for image in images:
        standard_deviation = get_standard_deviation_of_hue(image)
        divided_images['standard_deviation'].append((standard_deviation, image))
        # Add more divisions based on other hue characteristics

    return divided_images


def get_best_image_standard_deviation(images):
    """
    Determines the image with the best hue using the standard deviation.

    Args:
        images: A list of tuples containing standard deviation value and corresponding images.

    Returns:
        The image with the best hue based on standard deviation.
    """

    best_image = None
    best_standard_deviation = -1

    for standard_deviation, image in images:
        if standard_deviation > best_standard_deviation:
            best_standard_deviation = standard_deviation
            best_image = image

    return best_image


def main():
    # Get the path to the folder containing the images.
    folder_path = Path('C:/Users/USER/Downloads/Youghurt and granola')

    # Get all the images in the folder.
    images = [cv2.imread(str(file)) for file in folder_path.glob("*.jpg")]

    # Divide the images based on standard deviation
    divided_images = divide_images(images)

    # Find the image with the best hue based on standard deviation
    best_image_std_dev = get_best_image_standard_deviation(divided_images['standard_deviation'])

    # Display the best image based on standard deviation
    cv2.imshow("Best Image (Standard Deviation)", best_image_std_dev)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
