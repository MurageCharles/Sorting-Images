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
  entropy_of_hue = np.entropy(hue_values)
  return entropy_of_hue

def get_best_image(images):
  """
  Determines the image with the best hue using the methods above.

  Args:
    images: A list of NumPy arrays representing images.

  Returns:
    The image with the best hue.
  """

  best_image = None
  best_mean_hue = -1
  best_median_hue = -1
  best_standard_deviation_of_hue = -1
  best_entropy_of_hue = -1

  for image in images:
    mean_hue = get_mean_hue(image)
    median_hue = get_median_hue(image)
    standard_deviation_of_hue = get_standard_deviation_of_hue(image)
    entropy_of_hue = get_entropy_of_hue(image)

    if mean_hue > best_mean_hue:
      best_mean_hue = mean_hue
      best_image = image
    elif median_hue > best_median_hue:
      best_median_hue = median_hue
      best_image = image
    elif standard_deviation_of_hue < best_standard_deviation_of_hue:
      best_standard_deviation_of_hue = standard_deviation_of_hue
      best_image = image
    elif entropy_of_hue > best_entropy_of_hue:
      best_entropy_of_hue = entropy_of_hue
      best_image = image

  return best_image

def main():
  # Get the path to the folder containing the images.
  folder_path = Path('C:/Users/USER/Downloads/Youghurt and granola')

  # Get all the images in the folder.
  images = [cv2.imread(file) for file in folder_path.]