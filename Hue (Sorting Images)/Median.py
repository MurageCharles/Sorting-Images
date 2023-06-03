import cv2
import numpy as np
from pathlib import Path

def get_median_hue(image):
    """
    Calculates the median hue value of an image.

    Args:
        image: A NumPy array representing an image.

    Returns:
        The median hue value of the image.
    """

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue_values = hsv_image[:, :, 0]
    median_hue = np.median(hue_values)
    return median_hue


def divide_images(images):
    """
    Divides the images based on different hue characteristics.

    Args:
        images: A list of NumPy arrays representing images.

    Returns:
        A dictionary containing the divided images based on different hue characteristics.
    """

    divided_images = {
        'median': [],
        # Add more divisions based on other hue characteristics
    }

    for image in images:
        median_hue = get_median_hue(image)
        divided_images['median'].append((median_hue, image))
        # Add more divisions based on other hue characteristics

    return divided_images


def get_best_image_median(images):
    """
    Determines the image with the best hue using the median.

    Args:
        images: A list of tuples containing median hue value and corresponding images.

    Returns:
        The image with the best hue based on median.
    """

    best_image = None
    best_median_hue = -1

    for median_hue, image in images:
        if median_hue > best_median_hue:
            best_median_hue = median_hue
            best_image = image

    return best_image


def main():
    # Get the path to the folder containing the images.
    folder_path = Path('C:/Users/USER/Downloads/Youghurt and granola')

    # Get all the images in the folder.
    images = [cv2.imread(str(file)) for file in folder_path.glob("*.jpg")]

    # Divide the images based on median
    divided_images = divide_images(images)

    # Find the image with the best hue based on median
    best_image_median = get_best_image_median(divided_images['median'])

    # Display the best image based on median
    cv2.imshow("Best Image (Median)", best_image_median)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
