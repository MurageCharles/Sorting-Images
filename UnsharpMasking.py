import numpy as np
import cv2

def unsharp_masking(image, sigma=1.0, strength=1.0):
    # Convert the image to float
    image = image.astype(np.float32) / 255.0

    # Create a blurred version of the image
    blurred = cv2.GaussianBlur(image, (0, 0), sigma)

    # Calculate the difference between the original and blurred image
    mask = image - blurred

    # Enhance the mask by scaling it with the strength parameter
    enhanced_mask = mask * strength

    # Add the enhanced mask back to the original image
    sharpened = image + enhanced_mask

    # Clip the values to the valid range [0, 1]
    sharpened = np.clip(sharpened, 0, 1)

    # Convert the image back to the original data type (e.g., uint8)
    sharpened = (sharpened * 255).astype(np.uint8)

    return sharpened

# Load the image
image = cv2.imread('C:/Users/USER/Downloads/Youghurt and granola/20230515_090003.jpg')

# Apply the unsharp masking algorithm with custom parameters
sharpened_image = unsharp_masking(image, sigma=1.0, strength=1.5)

# Display the original and sharpened images
cv2.imshow('Original', image)
cv2.imshow('Sharpened', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()