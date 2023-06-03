import cv2
import numpy as np
from pathlib import Path

def get_mean_hue(image):
    """
    Calculates the mean hue value of an image.

    Args:
        image: A NumPy array representing an image.

    Returns:
        The mean hue value of the image.
    """

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue_values = hsv_image[:, :, 0]
    mean_hue = np.mean(hue_values)
    return mean_hue


def divide_images(images):
    """
    Divides the images based on different hue characteristics.

    Args:
        images: A list of NumPy arrays representing images.

    Returns:
        A dictionary containing the divided images based on different hue characteristics.
    """

    divided_images = {
        'mean': [],
        # Add more divisions based on other hue characteristics
    }

    for image in images:
        mean_hue = get_mean_hue(image)
        divided_images['mean'].append((mean_hue, image))
        # Add more divisions based on other hue characteristics

    return divided_images


def get_best_image_mean(images):
    """
    Determines the image with the best hue using the mean.

    Args:
        images: A list of tuples containing mean hue value and corresponding images.

    Returns:
        The image with the best hue based on mean.
    """

    best_image = None
    best_mean_hue = -1

    for mean_hue, image in images:
        if mean_hue > best_mean_hue:
            best_mean_hue = mean_hue
            best_image = image

    return best_image


def main():
    # Get the path to the folder containing the images.
    folder_path = Path('C:/Users/USER/Downloads/Youghurt and granola')

    # Get all the images in the folder.
    images = [cv2.imread(str(file)) for file in folder_path.glob("*.jpg")]

    # Divide the images based on mean
    divided_images = divide_images(images)

    # Find the image with the best hue based on mean
    best_image_mean = get_best_image_mean(divided_images['mean'])

    # Display the best image based on mean
    cv2.imshow("Best Image (Mean)", best_image_mean)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
